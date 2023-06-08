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

# The E32 module should be available and configured with the these parameters by default:
#  * Address: 0x0000
#  * UART parity: 8N1 (8 data bits, no parity)
#  * UART rate: 9600 bps
#  * Air data rate: 2.4 kbps
#  * Channel: 0
#  * TX mode: Transparent
#  * IO drive mode: TX and AUX as push-pull, RX as pull-up
#  * Wake-up time: 250ms
#  * Forward error correction: Enabled
#  * TX power: The lowest available

# /!\ Each configuration change will cause the module to go into sleep mode and flush the UART buffer /!\

# Changing the address
print(f"Old address: 0x{e32.address:x}")
e32.address = 0x1337
print(f"New address: 0x{e32.address:x}")

# TODO: Other parameters...
