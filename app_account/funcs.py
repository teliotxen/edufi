import datetime


def school_year_cal(date1):
    str_year = str(date1).split('-')
    year = int(str_year[0])
    str_now = str(datetime.datetime.now()).split('-')
    now_year = int(str_now[0])
    calc = now_year - year + 1
    if calc <= 8:
        school = '미취학'
        grade = calc
    elif calc <= 13:
        school = '초등'
        grade = calc - 8 + 1
    elif calc <= 16:
        school = '중등'
        grade = calc - 13 + 1
    elif calc <= 19:
        school = '고등'
        grade = calc - 16 + 1
    else:
        school = '일반'
        grade = '사용'
    if calc <=8:
        text = f'{school} {grade}세'
    elif calc <=13:
        text = f'{school} {grade}학년'
    else:
        text = f'{school}'

    return text