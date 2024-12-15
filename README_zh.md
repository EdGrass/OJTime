# OJ-TIme-Cmd

## 功能：

该工具用于读取四个本人常用的 OnlineJudge 平台的比赛信息，平台包括：
- **Codeforces**
- **Atcoder**
- **Codechef**
- **Nowcoder**

## 实现

- **Codeforces**：使用 `requests` 库向 API 发送请求，并解析返回的 JSON 数据。
  
- **Atcoder 和 Nowcoder**：利用动态浏览器控制技术 `selenium` 配合 `webdriver_manager` 实现。

- **Codechef**：由于网页源码中未包含比赛信息，且其比赛规律性较强（每周三举办），因此采用暴力打表的方式获取比赛数据（该功能会在未来进行完善，真的嘛）。

## 更新：

> 由于本人的acm生涯接近末期，对此其他功能的需求比较低，可能会咕

> 未来更新内容可能会随时调整，具体时间和功能将视情况而定。

- 留坑：
    - 可能会增加用户 Rating 查询功能。
    - 可能会增加按天查询比赛的功能。
    - ···
