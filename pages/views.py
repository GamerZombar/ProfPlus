from datetime import datetime
from dateutil.parser import parse


from django.shortcuts import render
from django.views import View

from pages.models import Page, Article
import requests

# Create your views here.

class HomepageView(View):
    '''вывод данных профессий'''

    def get(self, request):
        page_name = 'homepage'
        homepage = Page.objects.filter(page_name=page_name).first()
        homepage_profession = homepage.profession
        profession_articles = Article.objects.filter(page=homepage, profession=homepage_profession)
        return render(request, 'professions/homepage.html',
                      {'profession': homepage_profession, 'articles_list': profession_articles})


class DemandView(View):
    '''вывод востребованности профессии'''

    def get(self, request):
        page_name = 'demand'
        homepage = Page.objects.filter(page_name=page_name).first()
        homepage_profession = homepage.profession
        profession_articles = Article.objects.filter(page=homepage, profession=homepage_profession)
        return render(request, 'professions/demand.html',
                      {'profession': homepage_profession, 'articles_list': profession_articles})


class GeographyView(View):

    def get(self, request):
        page_name = 'geography'
        homepage = Page.objects.filter(page_name=page_name).first()
        homepage_profession = homepage.profession
        profession_articles = Article.objects.filter(page=homepage, profession=homepage_profession)
        return render(request, 'professions/geography.html',
                      {'profession': homepage_profession, 'articles_list': profession_articles})


class SkillsView(View):
    def get(self, request):
        page_name = 'skills'
        homepage = Page.objects.filter(page_name=page_name).first()
        homepage_profession = homepage.profession
        profession_articles = Article.objects.filter(page=homepage, profession=homepage_profession)
        return render(request, 'professions/skills.html',
                      {'profession': homepage_profession, 'articles_list': profession_articles})
class RecentVacanciesView(View):
    """вывод последних вакансий с hh.ru"""

    def get(self, request):

        profession = 'Backend-программист'

        date = "2022-12-22"
        url = f"https://api.hh.ru/vacancies?text=backend&per_page=10&date_from={date}&date_to={date}"

        response = requests.get(url).json()

        items = response.get('items')

        vacancies = []

        if items is not None:
            for item in items:
                vacancy_id = item.get('id')
                vacancy_name = item.get('name')
                vacancy_info = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}').json()
                vacancy_desc = vacancy_info.get('description')
                vacancy_skills = vacancy_info.get('key_skills')
                if vacancy_skills is not None:
                    result = []
                    for skill in vacancy_skills:
                        result.append(skill.get('name'))
                    vacancy_skills = result
                vacancy_company = item.get('employer').get('name')
                vacancy_salary = item.get('salary')
                if vacancy_salary is not None:
                    salary_from = item.get('salary').get('from')
                    salary_to = item.get('salary').get('to')
                    vacancy_salary = ""
                    if salary_from is not None:
                        vacancy_salary += f"От {salary_from}"
                    if salary_to is not None:
                        vacancy_salary += f" До {salary_to}"
                    vacancy_salary += " рублей"
                else:
                    vacancy_salary = "Не указано"
                vacancy_region = item.get('area').get('name')
                vacancy_pub_date = item.get('published_at')

                vacancies.append({
                    'name': vacancy_name,
                    'description': vacancy_desc,
                    'skills': vacancy_skills,
                    'company': vacancy_company,
                    'salary': vacancy_salary,
                    'region': vacancy_region,
                    'published_date': parse(vacancy_pub_date).strftime('%d.%m.%Y')

                })

        return render(request, 'professions/recent.html', {'profession': profession,'vacancies': vacancies})
