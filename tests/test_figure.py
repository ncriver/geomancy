from .context import structures
from itertools import product
Shield = structures.Shield
Figure = structures.Figure

def test_easy_figure():
    seed = (1,2,1,2)
    a = Figure(*seed)
    assert a.nums == seed

def test_hard_figure():
    seed = (0,3,6,2)
    answer = (2,1,2,2)
    a = Figure(*seed)
    assert a.nums == answer

def test_names():
    total_num_figures = 16
    dots = product((1,2),repeat=4)
    figures = {}
    for d in dots:
        figures[d] = Figure(*d)
        assert figures[d].name != 'Unset'
    assert len(figures) == total_num_figures

def test_correct_name():
    a = Figure(1,1,2,1)
    correct_name = 'Puer'
    assert a.name == correct_name

def test_add():
    a = Figure(1,2,1,2)
    b = Figure(1,2,2,1)
    answer = Figure(2,2,1,1)
    assert answer == (a + b)

def test_latin_names():
    cls_dict = Figure.latin_names
    a = Figure.quick_throw()
    obj_dict = a.latin_names
    assert cls_dict == obj_dict
    assert 'Puella' in obj_dict.values()


def run_test():
    new_vals = [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    moms = []
    for i in range(4):
        moms.append(Figure(*new_vals[i*4:(i*4)+4]))
    return Shield(*moms)
