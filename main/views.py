from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

grade_db = [
  {
    "_id": "4d705c94-f876-4c74-C64a-f008462499ca",
    "index": "1",
    "teacher": "권지연",
    "phone": "010-8338-4972",
    "grade": "3",
    "num": "13",
    "contents": "이상을 정당의 계집애들의 동산에는 공포한 대통령후보자가 따뜻한 하늘에는. 굳세게 차"
  },
  {
    "_id": "8fdb4b7e-41be-43fa-A42c-e05c3350e4a9",
    "index": "2",
    "teacher": "리현진",
    "phone": "010-2034-8391",
    "grade": "3",
    "num": "5",
    "contents": "아니한 위하여서 가슴속에 사람들의 중립성은 의장이 보호를 효력을. 국무회의는 무엇인지"
  },
  {
    "_id": "3b8f8242-4531-4858-C90b-014e0def420a",
    "index": "3",
    "teacher": "예준민",
    "phone": "010-9550-1072",
    "grade": "2",
    "num": "2",
    "contents": "릴케 정하는 멀듯이 행위로 공무원인 4년으로 보이는 60일. 인정할 붙일"
  },
  {
    "_id": "78421467-52ca-4779-B6c8-c7466ad3979d",
    "index": "4",
    "teacher": "오별",
    "phone": "010-3083-2417",
    "grade": "2",
    "num": "7",
    "contents": "계절이 사항은 가슴에 밥을 후가 별을 설립은 무엇이. 간에 고문을"
  },
  {
    "_id": "ad71511f-43de-48de-Aa86-d88b2fcd5872",
    "index": "5",
    "teacher": "성시윤",
    "phone": "010-7988-9963",
    "grade": "3",
    "num": "4",
    "contents": "관리 예산에 제고와 별에도 끓는 기관은 산야에 정한. 무엇을 인력의"
  }
]

def index(request):
    return render(request, 'main/index.html')

def jejuohyun(request):
    return render(request, 'main/jejuohyun.html')

def grade(request):
    return render(request, 'main/grade.html')

def my_page(request):
    return render(request, 'main/my_page.html')