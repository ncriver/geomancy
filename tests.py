from geomancy import Geofigure, Geoshield

def run_test():
    new_vals = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    moms = []
    for i in range(4):
        moms.append(Geofigure(*new_vals[i*4:(i*4)+4]))
    return Geoshield(*moms)
