#!/usr/bin/python3
"""_summary_
    """


def validUTF8(data):
    """_summary_

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    remaining_bytes = 0

    for num in data:
        # Check if the current integer starts a valid UTF-8 character sequence
        if remaining_bytes == 0:
            if (num >> 7) == 0b0:
                remaining_bytes = 0
            elif (num >> 5) == 0b110:
                remaining_bytes = 1
            elif (num >> 4) == 0b1110:
                remaining_bytes = 2
            elif (num >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            # Check if the current integer starts with the pattern '10'
            if (num >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # If all bytes are correctly processed, there should be no remaining bytes
    return remaining_bytes == 0
