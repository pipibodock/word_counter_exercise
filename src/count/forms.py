from django import forms

class WordCountForm(forms.Form):

    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "text here...",
            }
        )
    )