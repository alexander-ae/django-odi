from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import optimize_image


def home(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        file = request.FILES.get('file')
        print(file, type(file))

        image_data = optimize_image(file)

        return JsonResponse({'url': image_data.get('url')})

    return render(request, 'index.html')
