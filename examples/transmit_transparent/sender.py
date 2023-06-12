# SPDX-FileCopyrightText: 2023 Herwin Bozet
#
# SPDX-License-Identifier: Unlicense

import board
import time

import ebyte_e32

PIN_M0 = board.IO13
PIN_M1 = board.IO12
PIN_RXD = board.IO11  # Pin marked as RX on the module
PIN_TXD = board.IO10  # Pin marked as TX on the module
PIN_AUX = board.IO9

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, address=0x1337, channel=4)

# Switching to fixed transmission mode.
e32.tx_mode = ebyte_e32.TransmissionMode.TRANSMISSION_TRANSPARENT

# Switching to mode 0.  (Normal mode)
e32.mode = ebyte_e32.Modes.MODE_NORMAL

# Message content:
#  * Message: b'Hello World !'
# The target channel and address are the same as the module's.
message = b'Hello World !'

# Sending with helper
e32.send(message)

time.sleep(0.5)  # Waiting to prevent RF spamming

# Switching to an empty shared address and sending another message.
e32.address = 0xBEEF
message = b'You shouldn\'t receive this !'
e32.send(message)
e32.wait_aux()

# The message may be truncated at specific lengths depending on the frequencies used.
# Please check the documentation for more information !
