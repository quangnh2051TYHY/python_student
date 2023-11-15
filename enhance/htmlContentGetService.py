import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from model import Student as student

def getStudentHtml():
    host_url = 'http://127.0.0.1:5000/'
    try:
        html = urllib.request.urlopen(host_url).read()
    except Exception as e:
        print(f"Error opening URL: {e}")
        return []
    soup = BeautifulSoup(html, 'html.parser')

    tr_tags = soup.select('tr')[1:]
    studentList = []

    for tr in tr_tags:
        td_tags = tr.select('td')[:7]
        if td_tags:
            stu = student.Student(*[td.text for td in td_tags])
            studentList.append(stu)

    return studentList
