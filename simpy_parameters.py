# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 04:01:24 2017

@author: Afonso
"""

# Constants and global variables

REFERRAL_TYPES = ['AR', 'CR', 'FTA', 'CF', 'OTR']
FMT_TYPES = ['1to1', '1toWL', '1toM']
TRIAGE_TYPES = FMT_TYPES + ['free']

ACQ_MEAN = 1.0
SAMPLES_NUMBER = 100
NUM_STATIONS = 1
DAYS = 365
RANDOM_SEED = 1000
PT_MEAN = 1.0
PT_SIGMA = 0.1
MATCH_MEAN = 0.0
CALL_MEAN = 1.0
JOB_DURATION = 0.0
EXPERT_DAY_OFF = 0
EXAMINER_DAY_OFF = 0
T1_INSPECTION_MEAN = 1.0
T1_INSPECTION_SIGMA = 0.1
T2_INSPECTION_MEAN = 1.0
T2_INSPECTION_SIGMA = 0.1
NUM_EXAMINERS = 10
COST_EXAMINER = 1
SHIFT_EXAMINER = 24
NUM_EXPERTS = 10
COST_EXPERT = 1
SHIFT_EXPERT = 24
SIM_TIME = 1
SCORE_MIN = -10
SCORE_MAX = 10
SAMPLES_NUMBER = 100
NUM_STATIONS = 1
DAYS = [1,2,3,4,5,6,7]
EXPERT_DAY_OFF = []
EXAMINER_DAY_OFF = []
SHIFT_EXPERT_ST = 0
SHIFT_EXAMINER_ST = 0
NUM_DAYS = 1
NUM_REP = 1
MEAN_ESCALATION_RATE = 1.0
FMT_TIME = (1, 0.1)