# Testcases for v1 in TI3.25s
# MG
# 2025-03-03 14:56

import pytest

from aufgabe import *

def test_point_ladder():
    hi=10
    lo=7
    pts = point_ladder(hi,lo)
    assert str(hi) == pts[0]
    assert str(lo) == pts[-1]

def test_mark_ladder():
    hi=20
    lo=5
    for name,m in MARKSCALES.items():
        ml = mark_ladder(m,hi-lo+1)
        assert m[0]  == ml[0]
        assert m[-1] == ml[-1]
        assert hi-lo+1== len(ml)

    with pytest.raises(Exception) as e:
        mark_ladder(m,2)

def test_as_dict():
    hi=20
    lo=8
    for name,scala in MARKSCALES.items():
        d = as_dict(scala, hi,lo)
        assert hi-lo+1 == len(d)


def test_as_text():
    hi=20
    lo=10

    for name,scala in MARKSCALES.items():
        d = as_dict(scala, hi,lo)
        txt = as_text(d)
        n = len(txt.splitlines())
        assert hi-lo+1 == n

def test_getmark():
    hi=90
    lo=36
    pt="50"
    def doit(table,expect):
        d = as_dict(table, hi,lo)
        m = getmark(d,pt)
        assert expect == m

    doit(marks_HM, "3.3")
    doit(marks_AE, "D")
    doit(marks_14, "3")
    #
    for name,scala in MARKSCALES.items():
        d = as_dict(scala, hi,lo)
        m = getmark(d,"999")
        assert scala[0] == m
        m = getmark(d,"1")
        assert NB == m

"""
pytest will run all files of the form
    test_*.py or *_test.py
in the current directory and its subdirectories.
More generally, it follows standard test discovery rules.

Pytest will capture stdout and stderr. overcome: either option -s (= --capture=no)
or each testcase use capsys
def test_example(capsys): ... captured = capsys.readouterr(), captured.out is a string.
or same but "locally"
def test_example(capsys):
   with capsys.disabled():
        print("This will print directly to stdout")
"""
"""
test_it.py kann als pos. und neg.test ausgeführt werden:
pytest test.py // test cases, mostly neg.
python test.py // run = pos.tests, Gutfall, visual behaviour
"""

"""generally: Errors shall be handled via Exceptions (like IndexError) Exception
"""
##################
import inspect
def check_impl(f):
    """helper for normal run to skip unimplemented functions"""
    name=f.__name__
    if 'pass' in inspect.getsource(f):
        print(f"*** function '{name}  not yet implemented ***")
        return False
    else:
        print(f"--- running function '{name}' ---")
        return True


###############
#   M A I N   #
###############
if __name__ == "__main__":
    count=0

    # point_ladder
    if check_impl(point_ladder):
        count +=1
        hi=20
        lo=10
        pts = point_ladder(hi,lo)
        print(pts)

    # mark_ladder
    if check_impl(mark_ladder):
        count +=1
        for n,m in MARKSCALES.items():
            mks = mark_ladder(m,hi-lo+1)
            print(n,mks,sep=": ")

    # as_dict
    if check_impl(as_dict):
        count +=1

        d=as_dict(marks_AE,hi,lo) # should not be None
        assert hi-lo+1 == len(d)
        for k,v in d.items(): print(k,v)

    # as_text
    if check_impl(as_text):
        count +=1

        table = as_dict(marks_14, hi,lo)
        print("Notentabelle:", as_text(table),sep="\n")

    # getmark
    if check_impl(getmark):
        count +=1

        pt="7"
        print("pt =", pt, "-> mark =", getmark(table,pt))
        pt="0"
        print("pt =", pt, "-> mark =", getmark(table,pt))

    if count >= 5:
        print("OK, bye")
    else:
        print("... some functions are still missing")
