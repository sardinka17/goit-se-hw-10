from django.urls import path

from add_content.views import AddAuthorView, AddQuoteView

app_name = 'add_content'

urlpatterns = [
    path('add_author/', AddAuthorView.as_view(), name='add_author'),
    path('add_quote/', AddQuoteView.as_view(), name='add_quote')
]