from django.shortcuts import render
from django.http import HttpResponse
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

        response = HttpResponse(image_data['image'], content_type="image/jpg")
        response['Content-Length'] = image_data['size']
        response['Content-Disposition'] = 'attachment; filename={}'.format(file.name)
        return response

    return render(request, 'index.html')
