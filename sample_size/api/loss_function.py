"""REST API for sample size calcs."""
import flask
import sample_size
from ._utils import _loss_choose_B_over_A
from ._utils import _probability_B_beats_A


@sample_size.app.route('/api/v1/loss_function/', methods=["GET"])
def get_loss_function():
    """Get loss_function value for each variant"""

    context = {}
    a_A = flask.request.args.get('alpha_A', type=int)
    b_A = flask.request.args.get('beta_A', type=int)
    a_B = flask.request.args.get('alpha_B', type=int)
    b_B = flask.request.args.get('beta_B', type=int)

    code = 200
    if a_A is None or b_A is None or a_B is None or b_B is None:
        code = 400
        context['response_code'] = 400
        context['message'] = ('alpha_A, beta_A, alpha_B, and beta_B are '
                              'all required parameters')
    else:
        results = {}
        results['choose_variant_A'] = _loss_choose_B_over_A(a_B, b_B, a_A, b_A)
        results['choose_variant_B'] = _loss_choose_B_over_A(a_A, b_A, a_B, b_B)

        results['probability_A_greater_than_B'] = _probability_B_beats_A(a_B,
                                                                         b_B,
                                                                         a_A,
                                                                         b_A)
        results['probability_B_greater_than_A'] = _probability_B_beats_A(a_A,
                                                                         b_A,
                                                                         a_B,
                                                                         b_B)

        context['url'] = flask.request.path
        inputs = {}
        inputs['alpha_A'] = a_A
        inputs['beta_A'] = b_A
        inputs['alpha_B'] = a_B
        inputs['beta_B'] = b_B
        context['inputs'] = inputs
        context['outputs'] = results

    return flask.jsonify(**context), code
