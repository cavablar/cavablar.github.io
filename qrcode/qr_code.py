from pyzbar.pyzbar import decode
from PIL import Image
import qrcode , time


qr=qrcode.make("666")

name='qr_code'
qr.save(f"{name}.png")

time.sleep(5)
text=decode(Image.open(f'{name}.png'))

text=str(text[0][0])[1:]
print(text)
time.sleep(5)