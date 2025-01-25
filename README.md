# OJ-TIme-Tool

## Features

This tool is used to fetch competition information from four commonly used OnlineJudge platforms:

- **Codeforces**
- **Atcoder**
- **Codechef**
- **Nowcoder**

## Implementation

- **Codeforces**: Uses the `requests` library to send API requests and parses the returned JSON data.
  
- **Atcoder and Nowcoder**: Implements dynamic browser control with `selenium` and `webdriver_manager`.

- **Codechef**: Since the webpage source does not include competition information and its competitions are held regularly (every Wednesday), a brute-force approach is used to fetch the competition data (this feature will be improved in the future, (really?)).

## Configuration (macOS)

1. In the terminal, enter:
```bash
sudo ln -s /path/to/project/file/OJTImeTool.py /usr/local/bin/OJT
```

2. Change the first line path of OJTImeTool.py to:
```bash
/path/to/file/OJTimeTool/bin/python
```

3. In the terminal, enter:
```bash
OJT
```