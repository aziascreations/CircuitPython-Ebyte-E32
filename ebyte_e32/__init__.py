# SPDX-FileCopyrightText: Copyright (c) 2023 Herwin Bozet
#
# SPDX-License-Identifier: MIT
"""
`ebyte_e32`
====================================================
* Author(s): Herwin Bozet
"""

try:
    from typing import Union, Optional, Tuple
except ImportError:
    pass

from busio import UART
from collections import namedtuple
from digitalio import Direction, DigitalInOut
from microcontroller import Pin
from time import sleep


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
    The UART bus is disabled, and the module waits for incoming messages with the appropriate preambles.
    
    Once received, AUX goes low for ~5ms and the UART bus is re-opened, it sends the message, and AUX goes high again.
    
    Also known as `Mode 2` or `PS Mode`.
    """
    
    MODE_SLEEP = (1, 1)
    """
    Puts the module in sleep mode where the LoRa radio is turned off and the UART bus
    can be used to set and get the module's parameters, or reset it.
    
    Also known as `Mode 3`.
    """


class SerialParity:
    """
    ???  (? In non-sleep modes)
    
    This setting isn't related to the LoRa transmission rate and can be different between communicating modules.
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
    UART baud rate for all communications between the module and the MCU.  (? In non-sleep modes)
    
    This setting isn't related to the LoRa transmission rate and can be different between communicating modules.
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
    Data rate in bps at which LoRa modules communicate between each other.
    
    **This setting directly affects the maximum packet size and communication range !**
    
    **This setting must be the same between all communicating modules.**
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


class TransmissionMode:
    """
    ???
    """
    
    TRANSMISSION_TRANSPARENT = 0b0
    "???"
    
    TRANSMISSION_FIXED = 0b1
    "???"
    
    TRANSMISSION_DEFAULT = TRANSMISSION_TRANSPARENT
    """
    Default transmission mode on E32 devices.
    
    This is not explicitly indicated in the E32 datasheets, but this is the case in practice.
    """


class WakeUpTime:
    """
    ???
    
    [Not on mode 0 !]
    
    This setting isn't related to the LoRa transmission rate and can be different between communicating modules.
    """
    
    WAKE_TIME_250MS = 0b000
    "???"
    
    WAKE_TIME_500MS = 0b001
    "???"
    
    WAKE_TIME_750MS = 0b010
    "???"
    
    WAKE_TIME_1000MS = 0b011
    "???"
    
    WAKE_TIME_1250MS = 0b100
    "???"
    
    WAKE_TIME_1500MS = 0b101
    "???"
    
    WAKE_TIME_1750MS = 0b110
    "???"
    
    WAKE_TIME_2000MS = 0b111
    "???"
    
    WAKE_TIME_DEFAULT = WAKE_TIME_250MS
    "Default wake-up time on E32 devices"


class IODriveMode:
    """
    ???
    
    This setting isn't related to the LoRa transmission rate and can be different between communicating modules.
    """
    
    DRIVE_OPEN = 0b0
    """
    Both `TX` and `AUX` pins will be push-pull outputs.
    
    The `RX` pin will be a pull-up input.
    """
    
    DRIVE_PULL = 0b1
    """
    Both `TX` and `AUX` pins will be open-collector outputs.
    
    The `RX` pin will be an open-collector input.
    """
    
    DRIVE_DEFAULT = DRIVE_PULL
    "Default IO drive mode E32 devices"


class ForwardErrorCorrection:
    """
    ???
    
    **This setting must be the same between all communicating modules.**
    """
    
    FEC_DISABLED = False
    "Enables forward error correction"
    
    FEC_ENABLE = True
    "Disables forward error correction"
    
    FEC_DEFAULT = FEC_ENABLE
    "Default FEC status on E32 devices"


CHANNEL_MIN = 0
"""Minimal allowed channel number.  (Inclusive)"""

CHANNEL_MAX = 31
"""Maximal allowed channel number.  (Inclusive)"""


TX_POWER_MIN = 0b00
"""Minimal allowed TX power value.  (Inclusive)"""

TX_POWER_MAX = 0b11
"""Maximal allowed TX power value.  (Inclusive)"""


E32DeviceVersion = namedtuple("E32DeviceVersion", (
    "model", "version", "features"
))
"""Named tuple returned by the `E32DeviceConfig` when fetching the module's version."""


