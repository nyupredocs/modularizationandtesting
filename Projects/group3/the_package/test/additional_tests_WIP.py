"""
# Checks for collinearity
#VIF: statsmodels.stats.outliers_influence.variance_inflation_factor (if vif > & vif < 10, likely collin)
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
import numpy as np
X = pd.DataFrame(np.random.rand(100,10))
N = np.size(X,0)
K = np.size(X,1)
# For each X, calculate VIF and save in dataframe
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["Column Index"] = list(range(X.shape[1]))
vifLikelyCollinear = vif.loc[(vif['VIF Factor']>10)]
try:
    vifLikelyCollinear.size
    print("X is not collinear")
except:
        print("Error: Likely collinear predictors identified (VIF > 10).")
        print("|--------------Predictors listed by index:--------------|")
        s = ""
        for row in vifLikelyCollinear:
            print(s.join(map(str,row)))
# Check if covar matrix of predictors is ill-conditioned
# {N/K, K/N} > 0.95 (Marcenko-Pastur Law)
r1 = N/K
r2 = K/N
try:
    assert r1>0.95 | r2>0.95
except:
    print("Error: Covariance matrix of covariates is ill-conditioned.")
    print("Note that N/K = {} K/N = {}.".format(r1, r2))
"""