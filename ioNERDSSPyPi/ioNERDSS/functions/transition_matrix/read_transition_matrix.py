import numpy as np


def read_transition_matrix(FileName: str, SpeciesName: str, InitialTime: float, FinalTime: float):
    """
    Parses a text file containing information about a transition matrix over time for a specific species, and returns the matrices
    at two given time points.

    Args:
        FileName (str): The name of the file to be read.
        SpeciesName (str): The name of the species to be analyzed.
        InitialTime (float): The initial time point of interest.
        FinalTime (float): The final time point of interest.

    Returns:
        A tuple containing two numpy arrays: the transition matrix at the initial time point and at the final time point.

    The file must have the following structure:

        time: <time_value>
        <transition_matrix>

    where <time_value> is a float representing the time at which the transition matrix was recorded, and
    <transition_matrix> is a square matrix (in row-major order) representing the transition rates between
    different species.

    Example:
    >>> ti_matrix, tf_matrix = read_transition_matrix('transition_matrix.txt', 'species1', 0.0, 1.0)
    """
    ti_switch = False
    tf_switch = False
    spec_switch = False
    ti_matrix = []
    tf_matrix = []
    with open(FileName, 'r') as file:
        for line in file.readlines():
            if line[0:5] == 'time:':
                if float(line.split(' ')[1]) == InitialTime:
                    ti_switch = True
                if float(line.split(' ')[1]) == FinalTime:
                    tf_switch = True
                if float(line.split(' ')[1]) != InitialTime:
                    ti_switch = False
                if float(line.split(' ')[1]) != FinalTime:
                    tf_switch = False
            if line[0:8] == 'lifetime':
                ti_switch = False
                tf_switch = False
                spec_switch = False
            if line[0:4] == 'size':
                ti_switch = False
                tf_switch = False
                spec_switch = False
            if line[0:4] == SpeciesName:
                spec_switch = True
            if ti_switch and spec_switch:
                if line != SpeciesName + '\n':
                    info = line.strip(' ').strip('\n').split(' ')
                    temp_list = []
                    for i in info:
                        temp_list.append(int(i))
                    ti_matrix.append(temp_list)
            if tf_switch and spec_switch:
                if line != SpeciesName + '\n':
                    info = line.strip(' ').strip('\n').split(' ')
                    temp_list = []
                    for i in info:
                        temp_list.append(int(i))
                    tf_matrix.append(temp_list)
    ti_matrix = np.array(ti_matrix)
    tf_matrix = np.array(tf_matrix)
    return ti_matrix, tf_matrix


