# SPDX-FileCopyrightText: 2023 Herwin Bozet
#
# SPDX-License-Identifier: Unlicense

import board

from busio import UART
from digitalio import DigitalInOut

import ebyte_e32

PIN_M0 = board.IO13
PIN_M1 = board.IO12
PIN_RXD = board.IO11  # Pin marked as RX on the module
PIN_TXD = board.IO10  # Pin marked as TX on the module
PIN_AUX = board.IO9

e32 = ebyte_e32.E32Device(
    pin_m0=DigitalInOut(PIN_M0),    # Direction is set in constructor.
    pin_m1=DigitalInOut(PIN_M1),    # Direction is set in constructor.
    pin_aux=DigitalInOut(PIN_AUX),  # Direction is set in constructor.
    pin_tx=None,
    pin_rx=None,
    uart=UART(PIN_RXD, PIN_TXD),  # Parameters are set when the module changes its mode.
    address=0x0000,
    uart_parity=ebyte_e32.SerialParity.PARITY_DEFAULT,
    uart_rate=ebyte_e32.SerialBaudRate.BAUD_DEFAULT,
    data_rate=ebyte_e32.AirDataRate.RATE_DEFAULT,
    channel=0,  # Between: [0; 31]
    tx_mode=ebyte_e32.TransmissionMode.TRANSMISSION_DEFAULT,
    io_drive_mode=ebyte_e32.IODriveMode.DRIVE_DEFAULT,
    wake_up_time=ebyte_e32.WakeUpTime.WAKE_TIME_DEFAULT,
    forward_error_correction=ebyte_e32.ForwardErrorCorrection.FEC_DEFAULT,
    tx_power=0b11,  # Highest: 0b00 => Lowest: 0b11
)

# All the config parameters have the same value as if they weren't given to the constructor.
