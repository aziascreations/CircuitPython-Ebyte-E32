# SPDX-FileCopyrightText: Copyright (c) 2023 Herwin Bozet
#
# SPDX-License-Identifier: MIT
"""
`ebyte_e32.exceptions`
====================================================
* Author(s): Herwin Bozet
"""


class E32GenericError(Exception):
    """
    Exception raised when the E32 module didn't respond properly, or at all, to messages sent by the driver.
    """
