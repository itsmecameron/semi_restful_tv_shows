from django.shortcuts import render,redirect, HttpResponse
from .models import *
from datetime import datetime
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
        
        show = Shows.objects.create(title=request.POST["title"], network=request.POST["network"],desc=request.POST["desc"], date=request.POST["date"])

        id = show.id

    return redirect("/shows/"+ str(id))

def update(request):
    if request.method== "POST":
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