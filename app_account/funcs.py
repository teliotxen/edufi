import datetime


def school_year_cal(date1):
    str_year = str(date1).split('-')
    year = int(str_year[0])
    str_now = str(datetime.datetime.now()).split('-')
    now_year = int(str_now[0])
    calc = now_year - year + 1
    if calc <= 8:
        grade = 1
    elif calc <= 13:
        grade = calc - 8 + 1 - 2
    else:
        grade = 7

    return grade


def form_data_to_string(data):
    temp = str(data)
    temp = temp.split(' ')
    for item in temp:
        if 'value' in item:
            temp = item.split('=')
            string = ''
            for i in temp[1]:
                if i != '"':
                    string += i

            return string
