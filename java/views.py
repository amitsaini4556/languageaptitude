from django.shortcuts import render
from .models import java

# Create your views here.
def javaquiz(request):

    if request.method=='POST':

        data=java.objects.filter(quizname=request.POST['quiz'])

        return render(request,'cpp/quiz.html',{'data':data})
    else:
        info="basic rules for a quiz"
        return render(request,'cpp/quiz.html',{'info':info})
