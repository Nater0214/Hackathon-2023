import datetime

import src.garb_input as garb_input

def test_mine_1():
    assert garb_input.decipher("ap gov assignMent fEb 14") == {
        "name": "Ap Gov Assignment",
        "date": datetime.date(2023, 2, 14)
    }

def test_vibhor_1():
    assert garb_input.decipher("spanish test february 24") == {
        "name": "Spanish Test",
        "date": datetime.date(2023, 2, 24)
    }

def test_anish_1():
    assert garb_input.decipher("ap gov test march 2") == {
        "name": "Ap Gov Test",
        "date": datetime.date(2023, 3, 2)
    }

def test_vibhor_2():
    assert garb_input.decipher("submit application tomorrow") == {
        "name": "Submit Application",
        "date": datetime.date(2023, 2, 27)
    }

def test_mine_2():
    assert garb_input.decipher("old work dec 28") == {
        "name": "Old Work",
        "date": datetime.date(2022, 12, 28)
    }

def test_anish_2():
    assert garb_input.decipher("cspan may 12") == {
        "name": "Cspan",
        "date": datetime.date(2023, 5, 12)
    }