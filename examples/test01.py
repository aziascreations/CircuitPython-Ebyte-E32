import binascii
import board

import ebyte_e32

PIN_M0  = board.IO13
PIN_M1  = board.IO12
PIN_RXD = board.IO11
PIN_TXD = board.IO10
PIN_AUX = board.IO9

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, None, 0xBEEF)

binascii.hexlify(e32.get_raw_config(), '-')

e32.tx_power = 0b11

binascii.hexlify(e32.get_raw_config(), '-')
