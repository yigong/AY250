import pdb
import datetime
import json

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from numpy import nan as NaN

# Functions defined
def user_extract(dict_in):
	''' Extract 'login' key's value '''''
	return dict_in['login']

def count(resample_in):
	''' Count the number of samples in resampled data'''
	return len(resample_in)

def distinct_user(resample_in):
	''' Count the number of distinct user in resampled data'''
	unique_in = resample_in.drop_duplicates()
	return len(unique_in)

def mean_day(resample_in):
	''' Calculate the mean open day of an issue in resampled data'''
	try:
		#Create a Series has value equals to created_at
		created_at_series = pd.Series(
			resample_in.index, index=resample_in.index)
		diff = resample_in - created_at_series
		sec_mean = diff.sum()/float(len(diff))
		#Convert to timedelta object
		td = datetime.timedelta(microseconds=int(sec_mean/1000.))		
		#return day attribute of the time difference 
		return td.days 
	except Exception:
		return NaN

def comment_func(comment_list):
	''' Extract the comment string from the comments column'''
	try:
		return comment_list[0]['text']
	except Exception:
		return NaN

def chattiest_user(resample_se):
	''' Find the chattiest user in a month'''
	try:
		counts = resample_se.value_counts().order(ascending=True)
		return counts.index[0]
	except Exception:
		return NaN

def distinct(resample_se):
	''' Find the number of distinct user who comment on 'pandas' '''
	return len(resample_se.unique())

def percent(resample_se):
	''' Find the percentage of comments provided by the chattiest user'''
	try:
		counts = resample_se.value_counts().order(ascending=False)
		return int(counts.ix[0]/float(counts.sum())*100)
	except Exception:
		return NaN


# Read and load data
json_file = open('closed.json')
json_data = json.load(json_file)
all_data_df = pd.DataFrame(json_data)

###########
# part(1) #
###########

# p1 is the dataframe have title, created_at, labels, closed_at, user, \
# id as columns
p1 = all_data_df[['title', 'created_at', 'labels', 'closed_at',\
					'user', 'id']]
# transfer the user values to username string
p1.user = p1.user.map(user_extract)

###########
# part(2) #
###########

# Drop the duplicate rows using id inplace
p1.drop_duplicates(cols='id', inplace=True)

###########
# part(4) #
###########

# Convert created_at and closed_at columns from string to datetime
p1['created_at'] = pd.to_datetime(p1['created_at'])
p1['closed_at'] = pd.to_datetime(p1['closed_at'])

###########
# part(5) #
###########

# Set 'created_at' as index
p1.set_index('created_at', inplace=True)
# Make the monthly number of issue plot
issue_month = p1.title.resample('M', how=count)
issue_month.name = 'Number of Issues'
plt.figure()
issue_ax = issue_month.plot()
issue_ax.set_ylabel(issue_month.name)
# Make the monthly distinct user number plot
distinct_month = p1.user.resample('M', how=distinct_user)
distinct_month.name = 'Number of Distinct User'
plt.figure()
distinct_ax = distinct_month.plot()
distinct_ax.set_ylabel(distinct_month.name)

###########
# part(6) #
###########

# Resample the closed_at and return a series of mean open day
open_day = p1.closed_at.resample('M', how=mean_day)
open_day.name = 'Mean Open Day'
# Concatenate monthly issue number with mean open day
open_day = pd.concat([issue_month, open_day], axis=1)
open_day.columns = ['nIssues', 'mean_days']
plt.figure()
line1 = open_day['nIssues'].plot()
line1.set_ylabel('Number of issues')
plt.figure()
line2 = open_day['mean_days'].plot()
line2.set_ylabel('Mean Open Day')
open_day.to_pickle('mean_day.pkl')
print '_'*80
print open_day.head(20)

###########
# part(7) #
###########

# Create the comment dateframe
comm_df = all_data_df[['created_at', 'comments', 'id']]
comm_df.drop_duplicates(cols='id', inplace=True)
comm_df.comments = comm_df.comments.map(comment_func)
comm_df.created_at = pd.to_datetime(comm_df.created_at)
comm_df.set_index('created_at', inplace=True)
print '_'*80
print comm_df.head(20)
comm_df.to_pickle('comments.pkl')

###########
# part(8) #
###########

# Create user dataframe
user_df = all_data_df[['created_at', 'user', 'id']]
user_df.user = user_df.user.map(user_extract)
user_df.created_at = pd.to_datetime(user_df.created_at)
user_df.set_index('created_at', inplace=True)
user_se = user_df['user']
chattiest_df = user_se.resample('M', how=[count,chattiest_user,percent,distinct])
chattiest_df.columns = ['Number of comments', 'The chattiest', 'Percentage of the chattiest(%)',\
						'Number of participants']
print '_'*80						
print chattiest_df.head(20)
chattiest_df.to_pickle('chattiest.pkl')

###########
# part(9) #
###########

# Create id_label dataframe with create time as index
id_labels_temp = all_data_df[['id', 'labels', 'created_at']]
id_labels_temp.drop_duplicates(cols='id', inplace=True)
id_labels_list = []
for (idx,Id) in id_labels_temp.id.iteritems():
    if len(id_labels_temp.labels.ix[idx]):
        for label_dict in id_labels_temp.labels.ix[idx]:
            id_labels_list.append((Id, label_dict['name'], \
            					   id_labels_temp.created_at[idx]))
    else:
        id_labels_list.append((Id, np.nan,id_labels_temp.created_at[idx]))
id_labels_df = pd.DataFrame(id_labels_list, columns=['id', 'label', 'created_at'])
id_labels_df['created_at'] = pd.to_datetime(id_labels_temp['created_at'])
id_labels_df.set_index('created_at', inplace=True)

###########
# part(10) #
###########

# Add a column to the table in part(9) containing the number of days it took to
# close an issue
created = pd.Series(p1.index, index=p1.index)
closed = p1.closed_at
time_diff = closed - created
SEC_DAY = 24*60*60*1e9
open_day_per_issue = time_diff.map(lambda td: td/SEC_DAY)
open_day_per_issue.name = 'open_day'

# Merge the open_day dataframe onto the table created in (9)
label_open_df = pd.merge(id_labels_df.reset_index(), open_day_per_issue.reset_index(),\
		 on='created_at')
label_open_df.set_index('created_at', inplace=True)
bug_df = label_open_df.ix[label_open_df['label']=='Bug']
LABELS = label_open_df['label'].drop_duplicates().values[1:]
time_per_label = pd.DataFrame([])
for label_str in LABELS[:5]:
    temp = label_open_df.ix[label_open_df['label']==label_str]['open_day']
    label_month = temp.resample('M', how='mean')
    label_month.name = label_str
    time_per_label = time_per_label.join(label_month, how='outer')
print '_'*80						
print time_per_label.head()
time_per_label.to_pickle('time_label.pkl')


ax0 = time_per_label[['Bug', 'Enhancement']].plot()
ax0.set_ylabel('Number of issues')
ax0.legend()

# Show the plot
plt.show()














