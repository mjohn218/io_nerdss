from .dode_vert_coord import dode_vert_coord


def dode_vert_COM_leg_gen(radius: float):
    coord = dode_vert_coord(radius)
    COM_leg_list = []
    COM_leg_list.append(dode_vert_COM_leg(
        coord[0], coord[1], coord[12], coord[16]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[1], coord[0], coord[13], coord[17]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[2], coord[3], coord[14], coord[18]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[3], coord[2], coord[15], coord[19]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[4], coord[6], coord[12], coord[14]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[5], coord[7], coord[13], coord[15]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[6], coord[4], coord[16], coord[18]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[7], coord[5], coord[17], coord[19]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[8], coord[9], coord[12], coord[13]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[9], coord[8], coord[14], coord[15]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[10], coord[11], coord[16], coord[17]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[11], coord[10], coord[18], coord[19]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[12], coord[0], coord[4], coord[8]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[13], coord[1], coord[5], coord[8]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[14], coord[2], coord[4], coord[9]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[15], coord[3], coord[5], coord[9]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[16], coord[0], coord[6], coord[10]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[17], coord[1], coord[7], coord[10]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[18], coord[2], coord[6], coord[11]))
    COM_leg_list.append(dode_vert_COM_leg(
        coord[19], coord[3], coord[7], coord[11]))
    return COM_leg_list

