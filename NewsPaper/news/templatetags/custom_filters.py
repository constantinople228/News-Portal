from django import template


register = template.Library()

bad_word = ['редиска']


@register.filter()
def censor(word):
    if isinstance(word, str):
        for i in bad_word:
            word = word.replace(i[1:], '*' * len(i[1:]))
    else:
        raise ValueError('')
    return word
