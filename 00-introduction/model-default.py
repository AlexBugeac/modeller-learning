# Comparative modeling by the AutoModel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the AutoModel class
import os                           # Load os for directory handling

log.verbose()    # request verbose output
env = Environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['input_files']   # MODELLER will look here for 5fd1.pdb

a = AutoModel(env,
              alnfile  = 'input_files/alignment.ali',   # alignment filename (path is like this because i decided to have the inputs in a separate folder)
              knowns   = '5fd1',                        # codes of the templates
              sequence = '1fdx')                        # code of the target

a.starting_model = 1                 # index of the first model
a.ending_model   = 1                 # index of the last model
                                     # (determines how many models to calculate)
a.make()                             # do the actual comparative modeling

#The script was ran from the 00-introduction folder