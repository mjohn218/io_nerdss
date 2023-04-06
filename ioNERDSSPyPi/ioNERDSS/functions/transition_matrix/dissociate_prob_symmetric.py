import numpy as np
import matplotlib.pyplot as plt
import warnings
from .read_transition_matrix import read_transition_matrix


def dissociate_prob_symmetric(FileName: str, FileNum: int, InitialTime: float, FinalTime: float,
                              SpeciesName: str, DivideSize: int = 2, ShowFig: bool = True, SaveFig: bool = False):
    """
    Calculates and displays the probability of dissociation of complexes of different sizes into other complexes of different sizes.

    Args:
        FileName (str): Path to the '.dat' file representing the histogram data to be analyzed.
        FileNum (int): Number of input files. If multiple files are provided, their names should obey the naming rule described below.
        InitialTime (float): The initial time that users desire to examine (in seconds).
        FinalTime (float): The final time that users desire to examine (in seconds).
        SpeciesName (str): The name of the species that users want to examine, identical to the name written in the input (.inp and .mol) files.
        DivideSize (int, optional): The value that distinguishes the size of the dissociate complex (default=2). For example, if DivideSize=2, that means the dissociate events are classified as 'dissociate size < 2', 'dissociate size = 2' and 'dissociate size > 2'.
        ShowFig (bool, optional): If True, the plot will be displayed (default=True).
        SaveFig (bool, optional): If True, the plot will be saved as a '.png' file in the current directory (default=False).

    Returns:
        tuple: A tuple of four numpy arrays representing the x-axis data, y-axis data, errors in y-axis data, and the bin size. If the plot is not shown or saved, returns a tuple of None values.
        
    Raises:
        ValueError: If the value of FinalTime is smaller than InitialTime, or the range of InitialTime and FinalTime is beyond the range of simulation.
        
    Note:
        If a single file is provided, the input file should be named as its original name ('transition_matrix_time.dat'). If multiple files are provided, the name of the input file should include a serial number as 'transition_matrix_time_X.dat' where X = 1, 2, 3, 4, 5, etc.
        
        The function generates a line plot of the probability of dissociation of complexes of different sizes into other complexes of different sizes. The x-axis represents the size of the complex, and the y-axis represents the dissociate probability. Three lines will exist in the line graph, representing dissociating to complexes of sizes less than, equal to, or greater than the specified size, respectively. 'Symmetric' in the function name means that for the dissociate reaction, both sizes of complexes are counted as dissociating events symmetrically, for example, if a dissociate event occurs where a heptamer dissociates into a tetramer and a trimer, then this event is counted twice, which are heptamer dissociates to tetramer and heptamer dissociates to trimer. If multiple input files are given, the output plot will be the average value of all files and an error bar will also be included.
    """
    warnings.filterwarnings('ignore')
    matrix_list = []
    file_name_head = FileName.split('.')[0]
    file_name_tail = FileName.split('.')[1]
    for i in range(1, FileNum+1):
        temp_file_name = file_name_head + '_' + str(i) + '.' + file_name_tail
        if FileNum == 1:
            temp_file_name = FileName
        ti_matrix, tf_matrix = read_transition_matrix(
            temp_file_name, SpeciesName, InitialTime, FinalTime)
        matrix = tf_matrix - ti_matrix
        matrix_list.append(matrix)
    above = []
    equal = []
    below = []
    for k in range(len(matrix_list)):
        above_temp = np.zeros(len(matrix_list[0][0]))
        equal_temp = np.zeros(len(matrix_list[0][0]))
        below_temp = np.zeros(len(matrix_list[0][0]))
        i = 0
        while i < len(matrix_list[k][0]):
            j = 0
            while j < len(matrix_list[k][i]):
                if i > j:
                    if j + 1 == DivideSize:
                        equal_temp[i] += matrix_list[k][j][i]
                    elif j + 1 > DivideSize:
                        above_temp[i] += matrix_list[k][j][i]
                    else:
                        below_temp[i] += matrix_list[k][j][i]
                j += 1
            i += 1
        above.append(above_temp)
        equal.append(equal_temp)
        below.append(below_temp)
    above_prob = []
    equal_prob = []
    below_prob = []
    for i in range(len(above)):
        above_prob_temp = np.array([])
        equal_prob_temp = np.array([])
        below_prob_temp = np.array([])
        for j in range(len(above[0])):
            sum = above[i][j] + equal[i][j] + below[i][j]
            if sum != 0:
                above_prob_temp = np.append(above_prob_temp, above[i][j]/sum)
                equal_prob_temp = np.append(equal_prob_temp, equal[i][j]/sum)
                below_prob_temp = np.append(below_prob_temp, below[i][j]/sum)
            else:
                above_prob_temp = np.append(above_prob_temp, np.nan)
                equal_prob_temp = np.append(equal_prob_temp, np.nan)
                below_prob_temp = np.append(below_prob_temp, np.nan)
        above_prob.append(above_prob_temp)
        equal_prob.append(equal_prob_temp)
        below_prob.append(below_prob_temp)
    above_prob_rev = []
    for i in range(len(above_prob[0])):
        temp = []
        for j in range(len(above_prob)):
            temp.append(above_prob[j][i])
        above_prob_rev.append(temp)
    equal_prob_rev = []
    for i in range(len(equal_prob[0])):
        temp = []
        for j in range(len(equal_prob)):
            temp.append(equal_prob[j][i])
        equal_prob_rev.append(temp)
    below_prob_rev = []
    for i in range(len(below_prob[0])):
        temp = []
        for j in range(len(below_prob)):
            temp.append(below_prob[j][i])
        below_prob_rev.append(temp)
    mean_above = []
    mean_equal = []
    mean_below = []
    std_above = []
    std_equal = []
    std_below = []
    for i in range(len(above_prob_rev)):
        mean_above.append(np.nanmean(above_prob_rev[i]))
        mean_equal.append(np.nanmean(equal_prob_rev[i]))
        mean_below.append(np.nanmean(below_prob_rev[i]))
        if FileNum != 1:
            std_above.append(np.nanstd(above_prob_rev[i]))
            std_equal.append(np.nanstd(equal_prob_rev[i]))
            std_below.append(np.nanstd(below_prob_rev[i]))
    mean_above = np.nan_to_num(mean_above)
    mean_equal = np.nan_to_num(mean_equal)
    mean_below = np.nan_to_num(mean_below)
    n_list = list(range(1, 1 + len(matrix_list[0])))
    if ShowFig:
        errorbar_color_1 = '#c9e3f6'
        errorbar_color_2 = '#ffe7d2'
        errorbar_color_3 = '#d7f4d7'
        plt.plot(n_list, mean_above, 'C0')
        plt.plot(n_list, mean_equal, 'C1')
        plt.plot(n_list, mean_below, 'C2')
        if FileNum != 1:
            plt.errorbar(n_list, mean_above, yerr=std_above,
                         ecolor=errorbar_color_1, capsize=2)
            plt.errorbar(n_list, mean_equal, yerr=std_equal,
                         ecolor=errorbar_color_2, capsize=2)
            plt.errorbar(n_list, mean_below, yerr=std_below,
                         ecolor=errorbar_color_3, capsize=2)
        plt.legend(['Dissociate Size > ' + str(DivideSize), 'Dissociate Size = ' +
                    str(DivideSize), 'Dissociate Size < ' + str(DivideSize)])
        plt.xlabel('Number of ' + str(SpeciesName) + ' in Single Complex')
        plt.ylabel('Probability')
        plt.xticks(ticks=n_list)
        plt.title('Symmetric Dissociation Probability')
        if SaveFig:
            plt.savefig('dissociate_probability_symmetric.png', dpi=500)
        plt.show()
    return n_list, [mean_above, mean_equal, mean_below], 'Nan', [std_above, std_equal, std_below]


