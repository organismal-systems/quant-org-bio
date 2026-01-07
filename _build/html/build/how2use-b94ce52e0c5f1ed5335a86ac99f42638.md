# 🧭️ How to use this book

This book is organized into **Parts**, each devoted to a different general topic or biological research area:
- ***Biomechanics*** in physiology, behavior and sensing;
- ***Demography***, epidemiology and other dynamics of population;
- ***Spatial dynamics***, in which spatial distributions are essential to model derivations and biolical implications;
- ***Experimental methods***, including statistics, image/video analysis and other tools.

Each Part contains **Units** that present, in context, one or more models within the general topic. 
"In context" means that these Units provide:
- brief background (with links to additional outside references)  
- one or more Jupyter notebooks with working "executable" models
- instructions how to use the models, and how to interpret model output
- activities that explore potential implications of the model for interesting questions in Organismal Biology.  

Units are constructed from several types of pages, indicated with icons on the Table of Contents:
- 🧭️ "Orientation" pages, explaining the book structure and assisting in navigation to topics of interest
- 🏞️ "Introductory" pages, with context articulating the essential scientific rationale underlying models and activities
- 🧮 "Worksheet" pages, containing Jupyter notebooks with executable models
- 📖 "Background" pages, with additional information relevant to model derivation, output interpretation and activities
- 🛼 "Activity" pages, outlining "mini-studies" in which users can use the model to develop and test hypotheses about organism functions and interactions
- 💡 "Key Topic Ideas" pages, with more detailed focus on ideas on which models, analysis and activities are based  

These different document types overlap in their content, but generally "Introductory" pages are very useful or necessary for a basic operation of the models, which "Background" pages contribute to a deeper understanding of models' foundations, implications and limitations.

"Key Topic Ideas" are important background that is a somewhat more detailed presentation of a biological concept, or a specific idea on which a modelling approach is founded or interpreted.
These pages are intended to be short enough for a reader to internalize the most relevant, essential facts about a topic refered to in a model, without losing continuity of thought while working with that model.
Key Topic Ideas are not intended to be comprehensive, though ideally they may refer to additional sources that provide in-depth perspectives.
In many cases the most useful reference is simply a link to Wikipedia, which has proven to usually be comprehensive and accurate in many areas of biology, mathematics, physics, statistics and other disciplines.


## Usage
In general, users are expected to focus on a single Unit at a time, optionally followed by other related Units.
For example, a user who investigates movement of [particles](../../subrepos/biomechanics/ReSphere/RScontext.md) and [embryos](../../subrepos/biomechanics/ChimeraSwim/ChimeraSwim.ipynb) through fluids might follow up with an investigation of [larval dispersal in estuaries](../../subrepos/spatial-dynamics/EstuaryLarva/EstLarvSwim.ipynb), to understand the population and geographical implications of biomechanical characteristics. 

The intended method for most readers to use the book is to:
- read the "Introductory" pages in the [GitHub Pages e-book](https://organismal-systems.github.io/quant-org-bio/)
- use the "button" links to open and execute the models in the worksheet notebook on [Binder]()
- after getting familiar with the model, select an Activity and conduct the suggested systematic data collection. analysis and interpretation
- refer to "Background" and "Key Topic Ideas" for additional information

In courses and some other settings, an opportunity may be present to
- make a slide or two that presents an argument, conclusion or analysis using graphical or textual output from a model

## Static *vs.* executable book content
It's important for users to understand the differences between **static** and **executable** book content:
- Executable book content is that which is accessed through Binder, consisting of Worksheets implemented in Jupyter notebooks, sometimes with supporting Python code.  
  These notebooks provide interactive interfaces for setting parameters, running models and viewing output, for experiential learning by users.
- Static book contents are those accessed through GitHub Pages.  
  These contents include all the types of pages: Orientation, Introductory, Background, Activity and Key Topic Area pages.
  They also include Worksheets, but only as static non-operable copies &ndash; these copies cannot be executed like the ones on Binder can.
  

