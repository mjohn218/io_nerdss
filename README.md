## io_nerdss

This repository primarily contains Python code for creating user-friendly analysis tools for setting up models and analyzing output from the reaction-diffusion simulator NERDSS.

### Branch description

We have created a new development branch where we will be improving the code quality, cleaning up tutorials, optimizing certain functions, and reorganizing directories for better readability.

### Folder Descriptions

**IoNERDSSPyPi: Holds the main code of the library + extra files necessary for PyPi**
 - **IoNERDSS:** Holds the actual code. Each function can be find as a seperate file in /functions.
 - **ioNERDSS.egg-info:** text that is necessary for PyPi.
 - Then some text files that are all for PyPi

**Tutorial: Holds developer and user tutorials**
 - **DevelopersGuide:** Describes how to edit library, and then upload it to PyPi.
 - **MultiSpeciesTutorial:** Desribes how to create graphs and spreadsheets from a multi-component histogram file outputted by NERDSS.
 - **ReadRealPDBTutorial:** **WARNING OUTDATED** Describes how to interpret a pdb file from a database & create NERDSS inputs based off of it. **WARNING OUTDATED**
 - **SingleSpeciesTutorial:** Describes how to create inputs for a NERDSS sim & how to create graphs and spreadsheets 
                              from a single-component histogram file or transition matrix outputted by NERDSS.

**Unimportant: Holds files that may be useful for ioNERDSS development**
 - **ExamplesIoNERDSS:** Holds a lot of files that (i may be wrong) seem to be environments for using IoNERDSS or examples of it being used
 - **TestingFunctions:** Holds the different files necessary to try out all of ioNERDSS' functions. 
    - Recommended to be moved to ioNERDSSPyPi folder along with ioNERDSS_profiler.py
 - pre_update_ioNERDSS.py: this is the ioNERDSS from before the update. If there are functions not working, they may be working in this version (just slower).
 - Some python scripts that were helpful for testing / profiling

### Note From Ian 5/18/2023
This is my last day in the lab, and so my last day (probably) working with ioNERDSS. I have tried to tie up all of the loose ends, however there are still some of note:
 (1) The ReadRealPDBTutorial is out of date 
 (2) Certain functions are not in the UserGuide - you can find them listed at the bottom under ``2.7 Needs to be added``
 (3) Under certain circumastances functions may break, if you find any issues let me know and if it is before my school starts I will try to fix it
   - Functions are especially prone to breaking if you have a multi species system or multiple files (histogram will work fine)
 (4) The docs, docstrings and actual code may be slightly out of sync. If you find any issues please let me know


### Install

To install via pip, use the command: 
run ``pip install ioNERDSS`` on the command line

### Syncing PyPi from GitHub

- Navigate to the ioNERDSSPyPi folder
- Ensure that your package's version number in setup.py matches the version number of the PyPI package you want to sync (It should be a newer version). If not, update the version number.
- Create a source distribution of your package by running the following command in your terminal: **python setup.py sdist**. This will create a dist directory containing a tarball of your package's source code.
- Upload the source distribution to PyPI by running the following command: twine upload dist/*

### Best practices

- Use docstrings to document your code. Sphinx can extract docstrings from your code to create documentation, so it's important to write clear and concise docstrings that describe the purpose and functionality of your code.
- Use reStructuredText (reST) markup in your docstrings.
- Follow the Google-style docstring conventions. This is a popular convention for writing docstrings that is widely used in the Python community. It consists of a one-line summary, followed by a more detailed description, and optional sections for parameters, returns, and other details. You can find more information on this convention in the Sphinx documentation.
- Organize your code into modules and packages.
- Use meaningful names for modules, classes, functions, and variables.
- Include examples and usage instructions in documentation. Sphinx can include examples and usage instructions in your documentation, which can help users understand how to use your code.
- Use Sphinx to generate documentation.
- Add tests for each function using unittest.
