# Build your own package

In this exercise, you will use what you learned today to create your own package. We
expect that the package will be cleanly written code, well-documented (with a readthedocs
page), and downloadable via pip (through test PyPI).

Your package should implement (at least) one statistical method.

We'd like you to keep it relatively simple. We have some options for you to choose from
below along with datasets that they could be applied to. You are welcome to choose your
own method, but you will also need to find at least one dataset that it can be used
for -- Additionally, you'll need to submit a PR to this repository to add the method
and dataset to the table below.

Updated requirements:

* Basic statistical model that can generate estimates, standard errors, and confidence intervals
* Preferably quite simple
* Two models (maybe one is OLS/one depends on optimization to fit)


| Method                                               | Potential datasets                                                     |
| :--------------------------------------------------- | :--------------------------------------------------------------------- |
| Instrumental variables (IV)                          | [Cornwell Rupert 1988](./data/CornwellRupert_1988.md),                 |
| Fixed effects (FE)                                   | [Cornwell Rupert 1988](./data/CornwellRupert_1988.md),                 |
| Random effects (RE)                                  |                                                                        |
| Zero-inflated regression (zip)                       |                                                                        |
| Multinomial logit                                    | [Hensher Greene 2007](./data/HensherGreen_2007.md)                     |
| Autoregressive integrated moving average (ARIMA)     |                                                                        |
| Autoregressive conditional heteroskedasticity (ARCH) |                                                                        |

