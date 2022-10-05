from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from counter.utils import show_wordcloud
from counter.models import WordFreq
from djangoSayac.settings import BASE_DIR

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data= counter(uploaded_file_url)
        new_file = WordFreq(name=filename,top_items=data)
        new_file.save()
        return render(request, 'upload.html', {'data': data})
    return render(request, 'upload.html')


def counter(link):
    with open(f"{BASE_DIR}{link}", 'r') as destination:
        text = destination.read()
        data = show_wordcloud(text)
        return data