from django.http import HttpResponseRedirect, JsonResponse
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import UploadFileForm, DataTable
from .models import Quiz, uploadFileModel
from .uploader import bulk_input
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
# Create your views here.


# @login_required
def game_view(request):

    sample_list = [1, 3, 5, 7, 9]  # 이 친구를 어떻게 배열할 것인가 그것이 문제가 됨
    json_data = Quiz.objects.filter(id__in=sample_list)

    answer_sheet = []
    for datum in json_data:
        matter = [datum.id,datum.english, datum.korean, datum.word1, datum.word2, datum.word3]
        answer_sheet.append(matter)

    print(answer_sheet)


    #AJAX GET - get type을 확인해서 적절한 내용을 GET 하게 할 수 있다.
    if request.GET:
        json_object = serializers.serialize("json", json_data)
        return JsonResponse(json_object, safe=False)

    #AJAX POST
    if request.POST:
        print(type(request.body))
        print(json.loads(request.body))

    return render(request, 'english/game_view.html')



def data_upload(request):
    datum = uploadFileModel.objects.values().last()
    print(bulk_input(datum['file']))
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
    print(1)
    return render(request, 'english/uploader.html', {'form': form})

