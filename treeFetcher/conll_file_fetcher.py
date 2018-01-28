import subprocess
import io

yap = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/yap_run.sh'
yap_nett = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/yap'
dep_output = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/data/dep_output.conll'


def create_input_raw(utterance):
    seperated = utterance.split(" ")
    input_path = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/data/input.raw'
    with open(input_path, 'w') as file:
        file.write('\n'.join(seperated))
        file.write("\n\n")
    return input_path


def parse_sentence(utterance):
    create_input_raw(utterance)
    parsing = subprocess.Popen(yap, shell=True)
    parsing.wait()
    return parsing


def conll_to_list():
    with open(dep_output, 'r') as parse:
        lemmas = []
        for line in parse.readlines()[0:-1]:
            parts = [part for part in line.split("\t")]
            lemmas.append(parts)
    return lemmas

def pos_tagger():
    lemmas = conll_to_list()
    for line in lemmas:
        pos = ["%s\%s" % (line[1], line[3]) for line in lemmas]
    return " ".join(pos)


def show_dependencies():
    lemmas = conll_to_list()
    dependencies = []
    for line in lemmas:
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


def statistics():
    pass
# I can't extract the time from shell. maybe Amit can help.
