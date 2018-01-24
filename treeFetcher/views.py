from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UtteranceForm
from .conll_file_fetcher import get_conll_x_file
# Create your views here.
import time


def home(request):
    return render(request, 'index.html')


def submit_utterance(request):
    content = ""
    if request.method == 'GET':
        form = UtteranceForm
        empty = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/data/empty_file.txt'
        content = open(empty).read()
    else:
        form = UtteranceForm(request.POST)
        if form.is_valid():
            content = "failed"
            utterance = form.cleaned_data.get('utterance')
            annotation = form.cleaned_data.get('annotation')
            lattices_conll, output_conll, dep_output, content = get_conll_x_file(utterance)
            # return HttpResponse(content, content_type='text/plain')
            time.sleep(40)
    return render(request, "index.html", {'form': form, 'content': content})

