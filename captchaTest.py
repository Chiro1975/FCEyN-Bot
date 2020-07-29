from captcha.image import ImageCaptcha
from random import  randint

'''
Para armar el captcha, se necesita una fuente del sistema, el paquete de python
trae una por defecto, pero se recomienda usar una fuente instalada. Uso fuentes
Ubuntu ya que estoy casi seguro que estás leyendo esto desde Ubuntu.
'''

image = ImageCaptcha(fonts=['/usr/share/fonts/ubuntu/UbuntuMono-BI.ttf'])

captcha = str(randint(1000000, 9999999))

print(captcha)

image.write(captcha, 'out.png')
