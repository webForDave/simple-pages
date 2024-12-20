from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
