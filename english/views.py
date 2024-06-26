from django.http import HttpResponseRedirect, JsonResponse
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import UploadFileForm, DataTable
from .models import Quiz, uploadFileModel, UserAnswer
from app_account.models import Router,User
from .uploader import bulk_input
from django.core import serializers
import json
import time
import datetime

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def game_result(request):
    # try:
    user_info = User.objects.get(id=request.user.id)
    router_info = Router.objects.get(router_id=user_info.router)
    last_sheet = UserAnswer.objects.latest('dt_created')

    if not last_sheet.check_the_result:
        # last_sheet.check_the_result = True
        # last_sheet.save()
        user_get_time = int(user_info.get_time)
        router_get_time = int(router_info.get_time)
        router_max_time = int(router_info.max_time)
        if int(last_sheet.score) >= 60:
            total_get_time = user_get_time + router_get_time
            if total_get_time >= router_max_time:
                total_get_time = router_max_time

            user_info.get_time = total_get_time
            user_info.save()
            result_message = True
        else:
            total_get_time = user_get_time
            result_message = False
    else:
        raise Http404("이미 반영된 학습결과 입니다. ")

    # except:
    #     raise Http404("잘못된 접근입니다. ")

    context = {
        'user_get_time':user_get_time,
        'router_get_time': router_get_time,
        'total_get_time' : total_get_time,
        'result_message' : result_message,
        'currunt_sheet' : last_sheet
    }
    return render(request, 'english/game_result.html', context)

@login_required
def game_view(request):

    sample_list = [1, 3, 5, 7, 9]  # 이 친구를 어떻게 배열할 것인가 그것이 문제가 됨
    json_data = Quiz.objects.filter(id__in=sample_list)

    answer_sheet = []
    for datum in json_data:
        matter = {
            'id': datum.id,
            'level': datum.level,
            'english': datum.english,
            'korean': datum.korean,
            'word1': datum.word1,
            'word2': datum.word2,
            'word3': datum.word3
        }
        answer_sheet.append(matter)

    if request.GET:
        json_object = serializers.serialize("json", json_data)
        return JsonResponse(json_object, safe=False)

    #AJAX POST
    if request.POST:
        get_data = json.loads(request.body)['result']

        #test_score
        test_score = int(get_data.count('true')/len(get_data)*100)
        print(test_score)
        #user answer
        answer_sheet_list = list()
        for num in range(0,len(get_data)):
            user_answer = get_data[num]
            if user_answer == 'True':
                answer_sheet_list.append(answer_sheet[num]['english'])
            else:
                merged_sentence = ''
                for inside_num in range(0,len(user_answer)):
                    merged_sentence += user_answer[inside_num]
                    if inside_num < len(user_answer) - 2:
                        merged_sentence += ' '
                answer_sheet_list.append(merged_sentence)

        #vocabulary
        word_list = list()
        for item in answer_sheet:
            part_word_list = list()
            for i in range(1,4):
                index = 'word'+ str(i)
                print(item[index])
                if item[index] != '':
                    part_word_list.append(item[index])
            word_list.append(part_word_list)

        UserAnswer.objects.create(
            user=request.user,
            level=answer_sheet[0]['level'], #레밸 내용 수정하기
            score = test_score,
            sentence1=answer_sheet[0]['english'],
            korean1=answer_sheet[0]['korean'],
            answer1=answer_sheet_list[0],
            sentence2=answer_sheet[1]['english'],
            korean2=answer_sheet[1]['korean'],
            answer2=answer_sheet_list[1],
            sentence3=answer_sheet[2]['english'],
            korean3=answer_sheet[2]['korean'],
            answer3=answer_sheet_list[2],
            sentence4=answer_sheet[3]['english'],
            korean4=answer_sheet[3]['korean'],
            answer4=answer_sheet_list[3],
            sentence5=answer_sheet[4]['english'],
            korean5=answer_sheet[4]['korean'],
            answer5=answer_sheet_list[4],
            voca1=word_list[0],
            voca2=word_list[1],
            voca3=word_list[2],
            voca4 = word_list[3],
            voca5 = word_list[4],
        )
    return render(request, 'english/game_view.html')



def data_upload(request):
    datum = uploadFileModel.objects.values().last()
    context = bulk_input(datum['file'])

    if request.POST:
        try:
            Quiz.objects.bulk_create(bulk_input(datum['file']))
            return render(request, 'english/upload.html', context={'form':""})

        except:
            raise Http404("Question does not exist")

    return render(request, 'english/upload.html', context={'data': context})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            strings = str(request.FILES['file'])
            string_list = strings.split('.')
            console = string_list[-1]
            if 'csv' == console:
                form.save()
                return render(request, 'english/upload.html')
            else:
                return render(request, 'english/uploader.html', context={'error':'csv 파일을 넣으세요','form': form})

    else:
        form = UploadFileForm()
    return render(request, 'english/uploader.html', {'form': form})

