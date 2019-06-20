from django.shortcuts import render,redirect, HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
from .models import Shows


#------------------------------------------------
#root menu
#------------------------------------------------
def index(request):

    context = {
        'Shows': Shows.objects.all()
    }

    return render(request,"tv_shows/index.html",context)
#------------------------------------------------
#page to display the form to add a show
#------------------------------------------------
def add_show(request):
    return render(request,"tv_shows/add_show.html")
#------------------------------------------------
#method to process forms into the db
#------------------------------------------------
def process(request):
    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value,extra_tags=key)
        return redirect('/shows/new')

    else:
        show = Shows.objects.create(title=request.POST["title"], network=request.POST["network"],desc=request.POST["desc"], date=request.POST["date"])

        id = show.id

    return redirect("/shows"+ str(id))

def update(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        show_id = request.POST["show_id"]
        id = show_id
        return redirect('/shows/edit/'+str(id))

    else:
        show_id = request.POST["show_id"]
        show = Shows.objects.get(id=show_id)
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.date = request.POST["date"]
        show.desc = request.POST["desc"]
        show.save()

        id = show_id

    return redirect("/shows/"+ str(id))


#------------------------------------------------
#shows the shows info
#------------------------------------------------
def show(request,val):
    context = {
        "shows" : Shows.objects.get(id=val)
    }
    return render(request,"tv_shows/show.html",context)
#------------------------------------------------
#edit page to display the form to update
#------------------------------------------------
def edit(request,val):
    show = Shows.objects.get(id=val)
    # date = show.date.strftime("%Y-%m-%d")
    # print(date)
    context = {
        "shows" : Shows.objects.get(id=val),
        "date": show.date.strftime("%Y-%m-%d")
    }
    return render(request,"tv_shows/edit.html",context)
#------------------------------------------------
#method to delete the input
#------------------------------------------------
def destroy(request,val):
    show = Shows.objects.get(id=val)
    show.delete()

    return redirect("/shows")
