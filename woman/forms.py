from django import forms
from .models import Category, Women
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                  label="Категории")

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'tags']
        labels = {'slug': 'URL'}
        widgets = {
            'title': forms.TextInput (attrs={'class': 'form-input'}),
            'content': forms.Textarea (attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError ('Длина превышает 50 символов')

        return title