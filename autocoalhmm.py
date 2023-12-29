
# This script can be used to run coalHMM with the specified parameters. It requires 6 different
# arguments: the three species for a certain branch, the outgroup, the reference species.chr and
# the path for the unfiltered maf file. In turn, this script will create the necessary directories
# for the coalHMM pipeline in the path where it is executed.

import sys
import os
import pickle
import shutil
import subprocess

# Load arguments
path = '/'.join(sys.argv[0].split('/')[:-1])
species1 = sys.argv[1]
species2 = sys.argv[2]
species3 = sys.argv[3]
species4 = sys.argv[4]
target_seqname = sys.argv[5]
big_maf_file = '../../'+sys.argv[6]
winsize = sys.argv[7]
prefix = sys.argv[8]
param_lst = [path, species1, species2, species3, species4, target_seqname, big_maf_file, winsize]

# If given two/one species error model
if len(sys.argv) == 11:
    param_lst.append(sys.argv[9])
    param_lst.append(sys.argv[10])
elif len(sys.argv) == 10:
    param_lst.append(sys.argv[9])

# If the temporary directory exists
if os.path.isdir('./'+prefix):
    # Exit the script with warning message.
    sys.exit('Please, change directory or delete directory '+prefix)

print('Loading...')

# Copy temporary directory to current path
shutil.copytree(path+'/tmp/', './'+prefix)

# Save the arguments on a pickle list
with open('./'+prefix+'/params.pickle', 'wb') as f:
    pickle.dump(param_lst, f)

# Change directory and run the filtering gwf workflow
os.chdir('./'+prefix+'/filter/')
subprocess.call(['gwf', 'config', 'set', 'backend', 'slurm'])
subprocess.call(['gwf', 'run'])

#with open('../../call.txt', 'w') as f:
#    f.write(" ".join(sys.argv))

# Print success
print('Success!')
