import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)
qr.add_data("https://www.google.com")
qr.make(fit=True)
img = qr.make_image(fill_color="orange", back_color="red")
img.save("mycode.png")



