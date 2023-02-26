import datetime
import importlib

import src.garb_input as garb_input

def test_1():
    assert garb_input.decipher("ap gov assignMent fEb 1") == {
        "date": datetime.date(2023, 2, 14)
    }