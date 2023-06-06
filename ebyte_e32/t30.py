"""
`ebyte_e32.t30`
====================================================
* Author(s): Herwin Bozet
"""


class TransmitPower:
    """
    Available transmission power values for E32 modules with the T30 suffix.
    """
    
    TX_POWER_30DBM = 0b00
    "1W / 1000mW"
    
    TX_POWER_27DBM = 0b01
    "~500 mW"
    
    TX_POWER_24DBM = 0b10
    "~250 mW"
    
    TX_POWER_21DBM = 0b11
    "~125 mW"
    
    TX_POWER_DEFAULT = TX_POWER_30DBM
    "Default TX power for T30 modules"
