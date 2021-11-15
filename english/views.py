from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
# Create your views here.


def game_view(request):
    return render(request, 'english/game_view.html')


def data_upload(request):
    return render(request, 'english/uploader.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()

    print(form)
    return render(request, 'english/uploader.html', {'form': form})

