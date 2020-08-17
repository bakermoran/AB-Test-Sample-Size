"""REST API for sample size calcs."""
import flask
import sample_size
from ._utils import _sample_size_fixed_loss_tolerance


@sample_size.app.route('/api/v1/sample_size/', methods=["GET"])
def get_sample_size():
    """Get sample size estimate for parameters"""

    context = {}
    loss_tolerance = flask.request.args.get('loss_tolerance',
                                            default=.02, type=float)
    code = 200
    if flask.request.args.get('baseline_conversion_rate') is None:
        code = 400
        context['response_code'] = 400
        context['message'] = 'baseline_conversion_rate is a required argument'
    elif flask.request.args.get('expected_relative_lift') is None:
        code = 400
        context['response_code'] = 400
        context['message'] = 'expected_relative_lift is a required argument'
    elif loss_tolerance < .001:
        code = 400
        context['response_code'] = 400
        context['message'] = 'loss_tolerance must be greater than .001'
    else:
        baseline_conversion_rate = flask.request.args.get(
                                        'baseline_conversion_rate', type=float)
        expected_relative_lift = flask.request.args.get(
                                          'expected_relative_lift', type=float)
        loss_tolerance = flask.request.args.get('loss_tolerance',
                                                default=.02, type=float)
        prior_alpha = flask.request.args.get('prior_alpha',
                                             default=1, type=int)
        prior_beta = flask.request.args.get('prior_beta', default=1, type=int)

        results = _sample_size_fixed_loss_tolerance(
                             baseline_conversion_rate=baseline_conversion_rate,
                             expected_relative_lift=expected_relative_lift,
                             loss_tolerance=loss_tolerance,
                             prior_alpha=prior_alpha,
                             prior_beta=prior_beta)

        context['url'] = flask.request.path
        inputs = {}
        inputs['baseline_conversion_rate'] = baseline_conversion_rate
        inputs['expected_relative_lift'] = expected_relative_lift
        inputs['loss_tolerance'] = loss_tolerance
        inputs['prior_alpha'] = prior_alpha
        inputs['prior_beta'] = prior_beta
        context['inputs'] = inputs
        context['outputs'] = results

    return flask.jsonify(**context), code
