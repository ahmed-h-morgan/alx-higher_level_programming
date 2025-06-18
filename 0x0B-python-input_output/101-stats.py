#!/usr/bin/python3
"""
14. Log parsing
"""
import sys


def print_stats(total_size, status_counts):
    """Print the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    """
    the main function
    """
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                # File size is the last part
                total_size += int(parts[-1])
                # Status code is second to last part
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                # Skip lines that don't match expected format
                continue

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise



if __name__ == "__main__":
    main()
