from geomancy import Figure, Shield

def test_easy_figure():
    seed = [1,2,1,2]
    a = Figure(*seed)
    assert a.nums == seed

def test_hard_figure():
    seed = [0,3,6,2]
    answer = [2,1,2,2]
    a = Figure(*seed)
    assert a.nums == answer

def test_add():
    a = Figure(1,2,1,2)
    b = Figure(1,2,2,1)
    answer = Figure(2,2,1,1)
    assert answer == (a + b)

def run_test():
    new_vals = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    moms = []
    for i in range(4):
        moms.append(Figure(*new_vals[i*4:(i*4)+4]))
    return Shield(*moms)
