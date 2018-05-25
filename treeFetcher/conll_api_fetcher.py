import requests
import json

# curl -s -X GET -H 'Content-Type: application/json' -d'{"text": "גנן גידל דגן בגן  "}' localhost:8000/yap/heb/pipeline | jq -r '.dep_tree' | sed -e 's/\\t/\t/g' -e 's/\\n/\n/g'
url = "http://onlp.openu.org.il:8000/yap/heb/joint"

def call_yap_webapi(utterance) -> dict:
    data = '''{"text": "%s  "}''' % utterance
    response = requests.post(url,
                             data=data.encode('utf-8'),
                             headers={'Content-type': 'applications/json'})
    return response.json()

def parse_sentence(utterance) -> dict:
    return call_yap_webapi(utterance)

def conll_to_list(conll):
    lemmas = []
    print(conll)
    for line in conll.split("\n"):
        if not line:
            continue
        print("line: ", line)
        parts = [part for part in line.split("\t")]
        lemmas.append(parts)
    print("lemmas", lemmas)
    return lemmas


def segment_query(conll):
    lemmas = conll_to_list(conll)
    pos = []
    for lemma in lemmas:
        if '-' not in lemma[0]:
            pos.append(lemma[1])
    return " ".join(pos)

def pos_tagger(conll):
    lemmas = conll_to_list(conll)
    pos = []
    for lemma in lemmas:
        if (lemma[3] != "PUNCT") and ('-' not in lemma[0]):
            pos.append(". . %s %s  . ." % (lemma[1], lemma[3]))
    return "\t".join(pos)


def morphological_analyzer(conll):
    lemmas = conll_to_list(conll)
    morph = []
    for lemma in lemmas:
        if (lemma[3] != "PUNCT") and ('-' not in lemma[0]):
            morph.append("%s\t\t%s\t\t" % (lemma[1], lemma[5].replace("|", "\t\t").replace("_", "\t")))
    return "\n".join(morph)


def show_dependencies(conll):
    lemmas = conll_to_list(conll)
    dependencies = []
    for line in lemmas:
        if (line[3] != "PUNCT") and ('-' not in line[0]):
            relation = line[7]
            head_index = line[6]
            head_lemma = "root"
            for subline in lemmas:
                if subline[0] == head_index:
                    head_lemma = subline[1]
            self_lemma = line[1]
            self_index = line[0]
            dependency = "%s(%s-%s, %s-%s)" %(relation, self_lemma, self_index, head_lemma, head_index)
            dependencies.append(dependency)
    return "\n".join(dependencies)