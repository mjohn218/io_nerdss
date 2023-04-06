import numpy as np
from ..gen_platonic.COM_leg_list_gen import COM_leg_list_gen
from .cube_face_COM_leg_list_gen import cube_face_COM_leg_list_gen
from .cube_face_leg_reduce import cube_face_leg_reduce

def cube_face_leg_reduce_coord_gen(radius: float, sigma: float):
    COM_leg_list = cube_face_COM_leg_list_gen(radius)
    COM_leg_red_list = []
    for elements in COM_leg_list:
        temp_list = []
        temp_list.append(np.around(elements[0], 8))
        i = 1
        while i <= 4:
            temp_list.append(np.around(cube_face_leg_reduce(
                elements[0], elements[i], sigma), 8))
            i += 1
        COM_leg_red_list.append(temp_list)
    return COM_leg_red_list

