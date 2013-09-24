import numpy as np
import pprint
import matplotlib.pyplot as plt
dtp = [('frac_followed', 'f128'), ('frac_observed', 'f128')\
       ,('frac_obs_unc', 'f128')]
Eff = np.loadtxt('Efficiency.txt',dtype = dtp, skiprows=1)
Purity = np.loadtxt('Purity.txt',dtype = dtp, skiprows=2)

f0, [ax0,ax1] = plt.subplots(1,2)
ax0.plot(Eff['frac_followed'],Eff['frac_observed'], color = 'k')
ax0.plot(Eff['frac_followed'],Eff['frac_observed']+Eff['frac_obs_unc'], color = '0.55')
ax0.plot(Eff['frac_followed'],Eff['frac_observed']-Eff['frac_obs_unc'], color = '0.55')
ax0.fill_between(Eff['frac_followed'],Eff['frac_observed']-Eff['frac_obs_unc'],Eff['frac_observed']+Eff['frac_obs_unc'],color ='0.75' )
ax0.set_xlim(-0.04,1.04)
ax0.set_xlabel('Fraction of GRBs Followed Up')
ax0.set_ylabel('Fraction of high (z>4)GRBs observed')
ax0.set_title('Efficiecy')

ax1.plot(Purity['frac_followed'],Purity['frac_observed'], color = 'k')
ax1.plot(Purity['frac_followed'],Purity['frac_observed']+Purity['frac_obs_unc'], color = '0.55')
ax1.plot(Purity['frac_followed'],Purity['frac_observed']-Purity['frac_obs_unc'], color = '0.55')
ax1.fill_between(Purity['frac_followed'],Purity['frac_observed']-Purity['frac_obs_unc'],Purity['frac_observed']+Purity['frac_obs_unc'],color ='0.75' )
ax1.set_xlim(-0.04,1.04)
ax1.set_xlabel('Fraction of GRBs Followed Up')
ax1.set_ylabel('Fraction of high (z>4)GRBs observed')
ax1.set_title('Efficiecy')
plt.show()