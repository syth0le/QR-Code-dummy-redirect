from flask import Flask

app = Flask('QR code redirecter')


@app.get('/generate')
def generate_qr_code():
    return 'QR code redirecter'


@app.get('/dummy_request')
def get_dummy_request_from_qr_code():
    return 'Picture!'


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)
