from django.shortcuts import render
from .models import python

# Create your views here.
def pythonquiz(request):

    if request.method=='POST':

        data=python.objects.filter(quizname=request.POST['quiz'])

        return render(request,'cpp/quiz.html',{'data':data})
    else:
        info="basic rules for a quiz"
        return render(request,'cpp/quiz.html',{'info':info})
