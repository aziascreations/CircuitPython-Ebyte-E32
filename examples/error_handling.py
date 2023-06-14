# SPDX-FileCopyrightText: 2023 Herwin Bozet
#
# SPDX-License-Identifier: Unlicense

import board
import time

import ebyte_e32
import ebyte_e32.exceptions

PIN_M0 = board.B3
PIN_M1 = board.B4
PIN_RXD = board.A2  # Pin marked as RX on the module
PIN_TXD = board.A3  # Pin marked as TX on the module
PIN_AUX = board.B7

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, address=0x1337, channel=0)

# We'll be iterating over each channel
channel = 0
while True:
    print(f"Moving to channel {channel}")
    
    try:
        # Can cause errors if the module fails to respond to config request when validating it.
        e32.channel = channel
        e32.wait_aux()
    except ebyte_e32.exceptions.E32GenericError:
        print("Failed to change !")
        
        # We reset it and wait more than what AUX indicates.
        e32.reset(True)
        time.sleep(2)
        
        # We re-apply the `E32Device` class' config
        e32.update_config()
        e32.wait_aux()
        
        # Going back to the appropriate mode
        e32.mode = ebyte_e32.Modes.MODE_NORMAL
        e32.wait_aux()
        
        # Retrying to change channels and send the message.
        time.sleep(1)
        continue
    
    e32.send(b'Hello World !')
    e32.wait_aux()
    
    time.sleep(2.5)
    
    channel = channel + 1
    if channel > ebyte_e32.CHANNEL_MAX:
        channel = ebyte_e32.CHANNEL_MIN
    
    time.sleep(2.5)
