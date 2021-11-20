import requests
from bs4 import BeautifulSoup

# event, haksa, iphak, recruit, research, scholarship, seminar, volunteer
# 7, 1, 2, 3, 6, 8, 9, 4


class Scraper:
    def __init__(self, page_num, category):
        num_to_category = {
            "haksa": 1,
            "iphak": 2,
            "recruit": 3,
            "volunteer": 4,
            "research": 6,
            "event": 7,
            "scholarship": 8,
            "seminar": 9,
        }
        self.page_num = page_num
        BASE_URL = "https://www.hanyang.ac.kr/web/www/notice_all?p_p_id=viewNotice_WAR_noticeportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_viewNotice_WAR_noticeportlet_sCategoryId="
        self.url = (
            BASE_URL
            + str(num_to_category[category])
            + "&_viewNotice_WAR_noticeportlet_sCurPage="
        )

    def get_data(self):
        text_list = []
        href_list = []
        for page in range(1, self.page_num + 1):
            req = requests.get(
                self.url + str(page) + "&_viewNotice_WAR_noticeportlet_action=view"
            )
            soup = BeautifulSoup(req.text, "html.parser")

            for doc in soup.select(
                "#notice01 > div > table > tbody > tr > td > div > div > p > a"
            ):
                href = (
                    self.url
                    + str(page)
                    + "&_viewNotice_WAR_noticeportlet_sUserId=0&_viewNotice_WAR_noticeportlet_action=view_message&_viewNotice_WAR_noticeportlet_messageId="
                    + doc["href"].split("view_message")[1][1:-2]
                )
                text_list.append(doc.text)
                href_list.append(href)
        print(href_list)
        return text_list, href_list
