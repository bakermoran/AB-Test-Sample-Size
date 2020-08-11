"""
sample_size package initializer.

Baker Moran <bamoran99@gmail.com>
"""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (insta485/config.py)
app.config.from_object('sample_size.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/0.12/config/
app.config.from_envvar('SAMPLESIZE_SETTINGS', silent=True)

import sample_size.main  # noqa: E402  pylint: disable=wrong-import-position
import sample_size.api  # noqa: E402  pylint: disable=wrong-import-position
import sample_size.model  # noqa: E402  pylint: disable=wrong-import-position


if __name__ == "__main__":
    app.run()
