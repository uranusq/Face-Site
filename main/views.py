from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django_user_agents.utils import get_user_agent
from main import models

def main(request):
    user_agent = get_user_agent(request)

    users = models.User.objects.all()
    projects = models.Project.objects.all()

    if user_agent.is_mobile:
        return render(request, 'main.html', { "users": users, "projects": projects })
    else:
        return render(request, 'main.html', {"users": users, "projects": projects})
