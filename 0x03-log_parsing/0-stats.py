import sys

# Define possible status codes
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables for metrics
total_size = 0
lines_by_status_code = {code: 0 for code in status_codes}

# Define function to print metrics


def print_metrics():
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(lines_by_status_code.keys()):
        if lines_by_status_code[code] > 0:
            print("{}: {}".format(code, lines_by_status_code[code]))


# Read from stdin line by line
line_count = 0
for line in sys.stdin:
    # Parse line using input format
    try:
        ip_address, date, request, status_code_str, size_str = line.split(" ")
        status_code = int(status_code_str)
        size = int(size_str)
    except ValueError:
        continue

    # Update metrics
    total_size += size
    if status_code in status_codes:
        lines_by_status_code[status_code] += 1

    line_count += 1
    # Print metrics after every 10 lines or upon keyboard interruption
    if line_count % 10 == 0:
        print_metrics()

# Print final metrics upon EOF
print_metrics()
