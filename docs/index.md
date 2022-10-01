# DVC-PROJECT-TEMPLATE
DVC Project Template

## STEPS -

### STEP 01 - Create a repository by using template repository

### STEP 02 - Clone the new repository

### STEP 03 - Create a conda environment after opening the repository in VS Code

'''bash
conda create --prefix ./env python=3.8 -y
'''

'''bash
conda ctivate ./env
'''
OR
'''bash
source activate ./env
'''

### STEP 04 - Install the requirements
'''bash
pip install requirements.txt
'''

### STEP 05 - Initialize the DVC project
"""bash
dvc init
'''

### STEP 06 - commit and push the changes to the remote repository
