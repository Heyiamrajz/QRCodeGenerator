import qrcode
from PIL import Image, ImageDraw, ImageFont


def gen_qrcode(data, message):
    try:
    qr = qrcode.QRCode(box_size=10, border=6)  # Increase border size to 6

        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("qrfont.ttf", 30)

        draw.text((20, 20), message, font=font)  # Position message at the top-left

        img.save("Generated_QR.png")
        return True, data
    except Exception:
        raise Exception("Error occurred in gen_qrcode function")

# Example usage
data_input = input("Enter data for QR: ")
message_input = input("Enter message to be Displayed at Top Left of QR: ")
gen_qrcode(data_input, message_input)
