## io_nerdss

This repository primarily contains Python code for creating user-friendly analysis tools for setting up models and analyzing output from the reaction-diffusion simulator NERDSS.

### Branch description

We have created a new development branch where we will be improving the code quality, cleaning up tutorials, optimizing certain functions, and reorganizing directories for better readability.

### Folder Descriptions

**IoNERDSSPyPi: Holds the main code of the library + extra files necessary for PyPi**
 - **IoNERDSS:** Holds the actual code. Each function can be find as a seperate file in /functions.
 - **ioNERDSS.egg-info:** text that is necessary for PyPi.

**Tutorial: Holds developer and user tutorials**
 - **DevelopersGuide:** Describes how to edit library, and then upload it to PyPi.
 - **MultiSpeciesTutorial:** Desribes how to create graphs and spreadsheets from a multi-component histogram file outputted by NERDSS.
    - **Dodecahedron:** What is input into a NERDSS sim.
    - JupyterNotebook: Describes how to use different functions required for making graphs and spreadsheets from the output of a multi-component NERDSS sim.
    - histogram_complexes_time_dode_1 .... _5: the output from a NERDSS sim used by IoNERDSS in this context.
    - .png / .csv: Charts and spreadsheets outputted by IoNERDSS.
 - **ReadRealPDBTutorial:** Describes how to interpret a pdb file from a NERDSS sim & create new inputs based off of it.
    - JupyterNotebook: Describes how to use different functions required for interpreting data in pbd file & how to create new inputs for the NERDSS sim.
    - 1si4.pdb (hemoglobin protein) & 1utc.pdb (clathrin protein): The output from a NERDSS sim used by IoNERDSS in this context.
    - .mol / .inp: What is inputted into a RealPDB NERDSS sim, generated by IoNERDS.
    - show_structure.pdb: 'Simplified' .pdb file for creating graphs of the protein's connections, generated by IoNERDSS.
 - **SingleSpeciesTutorial:** Describes how to create inputs for a NERDSS sim & how to create graphs and spreadsheets from a single-component histogram file outputted by NERDSS.
    - JupyterNotebook: Describes how to use different functions required to create inputs for a NERDSS sim & to make graphs and spreadsheets from the single-component NERDSS output.
    - .mol / parm.inp: What is inputted into a Single-component NERDSS sim, generated by IoNERDSS.
    - histogran_complexes_time_dode_1 ... _5: The output from a NERDSS sim used by IoNERDSS in this context.
    - transition_matrix_time_1 ... _5: The output from a NERDSS sim used by IoNERDSS in this context.
    - restart.dat / 9999999.pdb: The output from a NERDSS sim used by IoNERDSS in this context.
    - output_file: IoNERDSS outputted file. Edited version of restart.dat/9999999.pdb.

**ExamplesIoNERDSS: Holds a lot of files that (i may be wrong) seem to be environments for using IoNERDSS or examples of it being used.** (This section has been less thoroughly checked and written about.)
 - **LocatePositionByPdbRestart** : an example of using IoNERDSS to interpret data from the pdb / restart / .dat files from a single-species NERDSS sim.
    - **PDB:** Example of using parms.inp + 9999999.pdb to locate positions.
    - **restart:** Example of using restart.dat + 9999999.pdb to locate positions.
    - Both Include:
        - output_file.pdb: File outputted by the jupyter notebook code.
 - **OutputVis:** An example of IoNERDSS using histograms and transition matricies from Single & MultiSpecies NERDSS sims to create graphs. (code not in a directory is for single species).
     - **multi_components:** Same thing but for multispecies.
        - **simulation:** Seems to be a complete NERDSS output.
        - **multi_components_sikao:** Another example of creating graphs (same data type as before, but new files).
        - JupyterNotebook: Shows a lot of examples of creating graphs based on data. Both inports and instantiates (some) functions.
        - histogram_complexes_time ... _5: NERDSS outputs.
    - histogram_complexes_time_dode_1 ... _5: NERDSS single-species output.
    - transition_matrix_time ... _5: NERDSS single-species output.
    - JupyterNotebook: Seems to just instantiate all functions that would be necessary, but does not do anything with them. Possibly intended for user to use final box?
    - hist_3d_time.py: Python script that generates a graph based on the other files in the folder.
    - multi_comp_hist.dat / hist_to_df.csv: Unknown.
 - **PdbAngleCalculation:** An example of IoNERDSS using pbd files from a NERDSS sims to create graphs and new inputs for NERDSS.
    - **1utc** : Seems to be an example of using IoNERDSS for editing PDB files and creating files to be input into NERDSS. However, the code is seperate from the library, and just .py files here. 
    - **raw_functions:** Same as 1utc but only includes the functions.
    - 3Dtest.py: Unknown.
    - JupyterNotebook: Instantiates IoNERDSS functions and uses them for various PDB related tasks.
    - 1si4/1utc: NERDSS output.
 - **PlatonicSolids:** Examples of creating platonic solids using IoNERDSS.
    - Folders with solid names (ex: Cube, Octahedron).
        - **[name]Face** and **[name]Vertex:** the two files have slightly different contents in each file, but I do not know the difference.
            - [name].mole / parm.inp: inputs for NERDSS made by IoNERDSS.
            - JupyterNotebook: Creates the inputs for NERDSS (instanstiates all functions, does not import).
    - **PyFilesForPlatonicSolids:** Includes python files that instantiate functions that can be used to create Platoic Solids that can be inputted in NERDSS. However, the scripts will not create any platonic solids as they only instantiate the functions, maybe intended for user to add their own code at the bottom.
    - **Clath_rotate:** Includes 1 JupyterNotebook that instantiates and then runs functions that rotates clathrin (the initial clathrin data is included in the script).



### Install

To install via pip, use the command: 
pip install ioNERDSS

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
