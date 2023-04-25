
from optimizar import Optimizar


def test_add():
    optimizar=Optimizar()
    assert len(optimizar.array) == 0
    optimizar.add(1)
    assert len(optimizar.array) == 1
    optimizar.add(2)
    assert len(optimizar.array) == 2
    optimizar.add(3)
def test_media():
    optimizar=Optimizar()
    optimizar.array.clear()
    optimizar.add(1)
    assert optimizar.media() == 1.0