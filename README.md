# Transmembrane - short project

Assignment and detection of a protein's transmembrane regions

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
```
conda activate transmembrane
```

### Quit the conda environment when done:
```
conda deactivate
```
