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

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, None, 0xBEEF)

# Grabbing the config in a named tuple.
config = e32.get_config()

print("Current config:")

print("* Address: " + binascii.hexlify(config.address, ":").decode("utf-8"))

print("* UART Parity:")
print("  * Value: " + bin(config.uart_parity))
for const_name, value in ebyte_e32.SerialParity.__dict__.items():
    if value == config.uart_parity:
        print("  * Const: " + const_name)
        break  # Avoids printing the default constants

print("* UART Rate:")
print("  * Value: " + bin(config.uart_rate))
for const_name, value in ebyte_e32.SerialBaudRate.__dict__.items():
    # FIXME: NOT WORKING: Matches the first !
    if value[0] == config.uart_parity:
        print("  * Const: " + const_name)
        print("  * Baudrate: " + str(value[1]))
        break  # Avoids printing the default constants
