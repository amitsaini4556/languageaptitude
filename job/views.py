from django.shortcuts import render
from .models import database

# Create your views here.
def home(request):
    return render(request,'job/home.html')
def quiz(request):

    if request.method=='POST':

        integer=int(request.POST['count'])
        intfirst=integer+1
        print(intfirst)
        res=0
        if intfirst>=2:
            xyz=intfirst-1
            print("xyz")
            print(xyz)
            ans=database.objects.filter(quizname=request.POST['quiz']).get(question__contains=str(xyz))
            print(ans.answer)
            print(request.POST['radio'])
            if str(request.POST['radio'])==str(ans.answer):
                res=int(request.POST['result'])+4
                print('result right')
                print(res)
            else:
                res=int(request.POST['result'])-2
                print('result wrong')
                print(res)
        if intfirst==5:
            submission=database.objects.filter(quizname=request.POST['quiz'])

            return render(request,'job/quiz.html',{'submission':submission,'quiz':request.POST['quiz'],'result':res,'incr':0,'close':11})
        data_list=database.objects.filter(quizname=request.POST['quiz']).filter(question__contains=str(intfirst))
        return render(request,'job/quiz.html',{'data_list':data_list,'incr':intfirst,'quiz':request.POST['quiz'],'result':res})
    else:
        info="Basic rules for a quiz"+"\n"+"=> There will be 10 Question."+"\n"+"=> 4 Marks for each correct answer."+"\n"+"=> 2 marks will be deducted for each wrong answer"+"\n"+"=> Best Of Luck!!!"             
        return render(request,'job/quiz.html',{'info':info,'incr':0,'result':0})
