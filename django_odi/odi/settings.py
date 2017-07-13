from django.conf import settings

CONVERT_PATH = settings.get('ODI_CONVERT_PATH', '/usr/bin/convert')

CJPEG_PATH = settings.get('ODI_CJPEG_PATH', '/usr/bin/cjpeg')
CJPEG_QUALITY = settings.get('ODI_CJPEG_QUALITY', 80)

PNGQUANT_PATH = settings.get('ODI_PNGQUANT_PATH', '/usr/local/bin/pngquant')
PNGQUANT_QUALITY = settings.get('ODI_PNGQUANT_QUALITY', 75-90)
