#!/usr/bin/env python3
""" MOdule for personal data redaction
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """Filter_datum the message by replacing
    the fields with the redaction
    Args:
        fields (List): List of fields to redact
        redaction (string): representing by what the
        field will be obfuscated
        message (string): a string representing the log line
        seperator (string): representing by which character
        is separating all fields in the log
    """
    for f in fields:
        message = re.sub(
            f'{f}=.*?{seperator}', f'{f}={redaction}{seperator}', message)
    return message
