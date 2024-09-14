from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['heading', 'author', 'text', 'category']

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        text = cleaned_data.get("text")

        if len(heading) > 100:
            raise ValidationError(
                "Слишком длинное название."
            )
        if text is not None and len(text) < 20:
            raise ValidationError(
                "Текст слишком короткий.")

        return cleaned_data

