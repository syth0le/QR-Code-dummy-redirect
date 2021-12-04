import io

from qrcode import QRCode, constants
from qrcode.image.styles.moduledrawers import SquareModuleDrawer


class QR_Generator(QRCode):

    def __init__(self, version: int,
                 box_size: int,
                 border: int,
                 filename: str,
                 url: str) -> None:
        super().__init__(version,
                         box_size,
                         border,
                         constants.ERROR_CORRECT_L)
        self.filename = filename
        self.url = url

    def generate(self):
        super().add_data(self.url)
        super().make(fit=True)
        return super().make_image(fill_color="black",
                                  back_color="white",
                                  module_drawer=SquareModuleDrawer())

    def save(self):
        self.generate().save(f'{self.filename}.jpeg')

    def print_qr_in_terminal(self):
        img = io.StringIO()
        self.generate().print_ascii(out=img)
        img.seek(0)

        print(img.read())


# qr = qrcode.QRCode(
#     version=3,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=20,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)

# image = qr.make_image(fill_color="black",
# back_color="white",
# module_drawer=SquareModuleDrawer())
# image.save('qrcode.jpeg')
qr = QR_Generator(version=3,
                  box_size=20,
                  border=4,
                  filename='source',
                  url='www.url.com')
qr.add_data('sdf')
qr.make(fit=True)
image = qr.make_image(fill_color="black",
                      back_color="white",
                      module_drawer=SquareModuleDrawer())
image.save('qrcode.jpeg')
