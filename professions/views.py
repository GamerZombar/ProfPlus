from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from professions.models import Profession


class ProfessionView(View):
    '''вывод данных профессий'''
    def get(self, request):
        professions = Profession.objects.all()
        return render(request, 'professions/index.html', {'profession_list': professions})
