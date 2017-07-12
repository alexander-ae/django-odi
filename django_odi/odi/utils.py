import os
import imghdr
import logging
import mimetypes
from subprocess import check_call
from PIL import Image


def optimize_image(file):
    ''' Optimiza una imagen '''
    image_type = imghdr.what(file)
    print(image_type)

    if image_type == 'jpeg':
        img, filename = optimize_jpg(file)
    elif image_type == 'png':
        img, filename = optimize_png(file)

    return {
        'image': img.read(),
        'mimetype': mimetypes.guess_type(filename)[0],
        'size': os.path.getsize(filename)
    }


def optimize_jpg(file):
    ''' Optimiza un archivo JPG '''
    img = Image.open(file)
    img.save('/tmp/test1.jpg')

    cjpeg_command = '/usr/bin/convert "/tmp/test1.jpg" pnm:- | /usr/bin/cjpeg -optimize -baseline -quality 75 > "/tmp/test2.jpg"'
    logging.debug(cjpeg_command)
    check_call(cjpeg_command, shell=True)

    img = open("/tmp/test2.jpg", "rb")
    # image_data = img.read()

    return (img, '/tmp/test2.jpg')


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
