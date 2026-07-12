# IP Reputation Checker

A lightweight Python command-line utility that validates an IP address, classifies it as **Public** or **Private**, identifies its version (**IPv4**/**IPv6**), and generates a formatted reputation report — both on screen and as a saved text file.

## Overview

This tool was developed as part of a Cybersecurity & Compliance internship project. It demonstrates a foundational building block used in larger security workflows: identifying whether a given IP address originates from a private (internal/LAN) range or a public (internet-facing) range, which is a common first step in log triage, firewall rule review, and incident investigation.

## Features

- Validates user-supplied IP addresses using Python's built-in `ipaddress` module
- Supports both **IPv4** and **IPv6** addresses
- Classifies each address as **Public** or **Private**
- Displays a clean, formatted report in the console
- Automatically saves the report to `report.txt`
- Gracefully handles invalid input with a clear error message

## Requirements

- Python 3.6 or later
- No third-party dependencies (uses only the Python standard library)

## Installation

No installation is required beyond having Python 3 available.

```bash
git clone <repository-url>
cd ip-reputation-checker
```

## Usage

Run the script and enter an IP address when prompted:

```bash
python ip_checker.py
```

**Example session:**

```
Enter IP Address: 8.8.8.8

IP Reputation Report
--------------------
IP Address : 8.8.8.8
Type       : Public
Version    : IPv4

Report generated successfully: report.txt
```

The same report is written to `report.txt` in the working directory.

## How It Works

1. The script prompts the user to enter an IP address.
2. `ipaddress.ip_address()` parses and validates the input. Invalid input raises a `ValueError`, which is caught and reported to the user.
3. The `is_private` attribute of the parsed address object determines whether the IP is classified as **Private** or **Public**.
4. The `version` attribute identifies whether the address is **IPv4** or **IPv6**.
5. A formatted report string is built, printed to the console, and written to `report.txt`.

## Project Structure

```
ip-reputation-checker/
├── ip_checker.py     # Main script
├── report.txt        # Generated after each run (sample included)
└── README.md         # Project documentation
```

## Limitations

- Classification is based solely on standard public/private IP range logic (RFC 1918 / RFC 4193, etc.); it does not query any external threat-intelligence or reputation database.
- Each run overwrites `report.txt` with the result of the latest lookup only.
- Processes one IP address per execution.

## Possible Future Enhancements

- Integration with threat-intelligence APIs (e.g., AbuseIPDB, VirusTotal) for true reputation scoring
- Batch processing of multiple IP addresses from a file
- Geolocation and ASN/ISP lookup
- Logging with timestamps and appending to a historical report instead of overwriting

## Author

**Sharvi Kamerkar**
Intern ID: 2106
RedKross Research Foundation

## License

Internal academic/internship project — for educational and demonstration purposes.
