from django import forms


class UtteranceForm(forms.Form):
    utterance = forms.CharField(label='Utterance', widget=forms.Textarea(attrs={
        'placeholder': 'למשל, גנן גידל דגן בגן',
        'rows': 3,
        'cols': 80}))

    annotation_options = ((None, "Choose Annotation"), ('segmentation', 'Segmentation'), ('pos', 'Part-of_speech Tags'),
                          ('dependency', 'Dependency Parse'),)
    # annotation = forms.MultipleChoiceField(choices=annotation_options)
    filename_options = ((None, "Choose type of output"), ('input', 'Input'), ('lattices', 'All possible lattices'),
                        ('output', 'The most likely lattice'), ('dependency', 'Dependency Parse'),)
    # filename = forms.ChoiceField(choices=filename_options, label="Type of output")


conll_placeholder = """

# text = אכן, כך עשתה חטיבת "הראל".
1	אכן	אכן	ADV	ADV	_	4	advmod	_	SpaceAfter=No
2	,	,	PUNCT	PUNCT	_	4	punct	_	_
3	כך	כך	ADV	ADV	_	4	advmod	_	_
4	עשתה	עשה	VERB	VERB	Gender=Fem|HebBinyan=PAAL|Number=Sing|Person=3|Tense=Past|Voice=Act	0	root	_	_
5	חטיבת	חטיבה	NOUN	NOUN	Definite=Cons|Gender=Fem|Number=Sing	4	nsubj	_	_
6	"	"	PUNCT	PUNCT	_	7	punct	_	SpaceAfter=No
7	הראל	הראל	PROPN	PROPN	_	5	flat:name	_	SpaceAfter=No
8	"	"	PUNCT	PUNCT	_	7	punct	_	SpaceAfter=No
9	.	.	PUNCT	PUNCT	_	4	punct	_	_
"""

class ConllForm(forms.Form):
    utterance = forms.CharField(label='Utterance', widget=forms.Textarea(attrs={
        'placeholder': conll_placeholder,
        'rows': 10,
        'cols': 120}))
