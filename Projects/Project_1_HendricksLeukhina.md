# How risky is college investment? (Hendricks Leukhina 2017)

This project is meant to highlight the importance of packaging your code nicely so that
others can build upon your work. In my own research, I benefited that the authors of this
paper provided their code and data in a relatively usable format. We hope that after the
next few days of instruction, you will be prepared to do an even better job at packaging
your research in an easily replicable and repeatable format.

We have written two versions of a Python package that contains the code needed to
replicate section 2 of their paper. You will be split into groups and asked to explore
some of the implications of their model using this code.


## Simple model of college credit accumulation

In this paper, the authors are interested in "quantifying the the relative importance
of heterogeneity and uncertainty for college dropout decisions." One of their innovations
beyond what previous work has done is they have a more explicit model of college
enrollment, credit accumulation, and dropout decisions.

Prior to presenting their full model, the authors use a simple model that only speaks
to credit accumulation to motivate some of the modeling decisions they make in later
sections of the paper.

We describe a single individual's problem.

The individual begins as a college freshman. They begin their college career at $t=1$
with 0 college credits, $n_0 = 0$. The student draws an ability level, $a \sim N(0, 1)$,
and a noisy signal of that ability given by $\text{GPA} = a + \varepsilon$ where
$\varepsilon \sim N(0, \sigma_\varepsilon^2)$.

Each year, a student attempts to complete $n_{courses} = 12$ that are each worth
$n_{credits} = 3$. The probability that a student successfully passes any given course
is given by
$p(a) = \gamma_\{\text{min}} + \frac{1 - \gamma_{\text{min}}}{1 + \gamma_1 \exp^{-\gamma_2 a}}$.

A student is awarded a degree once they have completed 42 courses (accumulated more than
125 credits). If a student fails to collect a degree after 6 years, they drop out of
college.

The authors use data from a proprietary microdata from the High School and Beyond survey
administered by the National Center for Education Statistics (NCES) which includes
information on a student's HS GPA, college transcript information, and financial
resources.


## Exploration

The code that replicates the outcomes from Hendricks Leukhina can be found on Github at
\url{https://www.github.com/cc7768/hrici_hl_2017}. If you were assigned to an odd numbered
group, then you should work off of the `group_odd` branch and if you were assigned to an
even numbered group, then you should off of the `group_even` branch.

1. An alternative model to the one described above is that all students have the same
   probability, $p$, of passing each class. Hendricks Leukhina argue against such a model
   because one of the key features of the transcript data is that there is a significant
   amount of dispersion in the number of credits accumulated.  Create a bar plot of the
   deciles of credits earned for years 1 and 2 with the "common probability model,"
   "heterogeneous probability model," and from the data.
2. Imagine that you have a technology that can raise the passing probability by 5\% for
   students within a particular GPA quartile, but you can only use it to improve the
   passing rate of one quartile. If you'd like to increase the overall graduation rate
   as much as possible, which quartile do you apply the technology to?

