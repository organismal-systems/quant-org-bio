# 🧭️  Using book content on your own computer, Part 1

The general expectation for this book is that most users will read the content online in the [GitHub pages version](https://organismal-systems.github.io/quant-org-bio/), and execute Jupyter notebooks with models online using [Binder](https://mybinder.org/).
This is the most straighforward route, uses no resources on a local computer (or tablet/phone), and always points to uptodate implementations of content and code.

However, there are situations in which there are advantages to running notebooks on a local computer or (less frequently) to downloading and building the entire book locally.

**To make Jupyter notebooks easy to run using Binder, repositories containing those notebooks are retained on the OSYM GitHub site, from which they are linked in the book. 
These repositories may have their own license requirements, which supercede (for that content) the licensing requirements for the original content of this book.**


## Running notebooks on a local computer
The potential advantages of running notebooks locally include:
- *Faster execution, depending on the speed of the local computer*  
  Binder has limited resources for computationally intensive models.
  While most models in this book run quickly on Binder, a few require long run times that might be significantly shorter on a local computer.
- *No time-out for idle session*  
  Binder suspends a session if it has been idle too long.
  On a local computer, you can leave a session idle indefintely and it will not change.
- *Editing notebooks or codes*  
  You can edit on Binder, but those are temporarly copies that do not persist past the end of that Binder session.
  If you wish to preserve edits, you need to make those changes on local copies.

The best way to set up to run a Jupyter notebook locally is to [clone the source repository from GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
In doing this, it is important to remember that
> The "official" version of the notebook &ndash; that is, the version Binder runs &ndash; is in a repository under the [organismal-systems account](https://github.com/orgs/organismal-systems/repositories).

Cloning this repository onto your local machine not only gives you a complete functional copy of the notebooks, but also an easy way to update your version with any revisions or additions that appear in the book, to report code bugs or other issues, and to contribute enhancememnts.

Each of the models in the book requires its own specific set of Python packages.
The simplest way to make sure a local copy of a model has the required packages is to use the [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main), [Anaconda](https://www.anaconda.com) or [Mamba](https://mamba.readthedocs.io/en/latest/index.html) package managers.

The required modules for each repository are listed in a file called *environment.yml*, included with the repository.
miniconda, Anaconda and Mamba use this file to automatically recreate the set of packages needed to make the models function correctly.
For example, to [install required packages using miniconda or Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), execute
```bash
conda env create --name MyEnv --file environment.yml
```
This command creates a new conda environment called "MyEnv" (change this to something informative about the notebook it'll be used for) that automatically contains the specified Python packages.

To run Jupyter notebooks using this environment, execute
```bash
conda activate MyEnv
```
followed by
```bash
jupyter lab
```
This will open a web browser page with a "launcher" you can use to open one or more notebooks.

Notebooks in this book are typically initialized by selecting **Run all cells** under the **Run** menu.
