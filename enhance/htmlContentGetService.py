from bs4 import BeautifulSoup
from model import Student as student
import requests


def getStudentHtml():
    host_url = 'https://mse.69mholdings.com/'
    try:
        response = requests.get(host_url)
        response.raise_for_status()
        html = response.text
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
