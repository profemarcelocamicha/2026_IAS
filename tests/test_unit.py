from app.services import hello

def test_hello():
    assert hello() == "Hello World"
