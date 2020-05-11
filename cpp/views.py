from django.shortcuts import render
from .models import cpp

# Create your views here.
def cppquiz(request):

    if request.method=='POST':
        count=int(request.POST['count'])
        intfirst=count+1
        print(intfirst)
        data_list=cpp.objects.filter(quizname=request.POST['quiz']).filter(question__contains=str(intfirst))
        return render(request,'cpp/quiz.html',{'data_list':data_list,'count':count,'quiz':request.POST['quiz']})
    else:
        info="Basic rules for a quiz"+"\n"+"=> There will be 10 Question."+"\n"+"=> 4 Marks for each correct answer."+"\n"+"=> 2 marks will be deducted for each wrong answer"+"\n"+"=> Best Of Luck!!!"
        return render(request,'cpp/quiz.html',{'info':info,'count':0})
