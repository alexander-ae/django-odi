from django.conf import settings

CONVERT_PATH = getattr(settings, 'ODI_CONVERT_PATH', '/usr/bin/convert')

CJPEG_PATH = getattr(settings, 'ODI_CJPEG_PATH', '/usr/bin/cjpeg')
CJPEG_QUALITY = getattr(settings, 'ODI_CJPEG_QUALITY', 80)

PNGQUANT_PATH = getattr(settings, 'ODI_PNGQUANT_PATH', '/usr/local/bin/pngquant')
PNGQUANT_QUALITY = getattr(settings, 'ODI_PNGQUANT_QUALITY', 75-90)
