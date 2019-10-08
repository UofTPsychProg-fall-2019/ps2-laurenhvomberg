#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
#
testingrooms = ['A','B','C']
for room in testingrooms:
...


#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#
data = np.empty((0,5))
for room in testingrooms:
...


#%%
# calculate overall average accuracy and average median RT
#
acc_avg = ...   # 91.48%
mrt_avg = ...   # 477.3ms


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#
...

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms


#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
acc_wp = ...  # 94.0%
acc_bp = ...  # 88.9%
mrt_wp = ...  # 469.6ms
mrt_bp = ...  # 485.1ms


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
...

# words - white/pleasant: 478.4ms
# words - black/pleasant: 500.3ms
# faces - white/pleasant: 460.8ms
# faces - black/pleasant: 469.9ms


#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats
...

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:23:01 2019

@author: laurenvomberg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
#
testingrooms = ['A','B','C']


for room in testingrooms:
    path_testingroom = 'testingroom' + room + '/experiment_data.csv'
    path_rawdata = 'rawdata/experiment_data_' + room + '.csv'
    shutil.copy(path_testingroom ,path_rawdata)


#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#
data = np.empty((0,5))
for room in testingrooms:
    new_path = 'rawdata/experiment_data_' + room + '.csv'
    tmp = sp.loadtxt(new_path, delimiter=',')
    data = np.vstack([data,tmp])


#%%
# calculate overall average accuracy and average median RT

acc_list = []
for element in range(92):
    acc_list.append(data[element][3])
    #only want data in element 3 (accuracy)
    
    
acc_avg = np.mean(acc_list)*100   # 91.48%

mrt_list = []
for element in range(92):
    mrt_list.append(data[element][4])
    #only want data from element 4 (rt)

mrt_avg = np.median(mrt_list)   # 477.3ms


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#
w_acc = []
w_rt = []
f_acc = []
f_rt = []

av_list = []
for element in range(92):
    stim = int(data[element][1])
    if stim == 1:
        w_acc.append(data[element][3])
        w_rt.append(data[element][4])
    else:
        f_acc.append(data[element][3])
        f_rt.append(data[element][4])

# words: 88.6%, 489.4ms
w_acc_av = np.mean(w_acc)*100
w_rt_av = np.mean(w_rt)

#faces: 94.4%, 465.3ms
f_acc_av = np.mean(f_acc)*100
f_rt_av = np.mean(f_rt)

#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#

acc_wp_list = []
acc_bp_list = []
mrt_wp_list = []
mrt_bp_list = []

av_list = []
for element in range(92):
    stim = int(data[element][2])
    if stim == 1:
        acc_wp_list.append(data[element][3])
        mrt_wp_list.append(data[element][4])
    else:
        acc_bp_list.append(data[element][3])
        mrt_bp_list.append(data[element][4])


acc_wp = np.mean(acc_wp_list)*100  # 94.0%
acc_bp = np.mean(acc_bp_list)*100  # 88.9%
mrt_wp = np.mean(mrt_wp_list)  # 469.6ms
mrt_bp = np.mean(mrt_bp_list)  # 485.1ms


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
w_w_p = []
w_b_p = []
f_w_p = []
f_b_p = []

avg_list = []
for element in range(92):
    stim = int(data[element][1])
    pairing = int(data[element][2])
    if stim == 1 and pairing == 1:
        w_w_p.append(data[element][4])
        #f_w_p.append(data[element][4])
    elif stim == 1 and pairing == 2:
        w_b_p.append(data[element][4])
        #f_b_p.append(data[element][4])
    elif stim ==2 and pairing == 1:
        f_w_p.append(data[element][4])
    elif stim == 2 and pairing == 2:
        f_b_p.append(data[element][4])

av_w_w_p = np.mean(w_w_p)
av_w_b_p = np.mean(w_b_p)
av_f_w_p = np.mean(f_w_p)
av_f_b_p = np.mean(f_b_p)



# words - white/pleasant: 478.4ms
# words - black/pleasant: 500.3ms
# faces - white/pleasant: 460.8ms
# faces - black/pleasant: 469.9ms


#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats

test_words = scipy.stats.ttest_rel(w_w_p, w_b_p)

test_faces = scipy.stats.ttest_rel(f_w_p, f_b_p)

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(acc_avg,mrt_avg))
print('\n Word acc and rt averages: {:.2f}%, {:.1f} ms'.format(w_acc_av, w_rt_av))
print('\n Faces acc and rt averages: {:.2f}%, {:.1f} ms'.format(f_acc_av, f_rt_av))
print('\n average rt for WORDS for white p and black p: {:.2f} ms, {:.1f} ms'.format(av_w_w_p, av_w_b_p))
print('\n average rt for FACES for white p and black p: {:.2f} ms, {:.1f} ms'.format(av_f_w_p, av_f_b_p))
print('\n average acc for white p and black p: {:.2f}%, {:.1f}% '.format(acc_wp, acc_bp))

print('\n t-test words: %.2f, %.7f '% (test_words))
print('\n t-test words: %.2f, %.7f '% (test_faces))
#print('\n average acc for white p and black p: {:.2f}, {:.7f} '.format(test_faces))
#print('\n T-test faces: {:.2f}%, {:.1f} ms'.format(test_faces))
#print('\n T-test words: {:.2f}%, {:.1f} ms'.format(test_words))

