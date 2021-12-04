import qrcode
from flask import Flask, render_template, send_file
from qrcode.image.styles.moduledrawers import SquareModuleDrawer

app = Flask('QR code redirecter')


@app.get('/generate')
def generate_qr_code():
    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4,
    )
    # qr.add_data(url_for('get_dummy_request_from_qr_code'))
    qr.add_data('edu.vsu.ru')
    qr.make(fit=True)

    image = qr.make_image(fill_color="black",
                          back_color="white",
                          module_drawer=SquareModuleDrawer())
    image.save('./static/images/qrcode.jpeg')
    return send_file('./static/images/qrcode.jpeg', mimetype='image/gif')


@app.get('/dummy_request')
def get_dummy_request_from_qr_code():
    return render_template('index.html')
