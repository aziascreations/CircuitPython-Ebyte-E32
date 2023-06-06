"""
`ebyte_e32`
====================================================
* Author(s): Herwin Bozet
"""

try:
    from typing import Union, Optional
except ImportError:
    pass

from binascii import hexlify
from busio import UART
from digitalio import Direction, DigitalInOut
from microcontroller import Pin
from time import sleep

# TODO: Remove useless imports from minified version


class Modes:
    """
    Refers to the E32 module's operating modes set via the `M0` and `M1` pins.
    
    The constants' values are organized in the following manner:
    `list[M0: int, M1_Value: int]`
    """
    
    MODE_NORMAL = (0, 0)
    """
    UART and LoRa radio are ready to receive and return packages.
    
    Also known as `Mode 0`.
    """
    
    MODE_WAKE_UP = (1, 0)
    """
    Same as normal mode, with a preamble added to sent data to wake up the receiver.
    
    The preamble's code length depends on the [???] set in the module operating configuration.
    
    Also known as `Mode 1`.
    """
    
    MODE_POWER_SAVE = (0, 1)
    """
    TODO
    """
    
    MODE_SLEEP = (1, 1)
    """
    Puts the module in sleep mode where the LoRa radio is turned off and the UART bus
    can be used to set and get the module's parameters, or reset it.
    
    Also known as `Mode 3`.
    """


class SerialParity:
    """
    aaa
    """
    
    PARITY_NONE = 0b00
    "Same as 8N1"
    
    PARITY_ODD = 0b01
    "Same as 8O1"
    
    PARITY_EVEN = 0b10
    "Same as 8E1"
    
    PARITY_DEFAULT = PARITY_NONE
    "Default UART parity on E32 devices"


class SerialBaudRate:
    """
    UART baud rate for all communications between the module and the MCU.
    
    It is not related to the LoRa transmission rate and can be different between communicating modules.
    """
    
    BAUD_1200 = (0b000, 1200)
    "Equal to 1200 bps"
    
    BAUD_2400 = (0b001, 2400)
    "Equal to 2400 bps"
    
    BAUD_4800 = (0b010, 4800)
    "Equal to 4800 bps"
    
    BAUD_9600 = (0b011, 9600)
    "Equal to 9600 bps  (Default)"
    
    BAUD_19200 = (0b100, 19200)
    "Equal to 19200 bps"
    
    BAUD_38400 = (0b101, 38400)
    "Equal to 38400 bps"
    
    BAUD_57600 = (0b110, 57600)
    "Equal to 57600 bps"
    
    BAUD_115200 = (0b111, 115200)
    "Equal to 115200 bps"
    
    BAUD_DEFAULT = BAUD_9600
    "Default baud rate on E32 devices"


class AirDataRate:
    """
    ???
    
    This rate must be the same between all [members of a communication].
    """
    
    RATE_0_3K = 0b000
    "Equal to 0.3 kbps"
    
    RATE_1_2K = 0b001
    "Equal to 1.2 kbps"
    
    RATE_2_4K = 0b010
    "Equal to 2.4 kbps"
    
    RATE_4_8K = 0b011
    "Equal to 4.8 kbps"
    
    RATE_9_6K = 0b100
    "Equal to 9.6 kbps"
    
    RATE_19_2K = 0b101
    "Equal to 19.2 kbps"
    
    RATE_DEFAULT = RATE_2_4K
    "Default air data rate on E32 devices"


TX_POWER_MIN = 0b00
"""Minimal allowed TX power value.  (Inclusive)"""

TX_POWER_MAX = 0b11
"""Maximal allowed TX power value.  (Inclusive)"""

CHANNEL_MIN = 0
"""Minimal allowed channel number.  (Inclusive)"""

CHANNEL_MAX = 31
"""Maximal allowed channel number.  (Inclusive)"""


