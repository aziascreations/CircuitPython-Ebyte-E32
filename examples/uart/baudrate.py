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

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, address=0x1377, channel=4)

# Setting the non-sleep UART bus speed
e32.uart_rate = ebyte_e32.SerialBaudRate.BAUD_19200
print(f"Sleep mode BPS: {e32.uart_rate}")

# Switching to mode 0.  (Normal mode)
e32.mode = ebyte_e32.Modes.MODE_NORMAL
print(f"Normal mode BPS: {e32.uart_rate}")

# We are now communicating with the module at 19200 bps.
# If we go back to sleep mode, we'll be automatically put back at 9600.
# Sending messages here will work on a module that uses the same air data rate and ANY UART baudrate.

# Switching back to sleep mode.
e32.mode = ebyte_e32.Modes.MODE_SLEEP
print(f"Sleep mode BPS: {e32.uart_rate}")

