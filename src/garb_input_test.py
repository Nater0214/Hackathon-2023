import datetime

import src.garb_input as garb_input

def test_1():
    assert garb_input.decipher("ap gov assignMent fEb 14") == {
        "name": "Ap gov assignment",
        "date": datetime.date(2023, 2, 14)
    }

def test_2():
    assert garb_input.decipher("spanish test february 24") == {
        "name": "Spanish test",
        "date": datetime.date(2023, 2, 24)
    }