# SPDX-FileCopyrightText: 2023 Herwin Bozet
#
# SPDX-License-Identifier: Unlicense

import board

import ebyte_e32

PIN_M0 = board.IO13
PIN_M1 = board.IO12
PIN_RXD = board.IO11  # Pin marked as RX on the module
PIN_TXD = board.IO10  # Pin marked as TX on the module
PIN_AUX = board.IO9

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD)

# These pins can also be given in their `digitalio.DigitalIO` and `busio.UART` variant.
# e32 = ebyte_e32.E32Device(DigitalIO, DigitalIO, DigitalIO, Null, Null, UART)

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
