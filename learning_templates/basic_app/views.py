from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'text':'hello world'}
    return render(request, 'basic_app/index.html',my_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/realtive_url_template.html')
