import qrcode
from flask import url_for
from qrcode.image.styles.moduledrawers import SquareModuleDrawer


def generator_qr_code(qr_path: str, site_domain: str) -> None:
    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4,
    )

    url = get_full_site_url(site_domain)
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black",
                          back_color="white",
                          module_drawer=SquareModuleDrawer())
    image.save(qr_path)


def get_full_site_url(site_domain: str) -> str:
    site_domain += url_for('get_dummy_request_from_qr_code')
    return site_domain
