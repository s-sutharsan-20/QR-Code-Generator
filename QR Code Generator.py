import qrcode
data='www.github.com'
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_colour='red',back_colour='white')
img.save('github qrcode.png')
