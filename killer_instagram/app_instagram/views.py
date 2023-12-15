import os
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Picture
from .forms import PictureForm

# Create your views here.
def main(request):
    # mapped to app_instagram/template/...
    return render(request, "app_instagram/index.html", context={"title":"Hello world new instagram"})

def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance = Picture())
        if form.is_valid():
            form.save()
            return redirect(to="app_instagram:pictures")
    return render(request, "app_instagram/upload.html", context={"title": "Hello world from upload", "form": form})

def pictures(request):
    pictures = Picture.objects.all() #objects as SQL-query
    return render(request, "app_instagram/pictures.html", 
                  context={"title": "Hello world from pictures", "pictures": pictures, "media": settings.MEDIA_URL})

def remove(request, pic_id):
    picture = Picture.objects.filter(pk=pic_id)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.first().path)))
    except OSError as e:
        print(e)
    picture.delete()
    return redirect(to="app_instagram:pictures")

def edit(request, pic_id):

    if request.method == "POST":
        description = request.POST.get('description')
        Picture.objects.filter(pk=pic_id).update(description=description)
        return redirect(to="app_instagram:pictures")
    picture = Picture.objects.filter(pk=pic_id).first()
    return render(request, "app_instagram/edit.html", 
                  context={"title": "Hello world from pictures", "pic": picture, "media": settings.MEDIA_URL})
