# Including Water Molecules, HETATM Residues, and Hydrogen Atoms

In some cases, your **template PDB file** contains ligands or other non-protein residues (e.g., DNA, RNA, small molecules, cofactors, or anything marked as `HETATM`). By default, MODELLER ignores these records. However, you can configure it to include them in your generated model.

This is done by:
- Using the **`.` (BLK)** residue type in your alignment to represent ligands or other HETATM residues.  
- Setting specific environment options (e.g., `env.io.hetatm = True`) to instruct MODELLER to read these records.  

---

## ⚙️ Key Options

- `env.io.hetatm = True` → read **HETATM** records from the template PDB file.  
- `env.io.water = True` → include **water residues** (use `w` in alignment).  
- `env.io.hydrogen = True` → include **hydrogen atoms** (generally not needed; instead, use the **AllHModel** class).  

---

### 🧬 Example Input Files

**Template structure file (`5fd1.pdb`)**
```HEADER    OXIDOREDUCTASE                          24-JAN-90   5FD1
TITLE     FERREDOXIN (OXIDOREDUCTASE)
EXPDTA    X-RAY DIFFRACTION
ATOM      1  N   ALA A   1      11.921  13.207   2.245  1.00 20.00           N
ATOM      2  CA  ALA A   1      12.769  12.005   2.511  1.00 20.00           C
ATOM      3  C   ALA A   1      12.028  10.708   2.070  1.00 20.00           C
...
HETATM  107  FE   SF4 A   1      15.123   9.876   3.456  1.00 20.00          FE
HETATM  108  S1   SF4 A   1      16.789  10.234   2.987  1.00 20.00           S
```

**Alignment file (`align-ligand.ali`)**
```pir
C; Similar to alignment.ali, but with ligands included

>P1;5fd1
structureX:5fd1:1:A:108:A:ferredoxin:Azotobacter vinelandii:1.90:0.19
AFVVTDNCIKCKYTDCVEVCPVDCFYEGPNFLVIHPDECIDCALCEPECPAQAIFSEDEVPEDMQEFIQLNAELA
EVWPNITEKKDPLPDAEDWDGVKGKLQHLER..*

>P1;1fdx
sequence:1fdx:1:A:56:A:ferredoxin:Peptococcus aerogenes:2.00:-1.00
AYVINDSC--IACGACKPECPVNIIQGS--IYAIDADSCIDCGSCASVCPVGAPNPED-----------------
-------------------------------..*
```

**Python script (`model-ligand.py`)**

```python
# Comparative modeling with ligand transfer from the template
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the AutoModel class

log.verbose()                       # request verbose output
env = Environ()                     # create a new MODELLER environment

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Read in HETATM records from template PDBs
env.io.hetatm = True

a = AutoModel(env,
              alnfile  = 'align-ligand.ali',  # alignment filename
              knowns   = '5fd1',              # template code
              sequence = '1fdx')              # target code

a.starting_model = 4   # index of the first model
a.ending_model   = 4   # index of the last model
a.make()               # build the model
```
