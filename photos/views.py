from django.shortcuts import render
from .models import Image, Location, Category
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


def GetLocation(request):
    data = request.GET["search_query"]

    # context = {"images" : Image.objects.filter(image_location=data)}
    # for image in Image.objects.filter():
    #     print(image.image_location.id)
    images = {}
    locale  = Location.objects.filter(image_location=data).first()
    categ = Category.objects.filter(image_category=data).first()
    if locale:
        images = Image.objects.filter(image_location=locale)
    elif categ:
        images = Image.objects.filter(image_category=categ)
    else:
        images = {}
    return render(request, 'search.html', {"images" : images})

#
# class CategoryView(DetailView):
#     model = Image
#
