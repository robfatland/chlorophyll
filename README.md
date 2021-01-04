# Chlorophyll

## Contents

* Section I: Setting up holoviz
* Section II: Details on setting up holoviz
* Section III: Setting up Jupyter Lab
* Section IV: Details on setting up Jupyter Lab
* Section V: Prosaic context

```
I Holoviz
```
* start a VM such as a modest AWS EC2 with a 32GB root drive
    * include a local `bash` environment with a keypair (`.pem`) file; and log in
    * modify the prompt in `.basrhc` and edit `.bash_aliases` to include common commands
* install miniconda
* go [here](https://holoviz.org/tutorial/index.html) and follow along

```
II
```

### Details on AWS EC2 start

#### Account and burn

#### Wizard details including root volume

#### elastic ip use

### Details on `.bashrc` and `.bash_aliases`

### Details on `miniconda` and environments

```
III Setting up Jupyter Lab
```

```
IV Details on Jupyter Lab
```

```
V Context
```

## Introduction


This repository concerns using [Ocean Observatories Initiative (OOI)](https://oceanobservatories.org/) 
data and data from other sources to examine chlorophyll
concentration in the northeast Pacific ocean. Most development uses the Pangeo Jupyter Hub. An alternative is to spin 
up a dedicated Jupyter Lab notebook server on the cloud; for example using 
[these instructions](https://github.com/cloudbank-project/image-research-computing-tutorial/blob/master/README.md).


## This project


Coastal oceans are typically more productive, i.e. support more phytoplankton biomass per unit volume 
than deep oceans off the 
continental shelf, by a factor of six or so. 
This differential productivity is attributed to driving phenomena such as terrigenous freshwater bringing nutrients
to coastal waters; or nutrient import due to coastal upwelling. 
It would be nice to make progress in this field; but the topic is pretty complex.
The work here focuses on understanding data sources, both
on their own and in relation to one another. As a first example the NASA MODIS satellite mission generates maps 
of ocean surface chlorophyll concentration on a regular basis (about once every two weeks) while cabled profilers
measure chlorophyll concentration to meter-scale resolution in the upper 200 meters of the water column 
as many as nine times per day. A very simple question is: Does the surface water chlorophyll concentration
from these two independent sources match? A more thorough exploration of the data and its implications is 
described in the sub-folder called `technical`. 


## Related projects

* The **Megaptera** project (nee *Whaledr*) concerns machine learning applied to identifying humpback whale calls as recorded by broadband hydrophones.
  * ...raw data server link needed...
* Student-driven work on connecting MODIS to shallow/deep profilers: Citation needed
* Resolving profiler/platform coincidence signals
* Canonical profiles
* Working with the Interactive Oceans portal



