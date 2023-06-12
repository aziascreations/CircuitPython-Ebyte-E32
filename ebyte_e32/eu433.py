# SPDX-FileCopyrightText: Copyright (c) 2023 Herwin Bozet
#
# SPDX-License-Identifier: MIT
"""
`ebyte_e32.eu433`
====================================================
* Author(s): Herwin Bozet
"""

FREQUENCY_MINIMUM = 410.0
"""Minimum LoRa EU443 frequency in MHz corresponding to channel `0`."""

FREQUENCY_MAXIMUM = 441.0
"""Maximum LoRa EU443 frequency in MHz corresponding to channel `31`."""


def channel_to_frequency(channel: int, strict: bool = True) -> float:
    """
    Converts a given EU443 channel into its corresponding MHz frequency.
    
    :param channel: The channel number.  (Between `0` and `31`)
    :param strict: Whether a `ValueError` exception should be raised if an invalid value is given (Default: ``True``)
    :return: The corresponding frequency in MHz.
    """
    if strict and channel not in range(0, 32):
        raise ValueError(f"The channel number should be between 0 and 31 !  (Got {channel})")
    
    return round(410 + 1 * channel)


def frequency_to_channel(frequency: float, strict: bool = True) -> float:
    """
    Converts a given MHz frequency into its corresponding EU443 channel number.
    
    :param frequency: The frequency in MHz.  (Between `409.5` and `441.5`)
    :param strict: Whether a `ValueError` exception should be raised if an invalid value is given (Default: ``True``)
    :return: The closest corresponding channel number.
    """
    if strict and not 409.5 <= frequency <= 441.5:
        raise ValueError(f"The frequency should be between 409.5 and 441.5 !  (Got {frequency})")
    
    return max(0, min(31, round(frequency - 410)))
