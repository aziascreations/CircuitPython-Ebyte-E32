# SPDX-FileCopyrightText: Copyright (c) 2023 Herwin Bozet
#
# SPDX-License-Identifier: MIT
"""
`ebyte_e32.t20`
====================================================
* Author(s): Herwin Bozet
"""


class TransmitPower:
    """
    Available transmission power values for E32 modules with the T20 suffix.
    """
    
    TX_POWER_20DBM = 0b00
    "100mW"
    
    TX_POWER_17DBM = 0b01
    "~50 mW"
    
    TX_POWER_14DBM = 0b10
    "~25 mW"
    
    TX_POWER_10DBM = 0b11
    "10 mW"
    
    TX_POWER_DEFAULT = TX_POWER_20DBM
    "Default TX power for T20 modules"
