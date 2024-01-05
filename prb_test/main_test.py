from probe_design import PATHDATA, PATHMAIN, PATHSRC, PATHSHELL
import probe_design as prb
import os
import shutil
import subprocess

print(prb.__all__) # List of all functions in probe_design

# Example run script for probe_design

## 1. Copy data folder from probe_design to working directory
if not os.path.exists('data'):
    shutil.copytree(PATHDATA,'data')
else:
    print('Data folder already exists! ... NOT OVERWRITING')

### 1.1 Download and install the necessary chr fasta
prb.download_chr(chr=17)
#### defaults 
    # prb.download_chr(chr_folder='data/ref',chr=17,release=109,build=38)
#### you can use the download_chr_list function to download multiple chromosomes
    # prb.download_chr_list([17,18,19,'X','Y'])

## 2. Create required folders
###  Declare folders to create
folders : list[os.PathLike|str] = ['data',
                                   'data/candidate',
                                   'data/secs',
                                   'data/db',
                                   'data/db_tsv',
                                   'data/logfiles',
                                   'HUSH']
### Create folders
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        print(f'Folder {folder} already exists! ... NOT OVERWRITING')

## 3. Retrieve your region sequences and extract all k-mers of correct length
prb.get_oligos(nt_type='DNA',gcfilter=1,extfolder='./data') # Defaults

## 4. Test all k-mers for their homology to other regions in the genome, using nHUSH.
subprocess.run(['bash',
                os.path.join(PATHSHELL,'run_nHUSH.sh'),
                '-d DNA -L 20 -l 21 -m 3 -t 40 -i 14 -g'])
'''
Instead of running the entire 
    k-mers (of length L) at once, 
can be sped up by testing 
    shorter sublength oligos (of length l).
-m number of mismatches to test for (always use 1 when running sublength); 
-t number of threads,
-i comb size
'''



if __name__ == '__main__':
    clean = True
    if clean:
        print('Cleaning up...')
        shutil.rmtree('data')
        shutil.rmtree('HUSH')
        print('Done!')
