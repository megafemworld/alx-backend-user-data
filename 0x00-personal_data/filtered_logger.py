#!/usr/bin/env python3
""" MOdule for personal data redaction
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """Filter_datum the message by replacing"""
    for f in fields:
        message = re.sub(
            f'{f}=.*?{seperator}', f'{f}={redaction}{seperator}', message)
    return message
