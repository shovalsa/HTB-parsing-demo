import subprocess
import io

yap = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/yap_run.sh'
yap_nett = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/yap'


def create_input_raw(utterance):
    seperated = utterance.split(" ")
    input_path = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/data/input.raw'
    with open(input_path, 'w') as file:
        file.write('\n'.join(seperated))
        file.write("\n\n")
    return input_path

def get_conll_x_file(utterance):
    input_raw = create_input_raw(utterance)
    lattices_conll = './parsing_handler/yapproj/src/yap/data/lattices.conll'
    output_conll = './parsing_handler/yapproj/src/yap/data/output.conll'
    dep_output = '/home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/data/dep_output.conll'
    parsing = subprocess.Popen(yap, shell=True)
    parsing.wait()
    # create_lattices = subprocess.Popen([yap_nett, 'hebma', '-raw', input_raw, '-out', lattices_conll], shell=True)
    # create_lattices.wait()
    # build_output = subprocess.Popen([yap_nett, 'md', '-in', lattices_conll, '-om', output_conll], shell=True)
    # build_output.wait()
    # build_dep = subprocess.Popen([yap_nett, 'dep', '-inl', output_conll, '-oc', dep_output], shell=True)
    # build_dep.wait()
    content = open(dep_output, 'r').readlines()

    return lattices_conll, output_conll, dep_output, content


# /home/shoval/PycharmProjects/hebrewUD/treeFetcher/parsing_handler/yapproj/src/yap/data