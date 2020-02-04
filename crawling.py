import requests
from bs4 import BeautifulSoup

def event():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get("https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=7&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')


        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=7&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list

def haksa():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get("https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=1&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')


        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=1&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list

def iphak():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get(
            "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=2&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')

        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=2&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list

def recruit():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get(
            "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=3&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')

        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=3&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list

def research():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get(
            "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=6&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')

        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=6&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list

def scholarship():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get(
            "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=8&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')

        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=8&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list

def seminar():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get(
            "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=9&_viewNotice_WAR_noticeportlet_sCurPage" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')

        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=9&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list

def volunteer():
    list = []
    href_list = []
    for i in range(1, 6):
        req = requests.get(
            "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId=4&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_action=view")
        soup = BeautifulSoup(req.text, 'html.parser')

        for j in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"):
            href = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sKeyType=title&_viewNotice_WAR_noticeportlet_sCategoryId=4&_viewNotice_WAR_noticeportlet_sCurPage=" + str(i) + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId=" + j["href"].split("view_message")[1][1:-2]
            list.append(j.text)
            href_list.append(href)
    return list, href_list