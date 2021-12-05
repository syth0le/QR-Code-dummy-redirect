from flask import Flask, render_template, send_file

from app.config import QR_CODE_PATH, SITE_URL
from app.utils import generator_qr_code

app = Flask('QR code redirecter')


@app.get('/generate')
def get_generated_qr_code():
    generator_qr_code(qr_path=QR_CODE_PATH, site_domain=SITE_URL)
    return send_file(QR_CODE_PATH, mimetype='image/gif')


@app.get('/dummy_request')
def get_dummy_request_from_qr_code():
    return render_template('index.html')
