#!/usr/bin/env python3
import re

# Define individual parts of the regex for each field in the log
regex_host = r'(?P<host>\S+)'              # IP address or hostname
regex_identity = r'(?P<identity>\S+)'      # Usually a dash (-)
regex_user = r'(?P<user>\S+)'              # Authenticated user or dash
regex_time = r'\[(?P<time>.*?)\]'        # Timestamp in square brackets
regex_request = r'"(?P<request>.*?)"'      # HTTP request string
regex_status = r'(?P<status>\d{3})'       # HTTP status code (3 digits)
regex_size = r'(?P<size>\S+)'             # Response size or dash
regex_referer = r'"(?P<referer>.*?)"'     # Referer URL
regex_agent = r'"(?P<agent>.*?)"'         # User agent string
regex_space = r'\s+'                      # One or more whitespace char


# Combine all the parts into a single regex pattern
pattern = (
    regex_host + regex_space +
    regex_identity + regex_space +
    regex_user + regex_space +
    regex_time + regex_space +
    regex_request + regex_space +
    regex_status + regex_space +
    regex_size + regex_space +
    regex_referer + regex_space +
    regex_agent
)

# Function to parse a log line
def Parser(log_line):
    """
    Parses a single Apache log line into a dictionary.

    Args:
        log_line (str): One line from the Apache log.

    Returns:
        dict: Parsed fields like host, time, request, etc.
              or None if parsing fails.
    """
    try:
        match = re.match(pattern, log_line)
        if match:
            return match.groupdict()
        else:
            return None
    except Exception as err:
        print("Error:", err)
        return None
