from django import forms
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class new_tasks_form(forms.Form):
    task = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter task'}), 
        label='', 
        error_messages={'required': ''}
    )
def index(request):
    form = new_tasks_form(request.POST)
    if "tasks" not in request.session :
        request.session["tasks"]=[]
    if request.method == "GET" :
        return render(request, "tasks/index.html", {
            "tasks": request.session["tasks"], "form": form
        })
    elif request.method == "POST" :
        if form.is_valid() :
            task = form.cleaned_data["task"] 
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else :
            return render(request, "tasks/index.html", {
            "tasks": request.session["tasks"], "form": form
    })
        
    return render(request, "tasks/index.html", {
        "form": new_tasks_form()
    })

