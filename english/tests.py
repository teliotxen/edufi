from django.test import TestCase
from pathlib import Path

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
    reader = csv.reader(hand)
    # csv 파일을 읽고 변수에 저장합니다.

    # 아직은 객체 상태입니다.
    bulk_list = []
    for row in reader:
        bulk_list.append(Quiz(
            level=row[1],
            word1=row[2],
            word1_switch=row[3],
            word1_korean=row[4],
            word2=row[5],
            word2_switch=row[6],
            word2_korean=row[7],
            word3=row[8],
            word3_switch=row[9],
            word3_korean=row[10],
            english=row[11],
            korean=row[12]))

    print(bulk_list)
    Quiz.objects.bulk_create(bulk_list)