class E32Device:
    """
    sbc
    """
    
    m0: DigitalInOut
    """M0 pin used to set the module's mode."""
    
    m1: DigitalInOut
    """M1 pin used to set the module's mode."""
    
    aux: Optional[DigitalInOut]
    """
    AUX pin used by the module to indicate its working status or to wake up the MCU.
    
    May be left floating and ignored during normal operations.
    """
    
    uart: UART
    """
    UART connection to the E32 module.
    """
    
    _address: int
    _uart_parity: Union[int, SerialParity]
    _uart_rate: Union[tuple[int, int], SerialBaudRate]
    _data_rate: Union[int, AirDataRate]
    _channel: int
    _tx_power: int
    
    def __init__(self,
                 pin_m0: Union[Pin, DigitalInOut],
                 pin_m1: Union[Pin, DigitalInOut],
                 pin_aux: Optional[Union[Pin, DigitalInOut]],
                 pin_tx: Optional[Pin],
                 pin_rx: Optional[Pin],
                 uart: Optional[UART],
                 address: int = 0x0000,
                 uart_parity: Union[int, SerialParity] = SerialParity.PARITY_NONE,
                 uart_rate: Union[tuple[int, int], SerialBaudRate] = SerialBaudRate.BAUD_DEFAULT,
                 data_rate: Union[int, AirDataRate] = AirDataRate.RATE_DEFAULT,
                 channel: int = 0,
                 # TODO: Add missing config fields
                 tx_power: int = 0b00,
                 ):
        # Preparing pins
        self.m0 = pin_m0 if pin_m0 is DigitalInOut else DigitalInOut(pin_m0)
        self.m1 = pin_m1 if pin_m1 is DigitalInOut else DigitalInOut(pin_m1)
        self.aux = pin_aux if (pin_aux is DigitalInOut or pin_aux is None) else DigitalInOut(pin_aux)
        
        if uart is not None:
            self.uart = uart
        elif pin_tx is not None and pin_rx is not None:
            self.uart = UART(pin_rx, pin_tx)
        else:
            raise ValueError("No UART bus or TX and RX pins given !")
        
        # Correcting some pin-related stuff
        self.m0.direction = Direction.OUTPUT
        self.m1.direction = Direction.OUTPUT
        if self.aux is not None:
            self.aux.direction = Direction.INPUT
        
        # Saving configuration values
        self._address = address
        self._uart_parity = uart_parity
        self._uart_rate = uart_rate
        self._data_rate = data_rate
        self._channel = channel
        # TODO: Add missing config fields
        self._tx_power = tx_power
        
        # Validating and applying configuration
        self.mode = Modes.MODE_SLEEP
        
        # TODO: Check if it works.
    
    def __del__(self):
        self.deinit()
    
    def deinit(self):
        """
        Deinitializes the E32 module instance and all its pins.
        
        :return: ``None``
        """
        # ? => deinit_pins: bool = True
        self.m0.deinit()
        self.m1.deinit()
        self.uart.deinit()
    
    def flush_uart(self):
        """
        Empties out the UART buffer if possible.
        
        :return: ``None``
        """
        if self.uart.in_waiting > 0:
            self.uart.read(self.uart.in_waiting)
    
    def wait_aux(self):
        """
        Wait for the `AUX` pin to go high meaning that the module is ready for communications.
        
        If no `AUX` pin was given, or if it stays low, the waiting period will be 150ms at most.
        
        :return: ``None``
        """
        if self.aux is None:
            sleep(0.1)
            return
        
        wait_loop_count = 0
        while not self.aux.value and wait_loop_count < 14:
            print("Waiting for AUX...")
            sleep(0.01)
            wait_loop_count += 1
        
        # Waiting just a bit more, this helps fix some timing issues when AUX is high but data wasn't sent yet.
        # This shouldn't be happening, but it does, so...
        sleep(0.01)
    
    def update_config(self, make_permanent: bool = False, verify: bool = True) -> None:
        """
        Applies the current config to the module.
        
        **The module will temporarily go into sleep mode and flush the UART buffer.**
        
        :param make_permanent: Whether the config should be saved when the module is powered-down.  (Default: ``False``)
        :param verify: Whether the config should be fetched and checked afterward.  (Default: ``True``)
        :return: ``None``
        :raises RuntimeError: If the config couldn't be applied.
        """
        print("Updating module's config...")
        
        original_mode = self.mode
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = Modes.MODE_SLEEP
        
        command = bytearray(6)
        command[0] = 0xC0 if make_permanent else 0xC2
        command[1] = (self._address & 0xFF00) >> 8
        command[2] = self._address & 0xFF
        command[3] = ((self._uart_parity & 0b11) << 6) | \
                     ((self._uart_rate[0] & 0b111) << 3) | \
                     (self._data_rate & 0b111)
        command[4] = self._channel & 0b00011111
        command[5] = 0b01000100 | (self._tx_power & 0b11)
        
        print(hexlify(command, '-'))
        
        # Preparing the UART bus
        self.uart.baudrate = 9600
        self.flush_uart()
        
        # Sending config
        if self.uart.write(command) != 6:
            raise RuntimeError("Failed to send the parameters configuration command !")
        
        # Waiting for module to react
        self.wait_aux()
        
        # Flushing data returned by the module.
        # The datasheet doesn't mention explicitly that it returns the new config, so I won't take the risk.
        self.flush_uart()
        
        if verify:
            raw_config = self.get_raw_config()
            print("Raw: ")
            print(hexlify(command, '-'))
            if raw_config[1:] != command[1:]:
                raise RuntimeError("The module doesn't return the new config !")
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = original_mode
            self.uart.baudrate = self._uart_rate[1]
    
    def get_raw_config(self) -> bytes:
        """
        Fetches the raw operating config from the module and returns it.
        
        **The module will temporarily go into sleep mode and flush the UART buffer.**
        
        :return: The raw response as a ``bytes`` object of length 6.
        """
        original_mode = self.mode
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = Modes.MODE_SLEEP
        
        self.uart.write(b'\xC1\xC1\xC1')
        self.wait_aux()
        if self.uart.in_waiting != 6:
            raise RuntimeError("The operating parameters request returned {} byte(s) instead of 6 !".format(
                self.uart.in_waiting
            ))
        raw_config = self.uart.read(6)
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = original_mode
            self.uart.baudrate = self._uart_rate[1]
        
        return raw_config
    
    @property
    def mode(self) -> Union[tuple[int, int], Modes]:
        """
        Module's mode as it is or should be represented on the `M0` and `M1` pins.
        
        **Changing this property will flush the UART buffer.**
        """
        return self.m0.value, self.m1.value
    
    @mode.setter
    def mode(self, value: Union[tuple[int, int], Modes]):
        self.m0.value = value[0]
        self.m1.value = value[1]
        self.wait_aux()
        self.uart.baudrate = 9600 if self.mode == Modes.MODE_SLEEP else self._uart_rate[1]
        self.flush_uart()
    
    @property
    def tx_power(self) -> int:
        """
        Module's TX power as transmitted via the save parameters command.
        
        Must be between ``TX_POWER_MIN`` and ``TX_POWER_MAX``, both are inclusive.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._tx_power
    
    @tx_power.setter
    def tx_power(self, value: int):
        if not (0b00 <= value <= 0b11):
            raise ValueError(f"The 'tx_power' isn't between 0 and 3 !  (It's {value})")
        self._tx_power = value
        self.update_config()


# if not (0 <= self.channel <= 31):
#     raise ValueError(f"The 'channel' isn't between 0 and 31 !  (It's {self.channel})")
