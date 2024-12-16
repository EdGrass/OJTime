# OJ-TIme-Tool

## Features

This tool is used to fetch competition information from four commonly used OnlineJudge platforms:

- **Codeforces**
- **Atcoder**
- **Codechef**
- **Nowcoder**

## 功能

该工具用于读取四个本人常用的 OnlineJudge 平台的比赛信息，平台包括：
- **Codeforces**
- **Atcoder**
- **Codechef**
- **Nowcoder**

## Implementation

- **Codeforces**: Uses the `requests` library to send API requests and parses the returned JSON data.
  
- **Atcoder and Nowcoder**: Implements dynamic browser control with `selenium` and `webdriver_manager`.

- **Codechef**: Since the webpage source does not include competition information and its competitions are held regularly (every Wednesday), a brute-force approach is used to fetch the competition data (this feature will be improved in the future, really).

## 实现

- **Codeforces**：使用 `requests` 库向 API 发送请求，并解析返回的 JSON 数据。
  
- **Atcoder 和 Nowcoder**：利用动态浏览器控制技术 `selenium` 配合 `webdriver_manager` 实现。

- **Codechef**：由于网页源码中未包含比赛信息，且其比赛规律性较强（每周三举办），因此采用暴力打表的方式获取比赛数据（该功能会在未来进行完善，真的嘛）。

## Updates

> Due to the nearing end of my ACM career, my need for additional features is quite low, so updates might be infrequent. 

> Future updates may be adjusted at any time, and the exact timing and features will depend on the situation.

- To-do:
    - May add a user Rating query feature.
    - May add a daily competition query feature.
    - More updates to come...

## 更新

> 由于本人的acm生涯接近末期，对此其他功能的需求比较低，可能会咕

> 未来更新内容可能会随时调整，具体时间和功能将视情况而定。

- 留坑：
    - 可能会增加用户 Rating 查询功能。
    - 可能会增加按天查询比赛的功能。
    - ···

## Configuration (macOS)

1. Enter the following in the terminal:
```bash
sudo ln -s /path/to/your/project/OJTImeTool.py /usr/local/bin/OJT
```

2. Change the path of `OJTImeTool.py` to:
```bash
/path/to/your/file/OJTimeTool/bin/python
```

3. Enter the following in the terminal:
```bash
OJT
```

## 配置(macos)

1. 在终端输入
```bash
sudo ln -s /该项目文件位置/OJTImeTool.py /usr/local/bin/OJT
```

2. 将OJTImeTool.py的路径改为
```bash
/该文件/OJTimeTool/bin/python
```

3. 终端输入
```bash
OJT
```