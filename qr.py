import qrcode

def generateQRImage(data):
    qr = qrcode.QRCode(box_size=5, border=20)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image()
    return image
