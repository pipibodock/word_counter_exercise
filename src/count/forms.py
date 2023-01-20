from django import forms


class WordCountForm(forms.Form):

    body = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "text here...",
            }
        )
    )