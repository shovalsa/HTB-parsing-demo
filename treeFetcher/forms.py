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
