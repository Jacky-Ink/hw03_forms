from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group',)
        help_text = {
            'text': 'Поле для ввода текста поста',
            'group': 'Выберете соответствующую группу'
        }