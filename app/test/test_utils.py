import os
from os.path import join, dirname, realpath

import pytest

from app.config import QR_CODE_PATH
from app.utils import generator_qr_code


@pytest.fixture
def mocked_url_for(mocker):
    return mocker.patch('app.utils.get_full_site_url')


def test_generator_qr_code(mocked_url_for):
    mocked_url_for.return_value = '127.0.0.1:8080/dummy_request'

    generator_qr_code(qr_path=QR_CODE_PATH, site_domain='127.0.0.1:8080')

    assert os.path.exists(QR_CODE_PATH)
