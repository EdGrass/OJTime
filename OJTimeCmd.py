#!/Users/edgrass/Documents/Vscode-cpp/OJ-Time-Cmd/OJTimeCmd/bin/python


import requests
import datetime
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re  # 引入正则表达式模块
from colorama import Fore, Style, init

# 初始化 colorama
init()
ORANGE = "\033[38;5;214m"

def get_codeforces_contests():
    print(f"{Fore.BLUE}CODEFORCES:{Style.RESET_ALL}")
    url = 'https://codeforces.com/api/contest.list'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch Codeforces contest data.")
        return
    contests = response.json()['result']
    upcoming_contests = [contest for contest in contests if contest['startTimeSeconds'] > datetime.now().timestamp()]
    if not upcoming_contests:
        print("No upcoming Codeforces contests.")
        return
    print(f"{Fore.BLUE}Upcoming Codeforces Contests:{Style.RESET_ALL}")
    print(f"")
    upcoming_contests.reverse()  # 确保按时间顺序排列
    for contest in upcoming_contests:
        start_time = datetime.fromtimestamp(contest['startTimeSeconds'])
        duration = str(timedelta(seconds=contest['durationSeconds']))
        print(f"{Fore.BLUE}Contest: {contest['name']}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Duration: {duration}{Style.RESET_ALL}")
        print("-" * 40)

def get_atcoder_contests():
    print(f"{Fore.GREEN}ATCODER:{Style.RESET_ALL}")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://atcoder.jp/contests")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.table-default")))
    contests = driver.find_elements(By.CSS_SELECTOR, "table.table-default tr")
    current_time = datetime.now()
    print(f"{Fore.GREEN}Upcoming Atcoder Contests:")
    print(f"")
    for contest in contests:
        columns = contest.find_elements(By.TAG_NAME, "td")
        if len(columns) >= 4:
            contest_time_str = columns[0].text.strip()
            contest_time_str = re.sub(r'\([A-Za-z]*\)', '', contest_time_str).strip()
            try:
                contest_time = datetime.strptime(contest_time_str, '%Y-%m-%d %H:%M')
            except ValueError:
                print(f"Atcoder比赛时间格式不匹配,跳过: {contest_time_str}")
                continue
            contest_name = columns[1].text.strip()
            contest_duration = columns[2].text.strip()
            contest_status = columns[3].text.strip()
            if current_time < contest_time:
                print(f"{Fore.GREEN}Contest: {contest_name[4:]}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Start Time: {contest_time}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Duration: {contest_duration}{Style.RESET_ALL}")
                print("-" * 40)
    driver.quit()

def codechef_generate_contests(start_contest_number, current_date, limit=5):
    contests = []
    contest_time = datetime.strptime("2024-12-11 22:30:00", "%Y-%m-%d %H:%M:%S")
    duration = "2 Hrs"
    count = 0
    while count < limit:
        if contest_time >= current_date:
            contest_name = f"Starters {start_contest_number}"
            contests.append({
                "name": contest_name,
                "start_time": contest_time.strftime("%Y-%m-%d %H:%M:%S"),
                "duration": duration
            })
            count += 1
        start_contest_number += 1
        contest_time += timedelta(days=7)
    return contests

def get_codechef_contests():
    print(f"{ORANGE}CODECHEF:")
    now = datetime.now()
    contests = codechef_generate_contests(164, now, limit=5)
    print(f"{ORANGE}Upcoming Codechef Contests:")
    print(f"")
    if contests:
        for contest in contests:
            name = contest["name"]
            start_time = contest["start_time"]
            duration = contest["duration"]
            print(f"{ORANGE}Contest: {name}")
            print(f"{ORANGE}Start Time: {start_time}")
            print(f"{ORANGE}Duration: {duration}")
            print("-" * 40)

def get_nowcoder_contests():
    print(f"{Fore.MAGENTA}NOWCODER:{Style.RESET_ALL}")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://ac.nowcoder.com/acm/contest/vip-index")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.platform-item-main"))
        )
    except Exception as e:
        print(f"页面加载失败: {e}")
        driver.quit()
        return
    contests = driver.find_elements(By.CSS_SELECTOR, "div.platform-item-main")
    current_time = datetime.now()
    print(f"{Fore.MAGENTA}Upcoming Nowcoder Contests:{Style.RESET_ALL}")
    print(f"")
    for contest in contests:
        try:
            contest_name = contest.find_element(By.CSS_SELECTOR, "h4 a").text.strip()
            match_time_text = contest.find_element(By.CSS_SELECTOR, "li.match-time-icon").text.strip()
            match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2})', match_time_text)
            if not match:
                print(f"比赛时间格式不匹配，跳过: {match_time_text}")
                continue
            start_time_str = match.group(1)
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            duration_match = re.search(r"时长:(\d+小时(?:\d+分钟)?)", match_time_text)
            duration = duration_match.group(1) if duration_match else "Unknown"
            if current_time < start_time:
                print(f"{Fore.MAGENTA}Contest: {contest_name}{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}Start Time: {start_time}{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}Duration: {duration}{Style.RESET_ALL}")
                print("-" * 40)
        except Exception as e:
            print(f"处理比赛数据时出错: {e}")
            continue
    driver.quit()

def get_all_contests():
    get_codeforces_contests()
    print(f"")
    get_atcoder_contests()
    print(f"")
    get_nowcoder_contests()
    print(f"")
    get_codechef_contests()

get_all_contests()
