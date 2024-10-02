from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


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


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user