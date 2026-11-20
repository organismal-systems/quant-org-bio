# 🧭️  Using book content on your own computer, Part 2

There are few situations in which is makes sense to download the entire book onto a local machine, unless you are contributing a new unit or making substantial editorial suggestions about an existing one[^cont].
There are situations, for example in running a workshop or course based on book content, in which it may make sense to do this.

[^cont]: New contributed Units are placed (after review and acceptance) into their own repositories within the main [**organismal-systems GitHub repository**](https://github.com/orgs/organismal-systems/repositories), so even for contributors is often is best to use the online [GitHub pages version](https://organismal-systems.github.io/quant-org-bio/) as the reference for textual content.

## Installing the book on a local computer

The potential advantages of installing the entire book locally include:
- *Customizing a course-specific version of the book*  
  Because the book structure is determined entirely by the **_toc.yml** file, it is straightforward to remake the book structure by editing this file.
  For example, a course on Biomechanics might include only the Biomechanics part, a course on Larval Biology might include only a set of models relevant to that topic, **etc**.
- *Obtaining all the content (notebooks, content, etc.) at once.*  
  If you intend to use many different models, cloning the entire book is a quick way to have them all on your local computer.
  Be aware, though, that you will still need to follow the [instructions for setting up a local Python environment](./localcopy.md) before you can run the notebooks.
- *Independence from Internet connections*  
  There are situations, for example during travel or at a field station, where Internet may be unavailable or costly.
  In these cases, having a copy on a laptop or desktop computer may facilitate reading the book.

The best way to set up to run a Jupyter notebook locally is to [clone the source repository from GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
In doing this, it is important to remember that
> The "current" version of the notebook is in the [Quantitative Organismal Biology](https://github.com/organismal-systems/quant-org-bio) repository, under the "main" (default) branch.

To build the book, use a terminal window to execute
```bash
conda env create --name QOB --file environment.yml
```
This command creates a new conda environment called "QOB" (change this to another informative name if you prefer) that automatically contains the specified Python packages.

To run Jupyter notebooks using this environment, execute
```bash
conda activate QOB
```
followed by
```bash
jupyter book start
```
This will show a link to open a web browser page that displays the book content.
The web page will show updates to reflect edits you make to the book content or notebooks.
