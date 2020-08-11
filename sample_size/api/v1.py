"""REST API for v1."""
import flask
import sample_size


@sample_size.app.route('/api/v1/', methods=["GET"])
def get_v1():
    """Return list of services available."""

    return flask.jsonify({'sample_size': "/api/v1/sample_size"})
