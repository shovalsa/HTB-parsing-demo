from .conll_api_fetcher import parse_sentence, morphological_analyzer, show_dependencies, segment_query, pos_tagger
from django.shortcuts import render, redirect
from .forms import UtteranceForm

def submit_utterance(request):
    lattices = ''
    query = ""
    pos = ""
    relations = ""
    segments = ''
    morph = ''
    if request.method == 'GET':
        form = UtteranceForm
    else:
        form = UtteranceForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('utterance')
            parse_data = parse_sentence(query)
            try:
                lattice = parse_data['md_lattice']
                lattices = parse_data['ma_lattice']
                conll = parse_data['dep_tree']
                segments = segment_query(conll)
                pos = pos_tagger(lattice)
                morph = morphological_analyzer(lattice)
                relations = show_dependencies(conll)
            except KeyError:
                pos = "error"
    return render(request, "index.html", {'form': form, 'pos': pos, 'morph': morph, 'relations': relations, 'segments': segments, 'query': query, 'lattices': lattices})




def send_bad_input():
    pass

def send_wrong_parse():
    pass

def send_correct_parse():
    pass