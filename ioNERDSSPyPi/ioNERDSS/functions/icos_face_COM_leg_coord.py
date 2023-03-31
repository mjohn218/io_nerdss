from .mid_pt import mid_pt
from .icos_face_COM_coord import icos_face_COM_coord


def icos_face_COM_leg_coord(a: float, b: float, c: float):
    COM_leg = []
    COM_leg.append(icos_face_COM_coord(a, b, c))
    COM_leg.append(mid_pt(a, b))
    COM_leg.append(mid_pt(b, c))
    COM_leg.append(mid_pt(c, a))
    return COM_leg

