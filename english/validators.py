from django.core.exceptions import ValidationError


# def validate_file_name(value):
#     strings = str(request.FILES['file'])
#     string_list = strings.split('.')
#     console = string_list[-1]
#     print(console)
#     if 'csv' == console:
#         print(13)
#         # form.save()
#         # print(request.FILES['file'])
#         return HttpResponseRedirect('/uploader/')