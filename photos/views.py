from django.shortcuts import render


def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'photos/base.html')

