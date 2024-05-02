import qrcode
import uuid

def generate_qr_code(url):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Generate a random filename
    filename = str(uuid.uuid4()) + ".png"

    # Save the image
    img.save(filename)

    return filename

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")

    qr_filename = generate_qr_code(website_url)
    print(f"QR code generated and saved as '{qr_filename}'")
