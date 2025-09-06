# Comparative modeling with ligand transfer from the template
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the AutoModel class

log.verbose()                       # request verbose output
env = Environ()                     # create a new MODELLER environment

# directories for input atom files
env.io.atom_files_directory = ['input_files']

# Read in HETATM records from template PDBs
env.io.hetatm = True

a = AutoModel(env,
              alnfile  = 'input_files/alignment.ali',   # alignment filename (path is like this because i decided to have the inputs in a separate folder)
              knowns   = '5fd1',              # template code
              sequence = '1fdx')              # target code

a.starting_model = 4   # index of the first model
a.ending_model   = 4   # index of the last model
a.make()               # build the model