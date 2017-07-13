import os
import imghdr
import logging
import mimetypes
from subprocess import check_call
from uuid import uuid4
from PIL import Image
from django.conf import settings


def optimize_image(file):
    ''' Optimiza una imagen '''
    image_type = imghdr.what(file)
    original_name = file.name
    uuid_folder = str(uuid4())
    new_folder = os.path.join(settings.MEDIA_ROOT, uuid_folder)

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    new_filename = os.path.join(new_folder, original_name)
    print(new_filename)
    print(image_type)

    if image_type == 'jpeg':
        img, filename = optimize_jpg(file, new_filename)
    elif image_type == 'png':
        img, filename = optimize_png(file, new_filename)

    return {
        'image': img.read(),
        'mimetype': mimetypes.guess_type(filename)[0],
        'size': os.path.getsize(filename),
        'url': '{}{}/{}'.format(settings.MEDIA_URL, uuid_folder, original_name)
    }


def optimize_jpg(file, new_filename):
    ''' Optimiza un archivo JPG '''
    img = Image.open(file)
    temp_filename = '{}{}'.format(new_filename, '.old.jpg')
    img.save(temp_filename)

    cjpeg_command = '/usr/bin/convert "{}" pnm:- | /usr/bin/cjpeg -optimize -baseline -quality 80 > "{}"'.format(
        temp_filename, new_filename)
    logging.debug(cjpeg_command)
    check_call(cjpeg_command, shell=True)

    img = open(new_filename, "rb")
    # image_data = img.read()

    return (img, new_filename)


def optimize_png(file):
    ''' Optimiza un archivo PNG '''
    img = Image.open(file)
    img.save('/tmp/test1.png')

    pngquant_command = '/usr/local/bin/pngquant -f --quality=75-90 -o"/tmp/test2.png" "/tmp/test1.png"'
    logging.debug(pngquant_command)
    check_call(pngquant_command, shell=True)

    img = open("/tmp/test2.png", "rb")
    # image_data = img.read()

    return (img, '/tmp/test2.png')
