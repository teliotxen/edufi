from django.http import HttpResponseRedirect, JsonResponse
from django.http import Http404
from django.shortcuts import render
from .forms import UploadFileForm, DataTable
from .models import Quiz, uploadFileModel
from .tests import bulk_input
from django.core import serializers
from django.contrib.auth.decorators import login_required
# Create your views here.


# @login_required
def game_view(request):

    if request.GET:
        temp = '3'
        json_data = Quiz.objects.filter(level=temp)

        if request.GET:
            json_object = serializers.serialize("json", json_data)
            return JsonResponse(json_object, safe=False)

    return render(request, 'english/game_view.html')



def data_upload(request):
    try:
        datum = uploadFileModel.objects.values().last()
        bulk_input(datum['file'])
        return render(request, 'english/upload.html', context={'form':""})

    except:
        raise Http404("Question does not exist")



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            strings = str(request.FILES['file'])
            string_list = strings.split('.')
            console = string_list[-1]
            if 'csv' == console:
                form.save()
                return HttpResponseRedirect('/upload/')
            else:
                return render(request, 'english/uploader.html', context={'error':'csv 파일을 넣으세요','form': form})

    else:
        form = UploadFileForm()

    return render(request, 'english/uploader.html', {'form': form})

