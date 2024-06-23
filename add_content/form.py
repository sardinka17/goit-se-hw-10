from django.forms import ModelForm, CharField, Textarea, TextInput, SelectMultiple, Select, ModelChoiceField, \
    ModelMultipleChoiceField

from quotes.models import Author, Quote, Tag


class AuthorForm(ModelForm):
    name = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(widget=Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ['name', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    author = ModelChoiceField(widget=Select, queryset=Author.objects.all())
    tags = ModelMultipleChoiceField(widget=SelectMultiple, queryset=Tag.objects.all())
    quote = CharField(widget=Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ['author', 'tags', 'quote']
