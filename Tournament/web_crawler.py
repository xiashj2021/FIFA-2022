import pyautogui
import time
import re
from selenium.webdriver import Edge

web = Edge()
url = 'https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/qatar2022/scores-fixtures?country=CN&wtw-filter=ALL'
web.get(url)
pyautogui.moveTo(937, 1020, duration=3)
time.sleep(4)
pyautogui.click()
text = web.page_source
date = re.findall(
    r'<div class="matches-container_title__1uTPf">(.*?)</div>', text)
race_time = re.findall(
    r'<div class="match-block_wtwStadiumName__2EACw">(.*?)</div>', text)
race_type = re.findall(
    r'<div class="match-block_wtwStadiumName__2EACw ff-mb-0">(.*?)</div>', text)
team_name = re.findall(
    r'<div class="wtw-teams-horizontally-component_TeamName__2lZ2s ff-mb-0 ff-ml-4">(.*?)</div>', text)
score_first = re.findall(
    r'<div class="wtw-teams-horizontally-component_score1__3HTmk">(.*?)</div>', text)
score_second = re.findall(
    r'<div class="wtw-teams-horizontally-component_score2__20sPm">(.*?)</div>', text)
status = re.findall(
    r'<div class="wtw-match-status_indicator__3cO5Z wtw-match-status_fullTime__1ONKu">(.*?)</div>', text)
penalties_score_first = re.findall(
    r'<div class="wtw-teams-horizontally-component_penaltiesColumn1__tC-Ud">(.*?)</div>', text)
penalties_score_second = re.findall(
    r'<div class="wtw-teams-horizontally-component_penaltiesColumn2__sVcHw">(.*?)</div>', text)
event = re.findall(
    r'<p class="ff-m-0">(.*?)</p>', text)
web.close()

team_list = []
for i in range(len(team_name)):
    if i % 2 == 0:
        team_list.append(team_name[i] + ' vs ' + team_name[i + 1])

score_data = []
for i in range(len(score_first)):
    score_data.append(score_first[i] + ' · ' + score_second[i])

penalties_data = []
for i in range(len(penalties_score_first)):
    penalties_data.append(penalties_score_first[i] + ' · ' + penalties_score_second[i])

date_list = []
m = 0
j = 3
k = 2
for i in range(len(race_time)):
    if i in (0, 1):
        date_list.append(date[m])
    elif i in (46, 47, 48):
        k += 1
        if k % 3 == 0:
            m += 1
            date_list.append(date[m])
        else:
            date_list.append(date[m])
    elif i in (49, 50, 51, 52, 53, 54, 57, 58):
        if (i+1) % 2 == 0:
            m += 1
            date_list.append(date[m])
        else:
            date_list.append(date[m])
    elif i in (55, 56, 59, 60, 61, 62, 63):
        m += 1
        date_list.append(date[m])
    else:
        j += 1
        if j % 4 == 0:
            m += 1
            date_list.append(date[m])
        else:
            date_list.append(date[m])

score_list = []
event_list = []
n = 0
for i in range(len(race_type)):
    if (race_type[i] == 'Round of 16' or race_type[i] == 'Quarter-final' or race_type[i] == 'Final') and (score_data[i][0] == score_data[i][-1]):
        score_list.append(score_data[i]+' '+penalties_data[n])
        event_list.append(event[n].replace(' &nbsp;', ' '))
        n += 1
    else:
        score_list.append(score_data[i])
        event_list.append('')

data = []
for i in range(len(team_list)):
    data.append((team_list[i], race_type[i], score_list[i], date_list[i], race_time[i], event_list[i], status[i]))

print(data)
