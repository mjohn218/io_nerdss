import math
from ..gen_platonic.distance import distance


def cube_face_leg_reduce(COM: float, leg: float, sigma: float):
    n = 12
    angle = math.acos(0)
    red_len = sigma/(2*math.sin(angle/2))
    ratio = 1 - red_len/distance(COM, leg)
    leg_red = []
    for i in range(0, 3):
        leg_red.append(round((leg[i] - COM[i])*ratio + COM[i], n))
    return leg_red

