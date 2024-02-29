import qrcode

# import modules

from PIL import Image
 
# taking image which user wants 

 
url_data='https://rkmrc.in/'

gen_QR=qrcode.make(url_data)
QR=qrcode.QRCode(version=15.0,box_size=20, border=3)

QR.add_data(url_data)

QR.make(fit=True)
gen_QR=QR.make_image(fill_color='red', back_color='Skyblue')
gen_QR.save('D:\Learn Python/myqrcode5.png')