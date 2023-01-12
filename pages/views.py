from django.shortcuts import render
from django.views import View

from pages.models import Homepage
from professions.models import Blog


# Create your views here.

class HomepageView(View):
    '''вывод данных профессий'''
    def get(self, request):
        homepage_profession = Homepage.objects.first().profession
        profession_blogs = Blog.objects.filter(profession=homepage_profession)
        return render(request, 'professions/homepage.html', {'profession': homepage_profession, 'blogs_list': profession_blogs})