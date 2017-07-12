from subprocess import check_call
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image


def upload(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        file = request.FILES.get('file')
        print(file, type(file))
        img = Image.open(file)
        img.save('/tmp/test1.jpg')

        check_call(
            '/usr/bin/convert "/tmp/test1.jpg" pnm:- | /usr/bin/cjpeg -optimize -baseline -quality 75 > "/tmp/test2.jpg"',
            shell=True)

        image_data = open("/tmp/test2.jpg", "rb").read()
        return HttpResponse(image_data, content_type="image/jpg")

    return render(request, 'index.html')
