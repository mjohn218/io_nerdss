import numpy as np
import matplotlib.pyplot as plt
import warnings
from .read_multi_hist import read_multi_hist


def multi_3D_hist(FileName: str, FileNum: int, InitialTime: float, FinalTime: float,
                  SpeciesList: list, xAxis: str, yAxis: str, xBarSize: int = 1, yBarSize: int = 1,
                  ShowFig: bool = True, SaveFig: bool = False):
    """ Creates 3D Histogram from a histogram.dat (multi-species) that shows the distribution of size of the different species.

    Args:
        FileName (str): Path to the histogram.dat file
        FileNum (int): Number of the total input files (file names should be [fileName]_1,[fileName]_2,...)
        InitialTime (float): The starting time. Must not be smaller / larger then times in file.
        FinalTime (float): The ending time. Must not be smaller / larger then times in file.
        SpeciesList (list): The names of the species you want to examine. Should be in the .dat file.
        xAxis (str): Species shown on X-axis.
        yAxis (str): Species shown on Y-axis.
        xBarSize (int, optional): The size of each data bar in the X-dimension. Defaults to 1.
        yBarSize (int, optional): The size of each data bar in the Y-dimension. Defaults to 1.
        ShowFig (bool, optional): If the plot is shown. Defaults to True.
        SaveFig (bool, optional): If the plot is saved. Defaults to False.

    Returns:
        3D Histogram. X-axis / Y-axis: the distribution of sizes of each specified species. Z-axis: relative occurance of each complex.
    """
    warnings.filterwarnings('ignore')
    file_name_head = FileName.split('.')[0]
    file_name_tail = FileName.split('.')[1]
    count_list_sum = []
    for i in range(1, FileNum+1):
        temp_file_name = file_name_head + '_' + str(i) + '.' + file_name_tail
        if FileNum == 1:
            temp_file_name = FileName
        x_size_list = []
        y_size_list = []
        hist_list = read_multi_hist(temp_file_name, SpeciesList=SpeciesList)
        for j in range(len(hist_list)):
            if hist_list[j] != []:
                time = hist_list[j][0]
                if InitialTime <= time <= FinalTime:
                    for k in range(len(hist_list[j])):
                        if k != 0:
                            if xAxis in SpeciesList and yAxis in SpeciesList:
                                x_name_index = SpeciesList.index(xAxis)
                                true_x_size = hist_list[j][k][x_name_index]
                                x_size = int(true_x_size / xBarSize)
                                y_name_index = SpeciesList.index(yAxis)
                                true_y_size = hist_list[j][k][y_name_index]
                                y_size = int(true_y_size / yBarSize)
                                if x_size not in x_size_list:
                                    if len(x_size_list) == 0:
                                        for m in range(0, x_size+1):
                                            x_size_list.append(m)
                                    else:
                                        if x_size - x_size_list[-1] == 1:
                                            x_size_list.append(x_size)
                                        else:
                                            diff = x_size - x_size_list[-1]
                                            for m in range(x_size_list[-1]+1, x_size+1):
                                                x_size_list.append(m)
                                if y_size not in y_size_list:
                                    if len(y_size_list) == 0:
                                        for m in range(0, y_size+1):
                                            y_size_list.append(m)
                                    else:
                                        if y_size - y_size_list[-1] == 1:
                                            y_size_list.append(y_size)
                                        else:
                                            for m in range(y_size_list[-1]+1, y_size+1):
                                                y_size_list.append(m)
                            else:
                                print('xAxis or yAxos not in SpeciesList!')
                                return 0
        count_list = np.zeros([len(y_size_list), len(x_size_list)])
        data_count = 0
        for j in range(len(hist_list)):
            if hist_list[j] != []:
                time = hist_list[j][0]
                if InitialTime <= time <= FinalTime:
                    data_count += 1
                    for k in range(len(hist_list[j])):
                        if k != 0:
                            count = hist_list[j][k][-1]
                            x_name_index = SpeciesList.index(xAxis)
                            x_size = hist_list[j][k][x_name_index]
                            x_size = int(x_size / xBarSize)
                            y_name_index = SpeciesList.index(yAxis)
                            y_size = hist_list[j][k][y_name_index]
                            y_size = int(y_size / yBarSize)
                            count_list[y_size][x_size] += count
        count_list = count_list/data_count
        count_list_sum.append(count_list)
    max_x = 0
    max_y = 0
    for i in count_list_sum:
        if len(i[0]) > max_x:
            max_x = len(i[0])
        if len(i) > max_y:
            max_y = len(i)
    count_list_sum_ = []
    for i in range(len(count_list_sum)):
        temp_matrix = np.zeros([max_y, max_x])
        for j in range(len(count_list_sum[i])):
            for k in range(len(count_list_sum[i][j])):
                temp_matrix[j][k] += count_list_sum[i][j][k]
        count_list_sum_.append(temp_matrix)
    count_list_mean = np.zeros([max_y, max_x])
    count_list_std = np.zeros([max_y, max_x])
    for i in range(len(count_list_sum_[0])):
        for j in range(len(count_list_sum_[0][0])):
            temp_list = []
            for k in range(len(count_list_sum_)):
                temp_list.append(count_list_sum_[k][i][j])
            count_list_mean[i][j] += np.mean(temp_list)
            count_list_std[i][j] += np.std(temp_list)
    x_list = np.arange(0, max_x) * xBarSize
    y_list = np.arange(0, max_y) * yBarSize
    if ShowFig:
        xx, yy = np.meshgrid(x_list, y_list)
        X, Y = xx.ravel(), yy.ravel()
        Z = count_list_mean.ravel()
        width = xBarSize
        depth = yBarSize
        bottom = np.zeros_like(Z)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.bar3d(X, Y, bottom, width, depth, Z, shade=True)
        ax.set_xlabel('Number of ' + xAxis + ' in sigle complex')
        ax.set_ylabel('Number of ' + yAxis + ' in sigle complex')
        ax.set_zlabel('Relative Occurrence Probability')
        ax.set_title('Complex Distribution of ' + xAxis + ' and ' + yAxis)
        fig.tight_layout()
        plt.xlabel('Count of ' + xAxis)
        plt.ylabel('Count of ' + yAxis)
        if SaveFig:
            plt.savefig('3D_hisogram_of_' + xAxis + '_and_' +
                        yAxis, dpi=500,  bbox_inches='tight')
        plt.show()
    return x_list, y_list, count_list_mean, 'Nan'


# --------------------------------Locate Position by Pdb or Restart----------------------------------

