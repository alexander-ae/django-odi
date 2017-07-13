from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import optimize_image


def home(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file')

        image_data = optimize_image(file)

        return JsonResponse({'url': image_data.get('url'), 'original_size': image_data.get('original_size'),
                             'size': image_data.get('size')})

    return render(request, 'index.html')
