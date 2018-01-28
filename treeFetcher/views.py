from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UtteranceForm
from .conll_file_fetcher import parse_sentence, pos_tagger, show_dependencies
import subprocess
# Create your views here.
import time


def home(request):
    return render(request, 'index.html')


def submit_utterance(request):
    dep_output = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/data/dep_output.conll'
    query = ""
    pos = ""
    relations = ""
    if request.method == 'GET':
        form = UtteranceForm
    else:
        form = UtteranceForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('utterance')
            annotation = form.cleaned_data.get('annotation')
            parsing = parse_sentence(query)
            parsing.wait()
            pos = pos_tagger()
            relations = show_dependencies()
    return render(request, "index.html", {'form': form, 'pos': pos, 'relations': relations, 'query': query})

