import qrcode

def generate_qr_code(text,filename):
    qr = qrcode.QRCode(
        version= 8,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    Image = qr.make_image(fill_color="#6aff9b",back_color="Black")
    Image.save(filename)

text = "https://training.techwithtim.net/free-guide"
filename = "qr_code.png"

generate_qr_code(text, filename)
print(f"QR code saved as {filename}")