import numpy as np
import pandas as pd
from numpy import sqrt
from random import uniform
from time import time
import multiprocessing
import matplotlib.pyplot as plt
#%matplotlib
number_of_darts = np.logspace(2,6,10)
number_of_darts = [int(number_of_darts[i]) for i in range(len(number_of_darts))]

def pi_approx_serial(number_of_darts):
    ''' approximate pi using serial method'''
    number_of_darts_in_circle = 0
    start_time = time()
    for n in xrange(number_of_darts):
        x = uniform(0,1)
        y = uniform(0,1)
        distance = np.sqrt((x-0.5)**2+(y-0.5)**2)
        if distance <= 0.5:
            number_of_darts_in_circle += 1
        else:
            pass
    end_time = time()
    execution_time = end_time - start_time
    pi_apx = 4*number_of_darts_in_circle/float(number_of_darts)
    return [execution_time, pi_apx]
time_serial = []
for dart in number_of_darts:
    time_temp = pi_approx_serial(dart)
    time_temp.insert(0, dart)
    time_temp.append(dart/time_temp[1])
    time_serial.append(time_temp)


def pi_approx(number_of_darts):
    ''' approximate pi using MC method'''
    number_of_darts_in_circle = 0
    for n in xrange(number_of_darts):
        x = uniform(0,1)
        y = uniform(0,1)
        distance = sqrt((x-0.5)**2+(y-0.5)**2)
        if distance <= 0.5:
            number_of_darts_in_circle += 1
        else:
            pass
    return 4*number_of_darts_in_circle/float(number_of_darts)

from IPython import parallel
rc = parallel.Client()
dview = rc[:]
with dview.sync_imports():
    from numpy import sqrt
    from random import uniform
    from time import time

def pi_approx_par(number_of_darts):
    ''' approximate pi using parallel method '''
    number_of_darts_per_thread = number_of_darts/len(dview)
    start_time = time()
    d_result = dview.apply_async(pi_approx, number_of_darts_per_thread)
    result = d_result.get()
    end_time = time()
    execution_time = end_time - start_time
    pi_apx = np.mean(result)
    return [execution_time, pi_apx]
time_Ipar = []
for dart in number_of_darts:
    time_temp = pi_approx_par(dart)
    time_temp.insert(0, dart)
    time_temp.append(dart/time_temp[1])
    time_Ipar.append(time_temp)


def pi_approx_stdlib(number_of_darts):
    if __name__ == '__main__':
        nCPU = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes=nCPU)
        start_time = time()
        number_of_darts_per_thread = number_of_darts/nCPU
        argu_list = [number_of_darts_per_thread] * nCPU
        pi_apx = pool.map_async(pi_approx, argu_list).get()
        pi_apx = np.mean(pi_apx)
        end_time = time()
        execution_time = end_time-start_time
        pool.terminate()
        return [execution_time, pi_apx]
time_stdlib = []
for dart in number_of_darts:
    time_temp = pi_approx_stdlib(dart)
    time_temp.insert(0, dart)
    time_temp.append(dart/time_temp[1])
    time_stdlib.append(time_temp)

def to_DataFrame(data_list):
    '''
        convert list to pandas DataFrame
        time is in second
        the unit of simu_rate is [# per us]
    '''
    data_df = pd.DataFrame(data_list, columns=['nDarts', 'time', 'pi_approx', 'simu_rate'])
    data_df.set_index('nDarts', inplace=True)
    return data_df

serial_df = to_DataFrame(time_serial)
Ipar_df = to_DataFrame(time_Ipar)
stdlib_df = to_DataFrame(time_stdlib)

fig, axes = plt.subplots()
serial_df.time.plot(style='r-', label='Simple')
serial_df.simu_rate.plot(secondary_y=True, style='r--')
Ipar_df.time.plot(style='g-', label='Ipcluster')
Ipar_df.simu_rate.plot(secondary_y=True, style='g--')
stdlib_df.time.plot(style='c-', label='Multiprocessing')
stdlib_df.simu_rate.plot(secondary_y=True, style='c--')
axes.set_xlabel('Darts Thrown')
axes.set_ylabel('Execution Time(seconds), solid line')
axes.set_xscale('log')
axes.set_yscale('log')
axes.right_ax.set_yscale('log')
axes.right_ax.set_ylabel('Simulation Rate (darts/seconds), dashed line')
axes.legend(loc='best')
axes.set_title('MacBook Pro with 2.4GHZ Intel Core 2 Duo', size='large')
plt.show()