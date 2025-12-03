# Predicting Neurological Recovery in Comatose Patients Post Cardiac Arrest

README FILE TO BE FILLED UP

This directory contains the code and data to replicate the results (and paper) described in:

DETAILS OF PUBLICATION TO BE ADDED

## Getting Started

In order to use the included code and replicate the results, you will need:

1. A working Python environment (see next session) 
2. Access to the HPC of the Uni Oldenburg
3. Be part of the agamt group on the HPC (to access the used data)


## Python

### Setup and check your workflow

The work is conducted in Python 3.11.4, using pyenv to setup the environment

#### Setup on local machine

1. Make sure pyenv is available on your system
2. create environment using: `pyenv virtualenv 3.11.4 Manne_2025_Master-3.11.4`
3. Install required packages using, from within the python directory: `~/.pyenv/versions/Manne_2025_Master-3.11.4/bin/pip install -r requirements.txt`
4. Configure your IDE to use the correct python interpretter
	1. In Spyder: Spyder > Preferences > Python Interpreter >  Use the following Python interpreter : `~/.pyenv/versions/Manne\_2025_Master-3.11.4/bin/python`
	2. In Pycharm: [instructions](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter)
5. Download part of the data on your local machine by executing the script, from within the data directory: `hpc_to_local.sh` 
6. Check (and correct if necessary) the paths under your user names in `python/utilities/PathsUtilities.py` 
7. Check that it is working running the example: `data_example.py `, the output should be:

	```
	Executing script check_setup.py on local machine
	Read TUH data succesfully.
	Read icare data succesfully.
	```

#### Setup on the HPC

1. Log into the HPC and load the necessary modules as:
	
	```
	module load hpc-env/13.1
	module load  Anaconda3/2023.09-0
	```
	
2. Create the environment and install requirements using pip as:

	```
	conda create --name Manne_2025_Master-3.11.4 python=3.11.4
	conda activate Manne_2025_Master-3.11.4
	pip install -r requirements.txt
	```
3. Schedule the job using, from within the python directory: `sbatch check_setup.job` ooo 
4. Check if you're job is running using: `squeue -u abcd1234` (replace by whatever your HPC user name is)
5. Once the job is finished, a directory `python/logs` should have been created containing two files ending in .err and .out. The error file .err should be empty and the .out dile should end with these 3 lines: 

	```
	Executing script check_setup.py on the HPC as abcd1234
	Read TUH data succesfully.
	Read icare data succesfully.
	```


	



## Data

This work is based on two publicly available datasets (TO DO: write the propoer citaitons here):

I-CARE avaialable [here](https://physionet.org/content/i-care/2.1/)

TUH EEG Dataset available [here](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/)




## Paper / Thesis

How replicate figures and compile the document


## Questions

For more information about this project you can contact [Benjamin Cauchi](mailto:benjamin.cauchi@offis.de).

		