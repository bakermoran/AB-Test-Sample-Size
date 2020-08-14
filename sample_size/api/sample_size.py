"""REST API for sample size calcs."""
import flask
import sample_size
import numpy as np
import scipy.special as sc
# pylint: disable=no-member


def _probability_B_beats_A(a_A, b_A, a_B, b_B):
    """Calculate the probablty that a Beta distributions is greater.

    Arguments:
        a_A {int} -- Beta_A alpha param
        b_A {int} -- Beta_A beta param
        a_B {int} -- Beta_B alpha param
        b_B {int} -- Beta_B beta param

    Returns:
        float -- probabilty that Beta_B(a_B, b_B) is greater
          than Beta_A(a_A, b_A)
    """
    sum = 0
    for i in range(0, a_B-1):
        sum += np.exp(sc.betaln(a_A+i, b_B+b_A) -
                      np.log(b_B+i) -
                      sc.betaln(1+i, b_B) -
                      sc.betaln(a_A, b_A)
                      )
    return sum


def _loss_choose_B_over_A(a_A, b_A, a_B, b_B):
    """Calc loss function value of two dists Beta_A(a_A, b_B) and Beta_B(a_B, b_B).

    Arguments:
        a_A {int} -- Beta_A alpha param
        b_A {int} -- Beta_A beta param
        a_B {int} -- Beta_B alpha param
        b_B {int} -- Beta_B beta param

    Returns:
        float -- the loss function value for Beta_B over Beta_A
    """
    x1 = sc.betaln(a_A + 1, b_A)
    y1 = np.log(1 - _probability_B_beats_A(a_A + 1, b_A, a_B, b_B))
    z1 = sc.betaln(a_A, b_A)

    x2 = sc.betaln(a_B + 1, b_B)
    y2 = np.log(1 - _probability_B_beats_A(a_A, b_A, a_B + 1, b_B))
    z2 = sc.betaln(a_B, b_B)

    return np.exp(x1 + y1 - z1) - np.exp(x2 + y2 - z2)


def _sample_size_fixed_loss_tolerance(baseline_conversion_rate,
                                      expected_relative_lift,
                                      loss_tolerance=0.05,
                                      prior_alpha=1,
                                      prior_beta=1):

    if expected_relative_lift <= 0:
        raise ValueError('expected_relative_lift must be greater than 0')

    variant_conversion_rate = baseline_conversion_rate * (
                               1 + expected_relative_lift)

    epsilon = baseline_conversion_rate - baseline_conversion_rate * (
              1 - loss_tolerance)

    B_risk = float('inf')
    base_sample = 10

    while B_risk > epsilon:
        control_alpha_likelihood = int(round(base_sample *
                                             baseline_conversion_rate, 0))
        control_beta_likelihood = int(round(base_sample *
                                            (1 - baseline_conversion_rate), 0))
        variant_alpha_likelihood = int(round(base_sample *
                                             variant_conversion_rate, 0))
        variant_beta_likelihood = int(round(base_sample *
                                            (1 - variant_conversion_rate), 0))
        a = control_alpha_likelihood + prior_alpha
        b = control_beta_likelihood + prior_beta
        c = variant_alpha_likelihood + prior_alpha
        d = variant_beta_likelihood + prior_beta

        B_risk = _loss_choose_B_over_A(a, b, c, d)
        confidence = _probability_B_beats_A(a, b, c, d)
        base_sample += 10

    context = {}
    context['loss_value'] = _loss_choose_B_over_A(a, b, c, d)
    context['probability_B_over_A'] = confidence
    context['sample_size_per_variant'] = base_sample

    return context


@sample_size.app.route('/api/v1/sample_size/', methods=["GET"])
def get_sample_size():
    """Get sample size estimate for parameters"""

    context = {}
    code = 200
    if flask.request.args.get('baseline_conversion_rate') is None:
        code = 404
        context['response_code'] = 404
        context['message'] = 'baseline_conversion_rate is a required argument'
    elif flask.request.args.get('expected_relative_lift') is None:
        code = 404
        context['response_code'] = 404
        context['message'] = 'expected_relative_lift is a required argument'
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
