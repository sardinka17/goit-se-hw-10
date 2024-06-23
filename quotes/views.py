from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from quotes.models import Quote, Author


# from django.contrib.auth.decorators import login_required


class IndexView(ListView):
    template_name = 'quotes/index.html'
    model = Quote
    context_object_name = 'quotes'
    paginate_by = 15


class AuthorDescriptionView(View):
    template_name = 'quotes/description.html'

    def get(self, request, id):
        author = Author.objects.get(pk=id)

        return render(request, self.template_name, {'author': author})
