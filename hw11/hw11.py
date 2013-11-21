import numpy as np 
import pandas as pd 
import pymc 
from sympy import *
from pymc import Matplot
import matplotlib.pyplot as plt

april_df = pd.read_csv('./hw_11_data/laa_2011_april.txt', sep='\t')
year_df = pd.read_csv('./hw_11_data/laa_2011_full.txt', sep='\t')

## part(a)
# April
april_df.set_index('Player', inplace=True)
MLE_april_se = april_df['H']/(april_df['AB'].astype(float))
MLE_april_se.name = 'MLE_april'
# Full year
year_df.set_index('Player', inplace=True)
MLE_year_se = year_df['H']/(year_df['AB'].astype(float))
MLE_year_se.name = 'MLE_year'

print 'Maximum likelihood estimation of batting average for each player from April data.'
print MLE_april_se
## part(b)
a, b = symbols('a b')
init_printing(use_unicode=True)
solu = solve([a/(a+b)-0.225, a*b/((a+b)**2*(a+b+1))-0.0011],[a,b])
alpha, beta = solu[1]
alpha = float(alpha)
beta = float(beta)
mcmc_dict = dict()
for i in range(len(MLE_april_se)):	
	player_se = april_df.ix[i,:]

	
	mu = pymc.Beta('mu', alpha, beta)
	xs = pymc.Binomial('xs', n=player_se['AB'], p=mu, value=player_se['H'], observed=True)
	mcmc_dict['mu'+str(i)] = pymc.MCMC([mu, xs])
	mcmc_dict['mu'+str(i)].sample(iter=4000, thin=2)

print '\t'
Matplot.plot(mcmc_dict['mu0'])
Matplot.plot(mcmc_dict['mu1'])
Matplot.plot(mcmc_dict['mu2'])
fall_in = 0
result_df = pd.concat([MLE_april_se, MLE_year_se], axis=1)
mean_post_list = []
ll_list = []
ul_list = []
in_list = []
for i, mui in enumerate(mcmc_dict.values()):
	
	mean_post = mui.stats()['mu']['mean']
	mean_post_list.append(mean_post)

	ll, ul = mui.stats()['mu']['95% HPD interval']
	ll_list.append(ll)
	ul_list.append(ul)
	
	player_name = MLE_april_se.index[i]
	print '-'*50
	print 'Player : ' + player_name
	print 'Posterior mean : ' + str(mean_post)
	print 'Posterior 95% CI : (' + str(ll) + ', ' + str(ul) + ')'
	
	mean_year = MLE_year_se[player_name]
	if (mean_year > ll) & (mean_year < ul):
		print 'Full season batting average fall within 95% CI predicted by the first month!'
		in_list.append(True)
		fall_in += 1
	else:
		print 'Full season falls out of 95% CI'
		in_list.append(False)
print '-'*50
print str(fall_in) + ' out of ' + str(len(MLE_year_se)) + ' fall into 95% CI'

mean_post_se = pd.Series(mean_post_list, index=MLE_april_se.index, name='mean_post' )
ll_se = pd.Series(ll_list, index=MLE_april_se.index, name='lower')
ul_se = pd.Series(ul_list, index=MLE_april_se.index, name='upper')
in_se = pd.Series(in_list, index=MLE_april_se.index, name='in 95%')
result_df = pd.concat([MLE_april_se, MLE_year_se, mean_post_se, ll_se, ul_se, in_se], axis=1)
print result_df

fig1, ax1 = plt.subplots()
ax1.plot(result_df['MLE_april'], result_df['MLE_year'], 'ro')
ax1.set_xlabel('MLE from April data', fontsize='x-large')
ax1.set_ylabel('Full-season batting average', fontsize='x-large')
ax1.set_xlim(0, 0.5)
ax1.set_ylim(0, 0.5)

fig2, ax2 = plt.subplots()
x_err_ll = result_df['mean_post'] -result_df['lower']
x_err_ul = result_df['upper'] - result_df['mean_post']
ax2.errorbar(result_df['mean_post'], result_df['MLE_year'], xerr=[x_err_ll, x_err_ul], fmt='o')
ax2.set_xlabel('posterier mean with 95% CI', fontsize='x-large')
ax2.set_ylabel('Full-season batting average', fontsize='x-large')
ax2.set_xlim(0, 0.5)
ax2.set_ylim(0, 0.5)

plt.show()

# mus = dict()
# xs = dict()
# for i in np.range(len(MLE_april_se)):
# 	mus['mu'+str(i)] = pymc.
# 	xs['x'+str(i)] = 
