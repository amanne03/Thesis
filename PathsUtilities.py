"""PathsUtilities"""

import os
import getpass
import shutil
from pathlib import Path
from collections import namedtuple


def get_paths():
    user_name = getpass.getuser()

    # For B. Cauchi on local machine and on HPC:
    if user_name == 'benjamincauchi':
        # bCauchi on MacBook
        data    = "/Users/benjamincauchi/Student_Theses/Manne_2025_Master/data"
        models  = "/Users/benjamincauchi/Student_Theses/Manne_2025_Master/python/models"
        output  = "/Users/benjamincauchi/Student_Theses/Manne_2025_Master/python/output"
        tmp     = "/Users/benjamincauchi/Student_Theses/Manne_2025_Master/python/tmp"
        thesis  = "/Users/benjamincauchi/Student_Theses/Manne_2025_Master/thesis"
    elif user_name == 'mimo4729':
        # mimo4729 on HPC
        data   = os.path.join(os.environ['GROUP'], 'Datasets')
        models = os.path.join(os.environ['WORK'], 'Manne_2025', 'models')
        output = os.path.join(os.environ['WORK'], 'Manne_2025', 'output')
        tmp    = os.environ['TMPDIR']
        thesis = os.path.join(os.environ['HOME'], 'Student_Theses/Manne_2025_Master/thesis')
    # For A. Manne on local machine and on HPC:
    elif user_name == 'amanne':
        # amanne on Linux laptop
        data    = "/home/amanne/Documents/Manne_2025_Master/data"
        models  = "/home/amanne/Documents/Manne_2025_Master/python/models"
        output  = "/home/amanne/Documents/Manne_2025_Master/python/output"
        tmp     = "/home/amanne/Documents/Manne_2025_Master/python/tmp"
        thesis  = "/home/amanne/Documents/Manne_2025_Master/thesis"   
    elif user_name == 'gana0076':
        # gana0076 on HPC
        data   = os.path.join(os.environ['GROUP'], 'Datasets')
        models = os.path.join(os.environ['WORK'], 'Manne_2025', 'models')
        output = os.path.join(os.environ['WORK'], 'Manne_2025', 'output')
        tmp    = os.environ['TMPDIR']
        thesis = os.path.join(os.environ['HOME'], 'Manne_2025_Master/thesis')    
    elif user_name == 'abcd1234':
        data    = "Directory containing icare and TUHEEG datasets"
        models  = "Where to save the trianed models"
        output  = "Directory where to save output"
        tmp     = "Directory where to save temporary iles, deleted after processing"
        thesis  = "Directory where the thesis is stored"
    else:
        raise Exception('Unknown user_name.')
        
    icare = os.path.join(data, '2023_Physionet_Official/i-care/2.0/training')
    tuh   = os.path.join(data, 'TUH_EEG/tuh_eeg/v2.0.1/edf')
    paths = namedtuple('paths', ['data', 'models', 'output', 'tmp', 'thesis', 'icare', 'tuh'])
    return paths(data, models, output, tmp, thesis, icare, tuh)

# def list_dirs(top_dir):
#     # list directories in top_dir, not recursive
#     sub_dirs = [os.path.basename(f.path) for f in os.scandir(top_dir) if f.is_dir()]
#     return sub_dirs

# def reset_dirs():
#     paths = get_paths()
#     rm_dir(paths.output)

    
# def clean_up():
#     paths = get_paths()
#     rm_dir(paths.output)

def rm_dir(dir_name):
    dir_path = Path(dir_name)
    if dir_path.exists() and dir_path.is_dir():
        shutil.rmtree(dir_name)
