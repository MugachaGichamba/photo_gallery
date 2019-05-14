from django.shortcuts import render
from .models import Image, Location
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'photos/home.html', context)


class PicListView(ListView):
    model = Image
    template_name = 'photos/home.html'
    context_object_name = "images"


def Location(request):
    data = request.GET["Location"]

    # context = {"images" : Image.objects.filter(image_location=data)}
    for image in Image.objects.filter():
        print(image.image_category)

    return render(request, 'location.html', {'data':data})

#
# class CategoryView(DetailView):
#     model = Image
#
