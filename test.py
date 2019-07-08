from percent import percent

def test_percent():
    p=percent(100,10)
    assert p == 10
    a="10"
    b="0"
    p=percent(a,b)
    assert p == "Invalid Arguments"