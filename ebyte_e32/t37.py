# SPDX-FileCopyrightText: Copyright (c) 2023 Herwin Bozet
#
# SPDX-License-Identifier: MIT
"""
`ebyte_e32.t37`
====================================================
* Author(s): Herwin Bozet
"""


class TransmitPower:
    """
    Available transmission power values for E32 modules with the T37 suffix.
    """
    
    TX_POWER_37DBM = 0b00
    "~5W / ~5000mW"
    
    TX_POWER_DEFAULT = TX_POWER_37DBM
    "Default TX power for modules with the T37 suffix"
