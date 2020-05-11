from django.shortcuts import render
from .models import python

# Create your views here.
def pythonquiz(request):

    if request.method=='POST':

        data=python.objects.filter(quizname=request.POST['quiz'])

        return render(request,'cpp/quiz.html',{'data':data})
    else:

        info="Basic rules for a quiz"+"\n"+"=> There will be 10 Question."+"\n"+"=> 4 Marks for each correct answer."+"\n"+"=> 2 marks will be deducted for each wrong answer"+"\n"+"=> Best Of Luck!!!"
        return render(request,'cpp/quiz.html',{'info':info})
