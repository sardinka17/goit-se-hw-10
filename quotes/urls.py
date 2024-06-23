from django.urls import path

from quotes.views import IndexView, AuthorDescriptionView
# from . import views

app_name = 'quotes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('page/<int:page>', IndexView.as_view(), name='index_paginate'),
    path('description/<str:id>', AuthorDescriptionView.as_view(), name='description')
]
