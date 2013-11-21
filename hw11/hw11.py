import numpy as np 
import pandas as pd 
import pymc 
from sympy import *
april_df = pd.read_csv('./hw_11_data/laa_2011_april.txt', sep='\t')
## part(a)
april_df.set_index('Player', inplace=True)
MLE_april_se = april_df['H']/(april_df['AB'].astype(float))
MLE_april_se.name = 'MLE'
print MLE_april_se
## part(b)
for i in range(1):	
	player_se = april_df.ix[i,:]
	a, b = symbols('a b')
	init_printing(use_unicode=True)
	solu = solve([a/(a+b)-0.225, a*b/((a+b)**2*(a+b+1))-0.0011],[a,b])
	alpha, beta = solu[1]
	alpha = float(alpha)
	beta = float(beta)
	with pymc.Model() as model:
		mu = pymc.Beta('mu', alpha, beta)
		xs = pymc.Binomial('xs', n=player_se['AB'], p=mu, value=player_se['H'], observed=True)
		xs.sample(1000)



# mus = dict()
# xs = dict()
# for i in np.range(len(MLE_april_se)):
# 	mus['mu'+str(i)] = pymc.
# 	xs['x'+str(i)] = 
