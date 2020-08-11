"""main route."""
import sample_size
import flask


@sample_size.app.route('/', methods=["GET"])
def home_view():
    """Return home route."""

    return 'head to <a href="{0}api/v1">{0}</a>'.format(flask.request.url_root)
