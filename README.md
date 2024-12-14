# OJ-Time-Cmd

## Purpose:

This script is designed to retrieve competition schedules from four commonly used OJ platforms: Codeforces, Atcoder, Codechef, and Nowcoder.

## Implementation:

- **Codeforces**: Uses the `requests` library to send API requests and parses the returned JSON data.

- **Atcoder and Nowcoder**: Employ dynamic browser control technologies with `selenium` and `webdriver_manager`.

- **Codechef**: The webpage source code does not include competition information (the webpage seems quite advanced). However, since Codechef contests are consistently held on Wednesdays with a predictable schedule, a brute-force approach with hard-coded data is used. (This will be improved in the future.)

## Update:

Nov 14 22:10 Standardize output format and adjust colors