from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    
    # def 방식
    # # ex: /polls/
    # path('',views.index, name ='index'),  # '~~/polls/' url 은 view 내부로 연결 
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote')

    # generic class 방식
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