E32DeviceConfig = namedtuple("E32DeviceConfig", (
    "address", "uart_parity", "uart_rate", "data_rate", "channel", "tx_mode", "io_drive_mode", "wake_up_time",
    "forward_error_correction", "tx_power"
))
"""Named tuple returned by the `E32DeviceConfig` when fetching the module's current config."""


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
    
    _uart_pin_tx: Pin
    _uart_pin_rx: Pin
    _uart_buffer_size: int
    
    _address: int
    _uart_parity: Union[int, SerialParity]
    _uart_rate: Union[tuple[int, int], SerialBaudRate]
    _data_rate: Union[int, AirDataRate]
    _channel: int
    _tx_mode: int
    _io_drive_mode: int
    _wake_up_time: int
    _fec: bool
    _tx_power: int
    
    def __init__(self,
                 pin_m0: Pin,
                 pin_m1: Pin,
                 pin_aux: Optional[Pin],
                 pin_tx: Pin,
                 pin_rx: Pin,
                 uart_buffer_size: int = 64,
                 address: int = 0x0000,
                 uart_parity: Union[int, SerialParity] = SerialParity.PARITY_NONE,
                 uart_rate: Union[tuple[int, int], SerialBaudRate] = SerialBaudRate.BAUD_DEFAULT,
                 data_rate: Union[int, AirDataRate] = AirDataRate.RATE_DEFAULT,
                 channel: int = 0,
                 tx_mode: Union[int, TransmissionMode] = TransmissionMode.TRANSMISSION_DEFAULT,
                 io_drive_mode: Union[int, IODriveMode] = IODriveMode.DRIVE_DEFAULT,
                 wake_up_time: Union[int, WakeUpTime] = WakeUpTime.WAKE_TIME_DEFAULT,
                 forward_error_correction: Union[bool, ForwardErrorCorrection] = True,
                 tx_power: int = 0b11,
                 ):
        # Preparing pins
        self.m0 = DigitalInOut(pin_m0)
        self.m1 = DigitalInOut(pin_m1)
        self.aux = None if pin_aux is None else DigitalInOut(pin_aux)
        
        # Preparing UART bus
        self._uart_pin_tx = pin_rx
        self._uart_pin_rx = pin_tx
        self._uart_buffer_size = uart_buffer_size
        self.uart = None
        self.prepare_uart(9600, None)
        
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
        self._tx_mode = tx_mode
        self._io_drive_mode = io_drive_mode
        self._wake_up_time = wake_up_time
        self._fec = forward_error_correction
        self._tx_power = tx_power
        
        # Checking if the module works by fetching its version and not getting any data validation errors.
        self.mode = Modes.MODE_SLEEP
        self.get_version()
        
        # Validating and applying configuration
        self.update_config()
    
    def __del__(self):
        self.deinit()
    
    def deinit(self):
        """
        Deinitializes the E32 module instance and liberates all used pins.
        
        :return: ``None``
        """
        self.reset()
        self.m0.deinit()
        self.m1.deinit()
        if self.aux is not None:
            self.aux.deinit()
        self.uart.deinit()
    
    def prepare_uart(self, baudrate: int, parity: Optional[UART.Parity]):
        """
        Prepares the UART bus for further communications.
        
        :param baudrate: Baudrate used by the new UART bus.
        :param parity: Parity used by the new UART bus.
        :return: ``None``
        """
        if self.uart is not None:
            self.flush_uart()
            self.uart.deinit()
        
        self.uart = UART(
            self._uart_pin_tx, self._uart_pin_rx,
            parity=parity, baudrate=baudrate,
            receiver_buffer_size=self._uart_buffer_size)
    
    def flush_uart(self):
        """
        Empties out the UART buffer if possible.
        
        :return: ``None``
        """
        self.uart.reset_input_buffer()
    
    def wait_aux(self, max_wait_ms: int = 150):
        """
        Wait for the `AUX` pin to go high meaning that the module is ready for communications.
        
        If no `AUX` pin was given, or if it stays low, the waiting period will be 150ms at most.
        
        :type max_wait_ms: Max amount of time in milliseconds to wait for the `AUX` pin to go high.  (Default: ``150``)
        :return: ``None``
        """
        if self.aux is None:
            sleep(max_wait_ms / 1000)
            return
        
        wait_loop_count = 0
        while not self.aux.value and wait_loop_count < (max_wait_ms / 10) - 1:
            # print("Waiting for AUX...")
            sleep(0.01)
            wait_loop_count += 1
        
        # Waiting just a bit more, this helps fix some timing issues when AUX is high but data wasn't sent yet.
        # This shouldn't be happening, but it does, so... yeah...
        sleep(0.01)
    
    def send(self, message: bytes, max_packet_size: Optional[int] = None):
        """
        Sends a message on the UART bus.
        
        :param message: Message to be sent, may get truncated.
        :param max_packet_size: Max byte count to send, if `None`, the message's length will be used.
        :return: The numbers of bytes written.
        """
        if max_packet_size is None:
            max_packet_size = len(message)
        
        return self.uart.write(message[:max_packet_size])
    
    def update_config(self, make_permanent: bool = False, verify: bool = True) -> None:
        """
        Applies the current config to the module.
        
        **The module will temporarily go into sleep mode and flush the UART buffer.**
        
        :param make_permanent: Whether the config should be saved when the module is powered-down.  (Default: ``False``)
        :param verify: Whether the config should be fetched and checked afterward.  (Default: ``True``)
        :return: ``None``
        :raises RuntimeError: If the config couldn't be applied.
        """
        # print("Updating module's config...")
        
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
        command[5] = ((self._tx_mode & 0b1) << 7) | \
                     ((self._io_drive_mode & 0b1) << 6) | \
                     ((self._wake_up_time & 0b111) << 3) | \
                     ((self._fec & 0b1) << 2) | \
                     (self._tx_power & 0b11)
        
        # Preparing the UART bus
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
            if raw_config[1:] != command[1:]:
                raise RuntimeError("The module doesn't return the new config !")
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = original_mode
    
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
        
        return raw_config
    
    def get_config(self) -> E32DeviceConfig:
        raw_config = self.get_raw_config()
        
        return E32DeviceConfig(
            raw_config[1:3],  # Address
            (raw_config[3] & 0b11000000) >> 6,  # UART Parity
            (raw_config[3] & 0b111000) >> 3,  # UART Rate
            raw_config[3] & 0b111,  # Air data rate
            raw_config[4] & 0b11111,  # Channel
            (raw_config[5] & 0b10000000) >> 7,  # Transmission mode
            (raw_config[5] & 0b1000000) >> 6,  # IO drive mode
            (raw_config[5] & 0b111000) >> 3,  # Wake-up time
            (raw_config[5] & 0b100) >> 2,  # FEC status
            raw_config[5] & 0b11,  # TX Power
        )
    
    def get_raw_version(self) -> bytes:
        """
        Fetches the raw version number and returns it.
        
        **The module will temporarily go into sleep mode and flush the UART buffer.**
        
        :return: The raw response as a ``bytes`` object of length 4.
        """
        original_mode = self.mode
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = Modes.MODE_SLEEP
        
        self.uart.write(b'\xC3\xC3\xC3')
        self.wait_aux()
        if self.uart.in_waiting != 4:
            raise RuntimeError("The operating parameters request returned {} byte(s) instead of 4 !".format(
                self.uart.in_waiting
            ))
        raw_version = self.uart.read(4)
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = original_mode
        
        return raw_version
    
    def get_version(self) -> E32DeviceVersion:
        """
        Fetches the module's model, version number and its features.
        
        **Ebyte's documentation doesn't explain the content of the second and third values in details.**
        
        :return: A tuple containing the module's model, its version number, ant its features
        """
        raw_version = self.get_raw_version()
        
        if raw_version[0] != 0xC3:
            raise RuntimeError("The version data has a bad response code !")
        
        if raw_version[1] != 0x32:
            raise RuntimeError("The version data has an invalid model !")
        
        return E32DeviceVersion(raw_version[1], raw_version[2], raw_version[3])
    
    def reset(self, stay_in_sleep_mode: bool = True):
        """
        Sends the `RESET` command to the module and stays in sleep mode waiting for further configuration unless
        instructed not to.
        
        The module is left in sleep mode to prevent rogue communications with an undesired operating configuration.
        
        **The module will temporarily go into sleep mode and flush the UART buffer.**
        
        **The module will likely be unresponsive for a couple of seconds !**
        
        :param stay_in_sleep_mode: Whether the module should be left in sleep mode after the reset.  (Default: ``True``)
        :return: ``None``
        """
        original_mode = self.mode
        
        if original_mode != Modes.MODE_SLEEP:
            self.mode = Modes.MODE_SLEEP
        
        self.uart.write(b'\xC4\xC4\xC4')
        self.wait_aux(1500)  # May not be enough, it doesn't respond directly, even if AUX is high...
        
        if not stay_in_sleep_mode and original_mode != Modes.MODE_SLEEP:
            self.mode = original_mode
    
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
        self.prepare_uart(
            baudrate=9600 if self.mode == Modes.MODE_SLEEP else self._uart_rate[1],
            parity=(
                None if self.mode == Modes.MODE_SLEEP or self.uart_parity == SerialParity.PARITY_NONE else (
                    UART.Parity.ODD if self.uart_parity == SerialParity.PARITY_ODD else UART.Parity.EVEN
                )
            )
        )
        self.flush_uart()
    
    @property
    def address(self) -> int:
        """
        Module's address that is used in "fixed transmissions" and ignored when receiving broadcast messages.
        
        Must be between ``0x0000`` and ``0xFFFF``.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._address
    
    @address.setter
    def address(self, value: int):
        if not (0x0000 <= value <= 0xFFFF):
            raise ValueError(f"The 'address' isn't between 0x0000 and 0xFFFF !  (It's {value})")
        self._address = value
        self.update_config()
    
    @property
    def uart_parity(self) -> int:
        """
        Module's UART parity used on the `RX` and `TX` lines when in non-sleep modes,
        as transmitted via the save parameters command.
        
        Must be between one of the values in ``SerialParity``.
        
        This value is automatically applied to the uart bus when switching modes.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._uart_parity
    
    @uart_parity.setter
    def uart_parity(self, value: int):
        if not (0b00 <= value <= 0b11):
            raise ValueError(f"The 'uart_parity' isn't between 0 and 3 !  (It's {value})")
        self._uart_parity = value
        self.update_config()
    
    @property
    def uart_rate(self) -> tuple[int, int] | SerialBaudRate:
        """
        Module's UART rate used on the `RX` and `TX` lines when in non-sleep modes.
        
        Must be between one of the values in ``SerialBaudRate``.
        
        This value is automatically applied to the uart bus when switching modes.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._uart_rate
    
    @uart_rate.setter
    def uart_rate(self, value: tuple[int, int] | SerialBaudRate):
        if not (0b000 <= value[0] <= 0b111):
            raise ValueError(f"The 'uart_rate' isn't between 0 and 7 !  (It's {value[0]})")
        self._uart_rate = value
        self.update_config()
    
    @property
    def data_rate(self) -> int | AirDataRate:
        """
        Module's data rate for any LoRa communications in non-sleep modes.
        
        Must be between one of the values in ``AirDataRate``.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._data_rate
    
    @data_rate.setter
    def data_rate(self, value: int | AirDataRate):
        if not (0b000 <= value <= 0b111):
            raise ValueError(f"The 'data_rate' isn't between 0 and 7 !  (It's {value})")
        self._data_rate = value
        self.update_config()
    
    @property
    def channel(self) -> int:
        """
        Module's channel used for any LoRa communications in non-sleep modes.
        
        **FIXME: Check how this applies to different TX modes !  (May be bypassed)**
        
        Must be between ``CHANNEL_MIN`` and ``CHANNEL_MAX``.  (Both are inclusive limits)
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._channel
    
    @channel.setter
    def channel(self, value: int):
        if not (CHANNEL_MIN <= value <= CHANNEL_MAX):
            raise ValueError(f"The 'channel' isn't between {CHANNEL_MIN} and {CHANNEL_MAX} !  (It's {value})")
        self._channel = value
        self.update_config()
    
    @property
    def tx_mode(self) -> int | TransmissionMode:
        """
        Module's transmission mode used for any LoRa communications in non-sleep modes.
        
        **FIXME: Check how this applies to different channels !  (May bypass them)**
        
        Must be between one of the values in ``TransmissionMode``.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._tx_mode
    
    @tx_mode.setter
    def tx_mode(self, value: int | TransmissionMode):
        if not (0 <= value <= 1):
            raise ValueError(f"The 'tx_mode' isn't between 0 and 1 !  (It's {value})")
        self._tx_mode = value
        self.update_config()
    
    @property
    def io_drive_mode(self) -> int | IODriveMode:
        """
        Module's IO drive mode for its ``RX``, ``TX`` and ``AUX`` pins.
        
        Must be between one of the values in ``IODriveMode``.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._io_drive_mode
    
    @io_drive_mode.setter
    def io_drive_mode(self, value: int | IODriveMode):
        if not (0 <= value <= 1):
            raise ValueError(f"The 'io_drive_mode' isn't between 0 and 1 !  (It's {value})")
        self._io_drive_mode = value
        self.update_config()
    
    @property
    def wake_up_time(self) -> int | WakeUpTime:
        """
        Module's wake-up time when in non-sleep and non-normal modes.
        
        Must be between one of the values in ``WakeUpTime``.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._wake_up_time
    
    @wake_up_time.setter
    def wake_up_time(self, value: int | WakeUpTime):
        if not (0b000 <= value <= 0b111):
            raise ValueError(f"The 'wake_up_time' isn't between 0 and 7 !  (It's {value})")
        self._wake_up_time = value
        self.update_config()
    
    @property
    def forward_error_correction(self) -> bool | ForwardErrorCorrection:
        """
        Module's forward error correction toggle for any LoRa communications when in non-sleep modes.
        
        Must be between one of the values in ``ForwardErrorCorrection``.
        
        **Changing this property will cause the module to temporarily go into sleep mode and flush the UART buffer.**
        """
        return self._fec
    
    @forward_error_correction.setter
    def forward_error_correction(self, value: bool | ForwardErrorCorrection):
        self._fec = value
        self.update_config()
    
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
