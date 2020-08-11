"""
sample_size index (main) view.

URLs include:
/
"""

import uuid
import flask
import arrow
import sample_size


@sample_size.app.route('/', methods=['GET'])
def show_index():
    """Display / route."""

    return flask.render_template("index.html")
