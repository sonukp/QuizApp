from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from quiz.models import Quiz,QuizUser,Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.


@login_required
def quiz(request):
    quiz = Quiz.objects.all()
    return render(request, 'quiz.html', {'quiz': quiz})


@login_required
@csrf_exempt
def quiz_page(request, quizname):
    # import pdb
    # pdb.set_trace()
    print("A")
    if request.method == "POST":
        # quiz = Quiz.objects.get(name=name)
        questions = Question.objects.all()
        score = 0
        quiz = ""
        for question in questions:
            correct_answer = question.answer
            print(question.quiz.name)
            entered_answer = request.POST.get(str(question.id))
            if entered_answer == correct_answer:
                score += 1
                quiz = question.quiz.name
        name = request.user.get_username()
        print(quiz)
        u = User.objects.get(username=name)
        user = QuizUser.objects.get(user=u)
        user.score = score
        user.quiz = quiz
        user.save()
        print(user.score, user.quiz)
        print(name, user)
        context = {'score': score}
        return render(request, 'result.html', context)
    else:
        quiz = Quiz.objects.get(name=quizname)
        ques = Question.objects.filter(quiz=quiz)
        print(quiz)
        # opt = Option.objects.all()
        # opt = Option.objects.filter(question=ques)
        # data = {"ques":ques, }
        return render(request, 'quiz_page.html', {'ques': ques, "quiz":quiz})



@api_view(['GET',])
def get_user_details(request,name):
    if request.method == "GET":
        u = User.objects.get(username = name)
        user = QuizUser.objects.get(user=u)

        data = {"results": {
            'user': u.username,
            "Question": user.quiz.name,
            "Score": user.score
        }}
        return Response(data)

