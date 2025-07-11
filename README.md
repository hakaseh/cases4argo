# cases4argo: configurations for a vertical one-dimensional ocean model at locations where Argo floats slowly drift
This repository contains various configurations for running a one-dimensional vertical ocean model (GOTM) featuring biogeochemistry (FABM) and ensembles (EAT) applied at selected locations in the global ocean where Argo float observations are available. The repository was created primarily to develop and test optimization methods for biogeochemical parameters.

## Installation and compilation
1. Change to your home directory

```
cd
```

1. Download GOTM, FABM, EAT, MEMG, CASES, and argo1d

```
git clone --recurse-submodules -b v6.0 https://github.com/gotm-model/code.git gotm
git clone https://github.com/fabm-model/fabm.git
git clone https://github.com/bwang63/gotm-fabm-memg-biogeochemical-model.git memg
git clone https://github.com/gotm-model/cases.git
git clone --recursive https://github.com/BoldingBruggeman/eat.git
git clone https://github.com/hakaseh/cases4argo.git
```

1. Set up EAT with MEMG

```
cd eat
conda env create -f environment.yml
conda activate eat
source ./install -DFABM_INSTITUTES=memg -DFABM_MEMG_BASE=../memg
```

An error may occur in the last step because `eat` requires an older version of `cmake` (it occurred to me after I re-installed `conda` (miniconda) on May 21, 2025). To resolve this issue, downgrade `cmake` and then re-install `eat`:

```
conda install cmake=3.24
source ./install -DFABM_INSTITUTES=memg -DFABM_MEMG_BASE=../memg
```

~~The above line will create executables in `$HOME/.local/bin/` (not sure why inside a hidden directory). To use them, this directory needs to be exported.~~

~~vi $HOME/.zshrc~~

~~Add `export PATH=$PATH:/$HOME/.local/bin`~~

~~Either open a new tab in Terminal or do `source $HOME/.zshrc` to reflect this change.~~

## Set up the environment
Install additional libraries necessary for analyses.
```
cd
cd cases4argo
conda env update --name eat --file environment_extra.yml
```

## Cases

Cases refer to configurations to run the model at specific locations. Here, each case represents a fixed point where a Argo float was drifting. We created a sample case for the North Sea by following an example from the official EAT repository (https://github.com/BoldingBruggeman/eat/tree/main/tests/nns_annual), by copying and pasting the directory and modifying the contents. **NOTE this is not a case for Argo location, which is still working in progress**

```
mv case/nns_annual
```
## Activate FABM and the 1p1z model
`vi gotm.yaml` and set `use: true` for `fabm`. Also set `repair_state: true` if the model has issues running at the start.
`vi fabm.yaml` and set `use: true` for `1p1z`

### Run the model
`eat-gotm` will run the model. This will use the input files `gotm.yaml, fabm.yaml, t_prof_file.dat, s_prof_file.dat, meteo.dat` and produce the output files `result.nc, restart.nc`.
`t_prof_file.dat` is the ocean temperature input data used for restroing/nudging. It must cover the entire simulation period, otherwise an error occurs. It is automatically interpolated to the model’s output vertical and temporal resolutions and included in `result.nc` as `temp_obs`. Same for salinity and BGC variables.

### LHS ensemble of biogeochemical parameters
For ensemble with identical physics but differing BGC parameters, we still need to create matching gotm_00##.yaml for each fabm_00##.yaml.
Refer to “create_parameter_ensemble.py”

1. Define the parameters, their ranges, and precision (define_parameter_range.py)
   `python define_parameter_range.py`
1. Generate the parameter ensemble
   `python generate_ensemble_yaml.py`
   
For example, to submit 1000 ensembles using 8 cores (available on my Macbook Pro), do the following:
```
seq -f "%04g" 1 1000 | parallel -j 8 'eat-gotm gotm_{}.yaml --output_id _{}'
```



# References
- GOTM: https://github.com/gotm-model/code 
- FABM: https://github.com/fabm-model/fabm 
- EAT: GOTM-FABM implementation of PDAF (https://gmd.copernicus.org/articles/13/4305/2020/; https://pdaf.awi.de/trac/wiki; https://github.com/PDAF/PDAF)
https://github.com/BoldingBruggeman/eat
- MEMG: This is the BGC model developed by the Marine Environmental Modelling Group at Dalhousie University (https://github.com/bwang63/gotm-fabm-memg-biogeochemical-model; https://doi.org/10.1029/2005GB002456; https://doi.org/10.1029/2008GL036147; https://doi.org/10.1016/j.ocemod.2019.101437) 
- CASES: This is the configuration space, where you run the model with a specific setup. https://github.com/gotm-model/cases 

