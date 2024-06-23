from django.urls import reverse_lazy
from django.views.generic import CreateView

from add_content.form import AuthorForm, QuoteForm


# Create your views here.

class AddAuthorView(CreateView):
    template_name = 'add_content/add_author.html'
    form_class = AuthorForm
    success_url = reverse_lazy('quotes:index')


class AddQuoteView(CreateView):
    template_name = 'add_content/add_quote.html'
    form_class = QuoteForm
    success_url = reverse_lazy('quotes:index')
