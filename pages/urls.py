from django.urls import path


from . import views


urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('recent', views.RecentVacanciesView.as_view(), name='recentVacancies'),
    path('demand', views.DemandView.as_view(), name='demand'),
    path('geography', views.GeographyView.as_view(), name='geography'),
    path('skills', views.SkillsView.as_view(), name='skills')
]