# SPDX-FileCopyrightText: 2023 Herwin Bozet
#
# SPDX-License-Identifier: Unlicense

import board
import time

import ebyte_e32

PIN_M0 = board.B3
PIN_M1 = board.B4
PIN_RXD = board.A2  # Pin marked as RX on the module
PIN_TXD = board.A3  # Pin marked as TX on the module
PIN_AUX = board.B7

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, address=0x1337, channel=4)

# Switching to transparent transmission mode.  (Default)
e32.tx_mode = ebyte_e32.TransmissionMode.TRANSMISSION_TRANSPARENT

# Switching to mode 0.  (Normal mode)
e32.mode = ebyte_e32.Modes.MODE_NORMAL

print(f"Waiting for messages on channel {e32.channel} between devices with the 0x{e32.address:x} address ...")

while True:
    # Checking if the module sent us some data
    if e32.in_buffer > 0:
        # Wait for the module to finish receiving data
        e32.wait_aux()
        
        # We grab the data, and can process it here
        data = e32.read()
        
        # We print it and exit
        print(f"We received a {len(data)} byte(s) long message:")
        print(data)
    
    # If nothing was received, we wait.
    time.sleep(0.1)

print()
print("Now exiting...")
e32.deinit()
