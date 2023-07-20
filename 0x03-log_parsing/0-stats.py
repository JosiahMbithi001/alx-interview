import sys

def print_stats(total_size, status_counts):
    print("Total file size:", total_size)
    sorted_statuses = sorted(status_counts.keys())
    for status in sorted_statuses:
        count = status_counts[status]
        print("{}: {}".format(status, count))

def main():
    total_size = 0
    status_counts = {}

    try:
        line_counter = 0
        for line in sys.stdin:
            line_counter += 1

            # Split the line by space and validate the format
            parts = line.split()
            if len(parts) != 10 or parts[2] != "GET" or parts[4] != "HTTP/1.1":
                continue

            try:
                status_code = int(parts[7])
                file_size = int(parts[8])
            except (ValueError, IndexError):
                continue

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_counter % 10 == 0:
                print_stats(total_size, status_counts)
                print("\n")

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
