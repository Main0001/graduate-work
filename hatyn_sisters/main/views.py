from django.shortcuts import render


def index(request):
    context = {'title': 'Main page'}
    return render(request, 'main/main_page.html', context=context)


def bells(request):
    context = {'title': 'Bells information'}
    return render(request, 'main/bells-information.html', context=context)


def monument(request):
    context = {'title': 'Monument information'}
    return render(request, 'main/monument-information.html', context=context)


def villages(request):
    context = {'title': 'Villages'}
    return render(request, 'main/villages.html', context=context)
