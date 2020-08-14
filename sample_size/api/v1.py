"""REST API for v1."""
import flask
import sample_size


@sample_size.app.route('/api/v1/', methods=["GET"])
def get_v1():
    """Return list of services available."""
    context = {}
    context['available_services'] = {'sample_size': "/api/v1/sample_size"}
    return flask.jsonify(**context)


@sample_size.app.errorhandler(404)
def resource_not_found(e):
    return flask.jsonify(error=str(e)), 404
