# Transmembrane - short project

Assignment and detection of a protein's transmembrane regions

WARNING DO NOT RUN THE SCRIPT IT LOOP INFINITELY

## Set up the environnement

### clone this repository

```bash
git clone https://github.com/iphigenieG/transmembrane.git
```
go into the created directory
```bash
cd ./transmembrane
```

### Install conda

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)

And for more speed install [mamba](https://mamba.readthedocs.io/en/latest/):
```bash
conda install mamba -n base -c conda-forge
```

### Create the `transmembrane` conda environnement

```bash
conda env create -f transmembrane.yml
```
or (recommended)

```bash
mamba create -f transmembrane.yml
```

### Load the `transmembrane` conda environment:
```bash
conda activate transmembrane
```

### Quit the conda environment when done:
```
conda deactivate
```
## Exemple use to get started

### Download a pdb file
For this exemple let's download the protein from [this entry](https://opm.phar.umich.edu/proteins/154) in the OPM database.
Either download the pdb  from your navigator or directly from the terminal like so:

```bash
wget https://files.rcsb.org/download/1JDM.pdb
```

### Use the main script to search for transmembrane regions

The basic usage goes like this (after activating the conda environement as shown previously)

```bash
python main.py 1jdm.pdb
```
We can manually set the width of the membrane in angstrom (defaults to 14)

```bash
python main.py 1jdm.pdb 22
```
