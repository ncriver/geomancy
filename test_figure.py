from geomancy import Geofigure, Geoshield

def test_easy_figure():
    seed = [1,2,1,2]
    a = Geofigure(*seed)
    assert a.nums == seed

def test_hard_figure():
    seed = [0,3,6,2]
    answer = [2,1,2,2]
    a = Geofigure(*seed)
    assert a.nums == answer

def run_test():
    new_vals = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    moms = []
    for i in range(4):
        moms.append(Geofigure(*new_vals[i*4:(i*4)+4]))
    return Geoshield(*moms)
