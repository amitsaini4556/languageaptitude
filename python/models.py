from django.db import models

# Create your models here.
class python(models.Model):
    quizname=models.TextField(max_length=10)
    question=models.TextField(max_length=500)
    code=models.TextField(max_length=1000)
    op1=models.TextField(max_length=100)
    op2=models.TextField(max_length=100)
    op3=models.TextField(max_length=100)
    op4=models.TextField(max_length=100)
    answer=models.TextField(max_length=100)
    solution=models.TextField(max_length=500)

    def __str__(self):
        return str(self.quizname)
