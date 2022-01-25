from django.shortcuts import render,get_object_or_404

from django.shortcuts import HttpResponse
from .models import Question
# Create your views here.

def Index(request):
    context={
        "var":"variable from views.py ...",
        "list_list":['python','java','javascripts']
    }
    return render(request,"polls/index.html",context=context)

def Polls(request):
    polls=Question.objects.all()
    context={
        'polls':polls

    }
    return render(request,'polls/polls_list.html',context)

def Poll_details(request,poll_id):
    #poll=Question.objects.get(id=poll_id)
    poll= get_object_or_404(Question,pk=poll_id)
    context={
        'poll':poll,
    }

    return render(request,'polls/poll_details.html',context)