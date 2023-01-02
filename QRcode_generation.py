import qrcode

from PIL import Image

qr=qrcode.QRCode(version=1, errpr_correction=qrcode.constants.ERROR_CORRECTIOM_H,
                 box_size=10, border=5)

qr.add_data('https://github.com/sam1145/Python_mini-projects')
qr.make(fir=True)
img=qr.make_image(fill_color='black', back_color='white')
img.save('shamanth_github.png')