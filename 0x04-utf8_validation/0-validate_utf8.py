#!/usr/bin/python3
"""This File Conatins Functions that validate whether a Digit is UTF-8 Valid"""


def validUTF8(data):
    # Helper function to get the number of bytes in a UTF-8 character based on the first byte.
    def get_num_bytes(byte):
        num_bytes = 0
        # Count the number of consecutive 1s from left to right until the first 0 is encountered.
        for i in range(7, -1, -1):
            if byte & (1 << i):
                num_bytes += 1
            else:
                break
        return num_bytes

    num_bytes_to_check = 0

    for byte in data:
        if num_bytes_to_check == 0:
            # Determine the number of bytes to check for the current character.
            num_bytes_to_check = get_num_bytes(byte)
            # Validate the number of bytes. UTF-8 characters can have 1 to 4 bytes.
            if num_bytes_to_check == 1 or num_bytes_to_check > 4:
                return False
            # Skip the iteration if the byte is a single ASCII character (num_bytes_to_check == 0).
            elif num_bytes_to_check == 0:
                continue
        else:
            # Check that the current byte matches the UTF-8 continuation byte pattern (10xxxxxx).
            if not (byte & 0b11000000 == 0b10000000):
                return False

        num_bytes_to_check -= 1

    # If num_bytes_to_check is not 0 at the end, the data set is incomplete or invalid.
    return num_bytes_to_check == 0
