# Chlorophyll notebook

Intended audience: A Python-savvy programmer needs a walk-through on photic zone datasets. Other intended audience: Myself after six months away from this project. 


## Contents

* Section I: Setting up holoviz
* Section II: Details on setting up holoviz
* Section III: Setting up Jupyter Lab
* Section IV: Details on setting up Jupyter Lab
* Section V: Prosaic context


## I Setting up holoviz

Starting with a bare Linux OS, pre-Python install. Some of these actions are "my preference".
For example I use `ssh` tunnels a lot so I have to start *jupyter notebooks* in no-screen
mode; and I alias this command to `jbook`. I also modify my terminal window and `vim` editor.


* start a VM, for example a modest AWS EC2 with a 32+ GB root drive (gives us some headroom)
    * include a local `bash` environment with a keypair (`.pem`) file; and log in
    * modify the prompt in `.bashrc` and edit `.bash_aliases` to include common commands
* install miniconda
    * search `install miniconda`, find the Linux version, copy the link
    * go to the VM prompt and run `wget <that link>`
    * per [this page](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html) run `bash <Miniconda_file.sh>`
        * During this installation: Agree to terms (or don't, see if I care) and allow the default install location.
        * This does not require `sudo` as one operates here as a system User installing "one's own" code.
        * That code just happens to be a package manager and a version of Python3. 
        * This in turn means having some awareness of both paths and Python environments. 
        * For example: Python 3 may already be included in the OS. 
            * On an AWS EC2 with Ubuntu: `which python3` produces `usr/bin/python3`
            * Always check that you are running the Python you intend.
         * The Miniconda installation modifies the User `.bashrc` file
             * A block of code is appending a block of code
             * The comments explain that this is "managed by `conda init`"...
             * ...so don't touch it.
         * `conda: command not found`
             * Sometimes the above auto-modification to `.bashrc` does not work. For example on my PC. 
             * First cd to your home directory and make sure the `miniconda3` directory is present
             * We need to add to the `$PATH` variable. Put this line at the end of `~/.bashrc`
             * `export PATH="/home/lparsons/miniconda3/bin:$PATH"`
             * Save the file and run `source .bashrc`
             * See if it worked: Type `conda`
         * Miniconda install advises: Close and reopen the terminal window
         * Enironments: Create an environment just to get the hang of it
              * Run this: `conda create --name myenvironment python=3.8`
              * Ensure it is listed: `conda env list`
              * See it in its registry location: `ls ~/miniconda3/envs`
              * Activate it: `conda activate myenvironment`
                  * I was informed that I need to run `conda init bash` for this to work
                  * After I ran it I was also told to close and re-open the shell
                  * So I did that... and thereupon `conda activate myenvironment` worked properly
              * Notice the prompt has changed: `(myenvironment) usualprompt>`
                  * This is a handy way to discern whether or not I am in the environment
              * Below we start building out environments from configuration `.yml` files
              * For now let's deactivate and remove this environment
                  * `conda deactivate`
                  * `conda env remove --name myenvironment`
                  * `ls ~/miniconda3/envs` to check that the environment is no longer listed
              
* Now back to holoviz: 
    * To reiterate: I am working on an AWS c5.large EC2 instance running Ubuntu.
    * Go [here](https://holoviz.org/installation.html) with the idea of completing the holoviz installation
        * Note this uses Python 3.7 whereas we just installed Miniconda with Python 3.8...
        * But this is detected and some package manager magic happens.
        * However I ran into a serious issue (circa January 2021)
            * This works fine: `conda update conda` (twice)
            * This works fine: `conda create -n holoviz-tutorial python=3.7`
            * This works fine: `conda activate holoviz-tutorial`
                * I have a prompt indicating I am in an activated Python environment, check.
            * This fails: `conda install -c pyviz holoviz`
                * `ERROR conda.core.link:_execute(698): An error occurred while installing package 'defaults::rise-5.6.1-py37_1'.`
                * Please observe that `-c pyviz` references the *pyviz* **channel**. 
                * Below the three installs use channel = *conda-forge* instead.
                * What to do? Go on [the holoviz discourse site](https://holoviz.discourse.org) and create a topic: "Help!"
            * This worked: `conda install -c conda-forge datashader`
            * This worked: `conda install -c conda-forge hvplot`
            * This worked (after a time): `conda install -c conda-forge geoviews`
            * At this point **holoviz** is not installed. It is also not found on the `conda-forge` channel. 
            * Trying `conda install -c pyviz holoviz` is the next try; but this finds conflicts
    * Make sure to return to the base environment using `conda deactivate` and proceed:
        * create a holoviz_env.yml file with the content as given below
        * execute `conda env create -f holoviz_env.yml`
        * this builds a coordinated environment with all of those packages installed (my trial featured no drama)
        
```
name: holoviz
channels:
  - conda-forge
  - defaults
dependencies:
  - datashader
  - geoviews
  - hvplot
  - ipykernel
  - pandas
  - xarray
  - fsspec
```

* go [here](https://holoviz.org/tutorial/index.html) for the tutorial
* go [here](https://www.youtube.com/watch?v=7deGS4IPAQ0) for a live narrative run-through


## II Details on setting up holoviz

### II.1 Details on AWS EC2 start

I'm using a very light AWS EC2 instance: Instance type m5.large at ten cents per hour. By default this 
comes with an 8GB root volume; which I increase to 32GB so as to not run out of disk space when working
through the holoviz tutorial. 


#### II.1.1 Account and burn

* Getting an AWS account.
* Calculating how long it would take to use $100.
* What are the issues in connecting the account to real money?
* What is CloudBank and how is it useful?

#### II.1.2 Wizard details including root volume

* First step of the wizard is to choose an image
    * Many options
    * Can save customized images and shift to different instance types
* As noted above: Small EC2 instances come with 8GB root drives. Two options:
    * Increase this size in the wizard
    * Add additional volumes: Down side they must be mounted on the instance
        * to do look up my notes on this and reference / copy

        
#### II.1.3 elastic ip use


Cloud instances are assigned an ip address. Typically this can change when the machine 
is stopped and then restarted. To not have to deal with this moving target AWS makes a
number of *elastic ips* available. These can be assigned to the instance; and they persist.


### II.2 Details on `.bashrc` and `.bash_aliases`

If like me you find color coded editor windows infuriating, why not customize vi (or *vim*)
to just use one color. And perhaps also the text in the terminal window. And perhaps stop the bell from
ringing (a Windows task associated with the bash shell; I'm using Ubuntu). And for common commands
perhaps create simple aliases. All of this is intended to accelerate us towards focus on the 
research. to do is describe how to actually do this stuff.


### II.3 Details on `miniconda` and environments


## III Setting up Jupyter Lab



## IV Details on Jupyter Lab


We want the Jupyter Lab hosted on the remote VM; and either a direct connection or an `ssh` tunnel.
to do describe how to do this. 


## V Context



### Introduction

We're interested in insight from *in situ* ocean sensors; covering physical, chemical and biological research.
What is the value of the data? There is a lof of difficult tactical work involved in arriving at good answers.


### Data

This repository concerns using [Ocean Observatories Initiative (OOI)](https://oceanobservatories.org/) 
data and data from other sources to examine chlorophyll
concentration in the northeast Pacific ocean. Most development uses the Pangeo Jupyter Hub. An alternative is to spin 
up a dedicated Jupyter Lab notebook server on the cloud; for example using 
[these instructions](https://github.com/cloudbank-project/image-research-computing-tutorial/blob/master/README.md).


### Productivity, sensors and research questions


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



