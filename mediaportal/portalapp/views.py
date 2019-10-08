from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from portalapp.models import Category


class BaseView(View):

    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, self.template_name, context)
