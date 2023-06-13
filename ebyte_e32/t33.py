# SPDX-FileCopyrightText: Copyright (c) 2023 Herwin Bozet
#
# SPDX-License-Identifier: MIT
"""
`ebyte_e32.t33`
====================================================
* Author(s): Herwin Bozet
"""


class TransmitPower:
    """
    Available transmission power values for E32 modules with the T33 suffix.
    """
    
    TX_POWER_33DBM = 0b00
    "~2W / ~2000mW"
    
    TX_POWER_30DBM = 0b01
    "1W / 1000mW"
    
    TX_POWER_27DBM = 0b10
    "~500 mW"
    
    TX_POWER_24DBM = 0b11
    "~250 mW"
    
    TX_POWER_DEFAULT = TX_POWER_33DBM
    "Default TX power for modules with the T33 suffix"
