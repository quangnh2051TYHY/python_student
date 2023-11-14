import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from model import Student as student


def getStudentHtml():
    host_url = 'http://127.0.0.1:5000/'
    html = urllib.request.urlopen(host_url).read()
    # Read all page
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('tr')
    removeHeaderTrList = tags[1: len(tags)]
    studentList = []
    for eachTr in removeHeaderTrList:
        # Find all td in each pair of <tr> tag
        soup = BeautifulSoup(str(eachTr), "html.parser")
        tdList = soup.find_all('td')
        if len(tdList) > 0:
            stu = student.Student(tdList[0].text, tdList[1].text, tdList[2].text,
                                  tdList[3].text, tdList[4].text, tdList[5].text, tdList[6].text)
            studentList.append(stu)

    return studentList
