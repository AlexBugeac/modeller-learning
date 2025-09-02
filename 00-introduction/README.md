# Introduction to MODELLER

## What is MODELLER?
MODELLER is a software package for **comparative protein structure modeling**.  
It builds 3D atomic models of proteins by satisfying spatial restraints, using:
- Known experimental structures (templates).
- A target sequence to be modeled.
- Alignments between target and templates.

---

## Using MODELLER for Comparative Modeling

MODELLER’s core workflow is:
1. **Prepare input files**:
   - **Atom file(s)**: Template coordinates from the PDB (e.g., `5fd1.pdb`).
   - **Alignment file**: PIR format alignment of target and template(s).
   - **Script file**: A Python script describing the modeling job.
2. **Run MODELLER** with the script.
3. **Examine output**: a PDB model of the target protein, plus logs and scores.

References:
- MODELLER documentation: https://salilab.org/modeller/documentation.html  
- Bioinformatics resources: https://salilab.org/bioinformatics_resources.shtml  
  - **MODBASE**: database of comparative models  
  - **MODWEB**: automated modeling webserver  
  - **MODLOOP**: automated loop refinement server  

---

### Example Input Files

**Alignment file (`alignment.ali`)**:
```pir
C; A sample alignment in PIR format

>P1;5fd1
structureX:5fd1:1:A:106:A:ferredoxin:Azotobacter vinelandii:1.90:0.19
AFVVTDNCIKCKYTDCVEVCPVDCFYEGPNFLVIHPDECIDCALCEPECPAQAIFSEDEVPEDMQEFIQLNAELA
EVWPNITEKKDPLPDAEDWDGVKGKLQHLER*

>P1;1fdx
sequence:1fdx:1:A:54:A:ferredoxin:Peptococcus aerogenes:2.00:-1.00
AYVINDSC--IACGACKPECPVNIIQGS--IYAIDADSCIDCGSCASVCPVGAPNPED-----------------
-------------------------------*


**Template structure file (`5fd1.pdb`)**
HEADER    OXIDOREDUCTASE                          24-JAN-90   5FD1  
TITLE     FERREDOXIN (OXIDOREDUCTASE)  
EXPDTA    X-RAY DIFFRACTION  
ATOM      1  N   ALA A   1      11.921  13.207   2.245  1.00 20.00           N  
ATOM      2  CA  ALA A   1      12.769  12.005   2.511  1.00 20.00           C  
ATOM      3  C   ALA A   1      12.028  10.708   2.070  1.00 20.00           C  
...  

**Python script (`model-default.py`)**
from modeller import *  
from modeller.automodel import *  
log.verbose()  
env = Environ()  
env.io.atom_files_directory = ['input_files']  
a = AutoModel(env,  
              alnfile  = 'input_files/alignment.ali',  
              knowns   = '5fd1',  
              sequence = '1fdx')  
a.starting_model = 1  
a.ending_model   = 1  
a.make()  

When this script is executed with the command python model-default.py > model-default.log, MODELLER writes detailed progress messages into model-default.log and produces a PDB file containing the modeled structure of the target sequence. The main outputs are model-default.log, which contains the log of the run, and 1fdx.B99990001.pdb, which contains the 3D model. The filename format is always <sequence>.B9999<model_number>.pdb, and if more than one model is requested by increasing the ending_model parameter, multiple PDB files are created. It is always important to check the log for warnings marked with W> and errors marked with E>.