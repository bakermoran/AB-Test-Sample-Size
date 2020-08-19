# AB Test Sample Size

A very simple website to host a calculator for a bayesian sample size estimate. This came about because we at Root switched from frequentist statistics to Bayesian statistics in order to gain many of the advantages that come with it for AB testing at a tech company. You can read more about why we use Bayesian statistics [here](https://github.com/bakermoran/BayesABTest/blob/master/docs/besyian_ab_testing/Bayesian_AB_Testing_explainer.md), but the gist of it is:

1. It allows us to explain results better
2. It allows us to avoid the goal of frequentist statistics, which is to avoid false positives
3. It allows us to test faster, because of point 2. We can go with the result that we believe is _not worse_, because the decision is not high stakes.

That is, it _would_ allow us to test fast, if we were not still using [this](https://www.evanmiller.org/ab-testing/sample-size.html) sample size calculator, backed by frequentist statistics. Working on a team that has very limited access to data volume, we _need_ to take advantage of this quality of Bayesian statistics. I therefore set out to make my own sample size calculator in order to justify a smaller sample size.

Hosted with Heroku at <https://ab-test-sample-size-backend.herokuapp.com/>
