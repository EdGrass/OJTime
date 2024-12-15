# OJ-Time-Cmd

## Features

This tool is used to fetch competition information from four commonly used OnlineJudge platforms:

- **Codeforces**
- **Atcoder**
- **Codechef**
- **Nowcoder**

## Implementation

- **Codeforces**: Uses the `requests` library to send API requests and parses the returned JSON data.
  
- **Atcoder and Nowcoder**: Implements dynamic browser control with `selenium` and `webdriver_manager`.

- **Codechef**: Since the webpage source does not include competition information and its competitions are held regularly (every Wednesday), a brute-force approach is used to fetch the competition data (this feature will be improved in the future, really).

## Updates

> Due to the nearing end of my ACM career, my need for additional features is quite low, so updates might be infrequent. 

> Future updates may be adjusted at any time, and the exact timing and features will depend on the situation.

- To-do:
    - May add a user Rating query feature.
    - May add a daily competition query feature.
    - More updates to come...
