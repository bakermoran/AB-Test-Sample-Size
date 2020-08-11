"""
sample_size development configuration.

Baker Moran <bamoran99@gmail.com>
"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
# SECRET_KEY = b'FIXME SET THIS WITH: $ python3 -c "import os; print(os.urandom(24))" '  # noqa: E501  pylint: disable=line-too-long
SECRET_KEY = b'\xde\x95\x10z\xc4\xd3`\x9dH\xa61|R^\xd2\xd2wJ9\xbb\x91k\xc2!'  # noqa: E501  pylint: disable=line-too-long
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'uploads'
)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/sample_size.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'sample_size.sqlite3'
)
