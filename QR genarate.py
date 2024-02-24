import qrcode
from PIL import Image
im='Image.gif'
logo=Image.open(im)
basewidth=250
wpercent=(basewidth/float(logo.size[0]))
hsize=int((float(logo.size[1])*float(wpercent)))
logo=logo.resize((basewidth,hsize))


gen_qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=35,border=2)
gen_qr.add_data('rkmrc.in')
gen_qr.make(fit=True)
gen_qr_data=gen_qr.make_image(fill_color="blue",back_color="white").convert("RGB")
pos=((gen_qr_data.size[0]- logo.size[0])// 2,(gen_qr_data.size[1]-logo.size[1])//2)
gen_qr_data.paste(logo,pos)
gen_qr_data.save('myQr2.png')
