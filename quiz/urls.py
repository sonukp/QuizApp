from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz_list'),
    path('<quizname>', views.quiz_page, name="quiz_page"),
    path('user/<name>', views.get_user_details, name='user_detail'),
]