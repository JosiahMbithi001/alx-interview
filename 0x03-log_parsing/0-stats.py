#!/usr/bin/python3
"""This File Solves Log Parsing """

import sys


def print_stats(total_size, status_counts):
    """ Print the total file size"""

    print("Total file size:", total_size)

    """ Sort the status codes in ascending order """
    sorted_statuses = sorted(status_counts.keys())

    """ Print the number of lines for each status code """
    for status in sorted_statuses:
        count = status_counts[status]
        print("{}: {}".format(status, count))


def main():
	"""Main Function that executes print_stats """
    total_size = 0
    status_counts = {}

    try:
        line_counter = 0
        for line in sys.stdin:
            line_counter += 1

            """ Split the line by space and validate the format"""
            parts = line.split()
            if len(parts) != 9 or parts[3] != "\"GET" or parts[5] != "HTTP/1.1\"":
                continue

            try:
                status_code = int(parts[7])
                file_size = int(parts[8])
            except (ValueError, IndexError):
                continue

            """ Accumulate the total file size """
            total_size += file_size

            """ Update the count for each status code """
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_counter % 10 == 0:
                """ Print statistics after every 10 lines """
                print_stats(total_size, status_counts)
                print()

    except KeyboardInterrupt:
        """ Print final statistics in case of keyboard interruption"""
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
