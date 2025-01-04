#!/usr/bin/env python3
import re
"""_summary_
"""

def filter_datum(fields, redaction, message, seperator):
    """_summary_

    Args:
        fields (_type_): _description_
        redaction (_type_): _description_
        message (_type_): _description_
        seperator (_type_): _description_
    """
    for field in fields:
            re.sub(f'{field}=.*?{seperator}', redaction, message)               