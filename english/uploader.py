import os
from edufi.settings import BASE_DIR
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edufi.settings")
# # django file upload

import django
django.setup()
from english.models import Quiz
import csv

# print(os.path.join(BASE_DIR, 'media'))

def bulk_input(value):

    url = os.path.join(BASE_DIR, 'media')
    hand = open(url + '/' + value)
    print(hand)
    reader = csv.reader(hand)
    # csv 파일을 읽고 변수에 저장합니다.



    # 아직은 객체 상태입니다.
    bulk_list = []
    for row in reader:
        bulk_list.append(
            Quiz(
                level=row[0],
                word1=row[1],
                word1_switch=row[2],
                word1_korean=row[3],
                word2=row[4],
                word2_switch=row[5],
                word2_korean=row[6],
                word3=row[7],
                word3_switch=row[8],
                word3_korean=row[9],
                english=row[10],
                korean=row[11],
            )
        )
    return bulk_list


