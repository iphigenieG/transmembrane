# Transmembrane - short project

Assignment and detection of a protein's transmembrane regions

## Set up the environnement

### clone this repository

```bash
git clone https://github.com/iphigenieG/transmembrane.git
```
```bash
cd ./transmembrane
```

### Install conda

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)

for more speed install mamba:
```bash
conda install mamba -n base -c conda-forge
```

### Create the `transmembrane` conda environnement

```bash
conda env create -f transmembrane.yml
```
or

```bash
mamba create -f transmembrane.yml
```

### Load the `transmembrane` conda environment:
```
conda activate transmembrane
```

### Quit the conda environment:
```
conda deactivate
```
