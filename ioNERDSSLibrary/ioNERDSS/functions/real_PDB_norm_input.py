def real_PDB_norm_input(normal_point_lst, chain_name, chain_pair1, chain_pair2):
    normal_point_1_temp = input('Please input normal vector for ' +
                                chain_name + ' in chain ' + chain_pair1 + " & " + chain_pair2 + ' : ')
    normal_point_1_temp = normal_point_1_temp.strip('[').strip(']').split(',')
    normal_point_1_temp_ = []
    for j in normal_point_1_temp:
        normal_point_1_temp_.append(float(j))
    normal_point_lst.append(normal_point_1_temp_)
    return normal_point_lst


