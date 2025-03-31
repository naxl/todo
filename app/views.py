from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    if request.method == "POST":
        data = request.POST
        attachment = request.FILES.get("attachment")
        if attachment == None:
            Todo.objects.create(
                name = data.get('name'),
                description = data.get("description"),
                attachment = os.path.join('none.png')
            )
        else:
            Todo.objects.create(
                name = data.get('name'),
                description = data.get("description"),
                attachment = attachment
            )
        return redirect("/")

    all_todos = Todo.objects.all()
    context = {"all_todos" : all_todos}
    return render(request, "index.html", context)


def delete_todo(request, id):
    obj = Todo.objects.get(id = id)
    if str(obj.attachment) != 'none.png':
            img_path = settings.MEDIA_ROOT + '/'+ str(obj.attachment)
            obj.delete()
            os.remove(img_path)
    else:
        obj.delete()
    return redirect("/")

def update_todo(request, id):
    if request.method == "POST":
        data = request.POST
        obj = Todo.objects.get(id = id)
        obj.name = data.get('name')
        obj.description = data.get("description")
        attachment_new = request.FILES.get("attachment")
        if attachment_new == None:
            none_image = os.path.join('none.png')
            if str(obj.attachment) != 'none.png':
                img_path = settings.MEDIA_ROOT + '/'+ str(obj.attachment)
                os.remove(img_path)
                none_image = os.path.join('none.png')
                obj.attachment = none_image
                obj.save()
        else:
            obj.attachment = attachment_new
            obj.save()
        return redirect("/")
    obj = Todo.objects.get(id = id)
    context = dict(name = obj.name,
    description = obj.description,
    attachment = obj.attachment)
    return render(request, "update.html", context)