import numpy as np
import pprint
import matplotlib.pyplot as plt
dtp = [('frac_followed', 'f128'), ('frac_observed', 'f128')\
       ,('frac_obs_unc', 'f128')]
Eff = np.loadtxt('Efficiency.txt',dtype = dtp, skiprows=1)
Purity = np.loadtxt('Purity.txt',dtype = dtp, skiprows=2)

f0, [ax0,ax1] = plt.subplots(1,2, figsize = (10,6) )
ax0.plot(Eff['frac_followed'],Eff['frac_observed'], color = 'k')
ax0.plot(Eff['frac_followed'],Eff['frac_observed']+Eff['frac_obs_unc'], color = '0.55')
ax0.plot(Eff['frac_followed'],Eff['frac_observed']-Eff['frac_obs_unc'], color = '0.55')
ax0.fill_between(Eff['frac_followed'],Eff['frac_observed']-Eff['frac_obs_unc'],Eff['frac_observed']+Eff['frac_obs_unc'],color ='0.75' )
ax0.set_xlim(-0.04,1.04)
ax0.set_xlabel('Fraction of GRBs Followed Up')
ax0.set_ylim(-0.04,1.04)
ax0.set_ylabel('Fraction of high (z>4)GRBs observed')
ax0.set_title('Efficiecy', fontdict=dict(size = 16))
ax0.set_aspect('equal')
ax0.annotate('Follow up 20% of\n bursts to capture ~55%\n of high-z events', xy = (0.2,0.55), \
             xytext = (0.43,0.15),arrowprops=dict(facecolor='black', width=0.8,\
             headwidth=7, shrink=0.08))
xRand = np.linspace(0,1,11)
yRand = xRand
ax0.plot(xRand,yRand,color = 'k')
x_20 = np.ones(11)*0.2
y_20 = np.linspace(0,0.55,11)
ax0.plot(x_20,y_20, color = 'k', linestyle = 'dotted', linewidth = 2)

ax0.annotate('Random \nguessing', xy = (0.8,0.8), xytext = (0.7,0.4), \
             arrowprops= dict(facecolor = 'black', width = 1.2,headwidth=7, shrink=0.08))




ax1.plot(Purity['frac_followed'],Purity['frac_observed'], color = 'k')
ax1.plot(Purity['frac_followed'],Purity['frac_observed']+Purity['frac_obs_unc'], color = '0.55')
ax1.plot(Purity['frac_followed'],Purity['frac_observed']-Purity['frac_obs_unc'], color = '0.55')
ax1.fill_between(Purity['frac_followed'],Purity['frac_observed']-Purity['frac_obs_unc'],Purity['frac_observed']+Purity['frac_obs_unc'],color ='0.75' )
ax1.set_xlim(-0.04,1.04)
ax1.set_xlabel('Fraction of GRBs Followed Up')
ax1.set_ylim(-0.04,1.04)
ax1.set_ylabel('Fraction of high (z>4)GRBs observed')
ax1.set_title('Purity', fontdict=dict(size = 16))
ax1.set_aspect('equal')
x_20_2 = np.ones(11)*0.2
y_20_2 = np.linspace(0,0.38,11)
ax1.plot(x_20_2, y_20_2, color = 'k', linestyle = 'dotted', linewidth = 2)
ax1.annotate('If 20% of events are\n followed up, ~40% of\n them will be high-z',\
             xy = (0.2, 0.4), xytext = (0,0.76), \
             arrowprops = dict(facecolor = 'black', width = 1.2,headwidth=7, shrink=0.08))
xRand_2 = np.linspace(0,1,11)
yRand_2 = np.ones(11)*18.0/135.0
ax1.plot(xRand_2,yRand_2,color = 'k')
ax1.annotate('Random\n guessing',xy = (0.6,0.133), xytext = (0.65,0.45),\
             arrowprops = dict(facecolor = 'black', width = 1.2,headwidth=7, shrink=0.08))
plt.show()