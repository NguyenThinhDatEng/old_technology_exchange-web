from app1.models import Question
from app1.models import Choice
from django.utils import timezone

t = timezone.now()

q = []

c1 = []
c2 = []

for i in range(2):
    q[i]= Question(question_text= input(), time_pub = t)
    q[i].save()
    c1[i] = Choice(question = q[i], choice_text = input(), vote=0)
    c1[i].save()
    c2[i] = Choice(question = q[i], choice_text = input(), vote=0)
    c2[i].save()
