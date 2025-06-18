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
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                # Extract file size (last part)
                file_size = int(parts[-1])
                total_size += file_size

                # Extract status code (second to last part)
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

            except (IndexError, ValueError):
                # Skip lines that don't match the expected format
                continue

    except KeyboardInterrupt:
        # Handle CTRL+C
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
