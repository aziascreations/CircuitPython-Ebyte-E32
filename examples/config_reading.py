# SPDX-FileCopyrightText: 2023 Herwin Bozet
#
# SPDX-License-Identifier: Unlicense

import binascii
import board

import ebyte_e32

PIN_M0 = board.IO13
PIN_M1 = board.IO12
PIN_RXD = board.IO11  # Pin marked as RX on the module
PIN_TXD = board.IO10  # Pin marked as TX on the module
PIN_AUX = board.IO9

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD)

# /!\ This operation will cause the module to go into sleep mode and flush the UART buffer /!\

# Grabbing the config in a named tuple.
config = e32.get_config()

print(config)

# Output:
# E32DeviceConfig(
#     address=b'\x00\x00',
#     uart_parity=0,
#     uart_rate=3,
#     data_rate=2,
#     channel=0,
#     tx_mode=0,
#     io_drive_mode=1,
#     wake_up_time=0,
#     forward_error_correction=1,
#     tx_power=3
# )
