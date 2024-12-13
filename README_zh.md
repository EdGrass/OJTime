# OJ-TIme-Cmd

## 用途：
用来负责读取四个本人常用的OJ平台比赛：Codeforces,Atcoder,Codechef,Nowcoder

## 实现方式：

Codeforces采用api直接读取，Atcoder和Nowcoder使用BeautifulSoup爬取了相应的比赛，Codechef由于网页源码并没有比赛信息，但是好在每次它的比赛都是周三且十分规律，我们直接暴力打表。

## 主要技巧：

Python