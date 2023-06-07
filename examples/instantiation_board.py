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

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, None, 0xBEEF)
