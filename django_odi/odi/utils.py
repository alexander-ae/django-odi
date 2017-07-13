import os
import imghdr
import logging
import mimetypes
from subprocess import check_call
from uuid import uuid4
from PIL import Image
from django.conf import settings as django_settings
from . import settings


def optimize_image(file):
    ''' Optimiza una imagen '''
    image_type = imghdr.what(file)
    original_name = file.name
    uuid_folder = str(uuid4())
    new_folder = os.path.join(django_settings.MEDIA_ROOT, uuid_folder)

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    new_filename = os.path.join(new_folder, original_name)

    if image_type == 'jpeg':
        img = optimize_jpg(file, new_filename)
    elif image_type == 'png':
        img = optimize_png(file, new_filename)

    return {
        'image': img.read(),
        'mimetype': mimetypes.guess_type(new_filename)[0],
        'original_size': humansize(file.size),
        'size': humansize(os.path.getsize(new_filename)),
        'url': '{}{}/{}'.format(django_settings.MEDIA_URL, uuid_folder, original_name)
    }


def optimize_jpg(file, new_filename):
    ''' Optimiza un archivo JPG '''
    img = Image.open(file)
    temp_filename = '{}{}'.format(new_filename, '.old.jpg')
    img.save(temp_filename)

    cjpeg_command = '{} "{}" pnm:- | {} -optimize -baseline -quality {} > "{}"'.format(settings.CONVERT_PATH,
                                                                                       temp_filename,
                                                                                       settings.CJPEG_PATH,
                                                                                       settings.CJPEG_QUALITY,
                                                                                       new_filename)
    logging.debug(cjpeg_command)
    check_call(cjpeg_command, shell=True)

    img = open(new_filename, "rb")

    return img


def optimize_png(file, new_filename):
    ''' Optimiza un archivo PNG '''
    img = Image.open(file)
    temp_filename = '{}{}'.format(new_filename, '.old.png')
    img.save(temp_filename)

    pngquant_command = '{} -f --quality={} -o"{}" "{}"'.format(settings.PNGQUANT_PATH, settings.PNGQUANT_QUALITY,
                                                               new_filename, temp_filename)
    logging.debug(pngquant_command)
    check_call(pngquant_command, shell=True)

    img = open(new_filename, "rb")

    return img


def humansize(nbytes):
    ''' COnvierte el tamaño de un archivo de bytes a formato legible '''
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])
