#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from utilities import PathsUtilities as putil

# Two modules, one for each considered dataset
from utilities import TuhUtilities as tuh
from utilities import IcareUtilities as icare

script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 1:
    print('Executing script ' + script_name + ' on the HPC as ' + sys.argv[1])
else:
    print('Executing script ' + script_name + ' on local machine')
        

paths = putil.get_paths()

# TUH example, we read eeg data of the first recording available
tuh_patients = tuh.list_patients(paths.tuh)
for pp, patient_id in enumerate(tuh_patients):
    if pp == 0:
        recording_ids = tuh.list_recordings(paths.tuh, patient_id)
        for rr, recording_id in enumerate(recording_ids):
            if rr == 0:  # just first recording as example
                eeg, info = tuh.read_eeg(paths.tuh, recording_id)              
                print('Read TUH data succesfully.')
                

# icare example, we read eeg data of the first recording available
# as well as age, outcome and cpc of the patient
icare_patients = icare.list_patients(paths.icare)
for pp, patient_id in enumerate(icare_patients):
    if pp == 0:
        age           = icare.age(paths.icare, patient_id)
        outcome       = icare.outcome(paths.icare, patient_id)
        cpc           = icare.outcome(paths.icare, patient_id)
        recording_ids = icare.list_recordings(paths.icare, patient_id)
        for rr, recording_id in enumerate(recording_ids):
            if rr == 0:  # just first recording as example
                eeg, info = icare.read_eeg(paths.icare, recording_id)
                print('Read icare data succesfully.')
