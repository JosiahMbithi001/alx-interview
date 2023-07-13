#!/usr/bin/python3
"""This File Contains a Function min Operations"""


def minOperations(n):
    """This Function finds the minimum operations"""
    if n <= 1:
        return 0

    operations = 0
    paste_buffer = 1
    total_characters = 1

    while total_characters < n:
        if n % total_characters == 0:
            operations += 2  # Copy All and Paste
            paste_buffer = total_characters
            total_characters *= 2
        else:
            operations += 1  # Paste
            total_characters += paste_buffer

    return operations
