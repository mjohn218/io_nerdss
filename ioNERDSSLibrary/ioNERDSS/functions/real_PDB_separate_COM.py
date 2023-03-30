def real_PDB_separate_COM(Result: tuple):
    reaction_chain, new_int_site, new_int_site_distance, unique_chain, COM, angle, normal_point_lst1, normal_point_lst2, one_site_chain = Result
    for i in range(len(unique_chain)):
        for k in range(len(reaction_chain)):
            for j in range(2):
                if unique_chain[i] == reaction_chain[k][j]:
                    for l in range(3):
                        new_int_site[k][j][l] = new_int_site[k][j][l] - COM[i][l]
        for m in range(3):
            COM[i][m] = 0.0
    print('COM is normalized as [0.000, 0.000, 0.000]')
    return reaction_chain, new_int_site, new_int_site_distance, unique_chain, COM, angle, normal_point_lst1, normal_point_lst2, one_site_chain


