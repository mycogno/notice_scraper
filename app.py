from flask import Flask, render_template, request

app = Flask(__name__)

import crawling

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods = ['POST', 'GET'])
def search():
    list = crawling.event()[0] + crawling.haksa()[0] + crawling.iphak()[0] + crawling.recruit()[0] + crawling.research()[0] + crawling.scholarship()[0] + crawling.seminar()[0] + crawling.volunteer()[0]
    href_list = crawling.event()[1] + crawling.haksa()[1] + crawling.iphak()[1] + crawling.recruit()[1] + crawling.research()[1] + crawling.scholarship()[1] + crawling.seminar()[1] + crawling.volunteer()[1]
    result_list = []
    result_href_list = []
    if request.method == 'POST':
        result = request.form

    for i in range(len(list)):
        if list[i].find(result['search']) != -1:
            result_list.append(list[i])
            result_href_list.append(href_list[i])

    return render_template("search.html", search=result_list, href=result_href_list, leng=len(result_list))

@app.route('/check', methods = ['POST', 'GET'])
def check():
    list = crawling.haksa()[0]
    href_list = crawling.haksa()[1]
    result_list = []
    result_href_list = []
    if request.method == 'POST':
        value = request.form.getlist('check')
        for i in value:
            result_list.append(list[int(i)])
            result_href_list.append(href_list[int(i)])

    # from openpyxl import Workbook
    # wrtie_wb = Workbook()
    # wrtie_ws = wrtie_wb.active
    #
    # for i in range(len(result_list)):
    #     wrtie_ws.cell(i + 1, 1, result_list[i])
    #     wrtie_ws.cell(i + 1, 2, result_href_list[i])
    # wrtie_wb.save("check.xlsx")

    return render_template("check.html", check_list=result_list, href=result_href_list, leng=len(result_list))


@app.route('/event')
def event():
    event_list, href_list = crawling.event()
    return render_template("event.html", event_data = event_list, data_href = href_list, leng = len(event_list))

@app.route('/haksa')
def haksa():
    haksa_list, href_list = crawling.haksa()
    return render_template("haksa.html", haksa_data = haksa_list, data_href = href_list, leng = len(haksa_list))

@app.route('/iphak')
def iphak():
    iphak_list, href_list = crawling.iphak()
    return render_template("iphak.html", iphak_data = iphak_list, data_href = href_list, leng = len(iphak_list))

@app.route('/recruit')
def recruit():
    recruit_list, href_list = crawling.recruit()
    return render_template("recruit.html", recruit_data = recruit_list, data_href = href_list, leng = len(recruit_list))

@app.route('/research')
def research():
    research_list, href_list = crawling.research()
    return render_template("research.html", research_data = research_list, data_href = href_list, leng = len(research_list))

@app.route('/scholarship')
def scholarship():
    scholarship_list, href_list = crawling.scholarship()
    return render_template("scholarship.html", scholarship_data = scholarship_list, data_href = href_list, leng = len(scholarship_list))

@app.route('/seminar')
def seminar():
    seminar_list, href_list = crawling.seminar()
    return render_template("seminar.html", seminar_data = seminar_list, data_href = href_list, leng = len(seminar_list))

@app.route('/volunteer')
def volunteer():
    volunteer_list, href_list = crawling.volunteer()
    return render_template("volunteer.html", volunteer_data = volunteer_list, data_href = href_list, leng = len(volunteer_list))

if __name__ == '__main__':
    app.run()