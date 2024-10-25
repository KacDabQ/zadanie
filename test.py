import io
import main

def test_pierwiastek():
    result = main.pierwiastek(4,6)
    assert result == 2.0

def test_pierwiastek2():
    result = main.pierwiastek(9,6)
    assert result == 3.0

def test_user_input3(monkeypatch):
    buffer = io.StringIO()
    buffer.write('4\n6\n')
    buffer.seek(0)
    monkeypatch.setattr('sys.stdin', buffer)
    result = main.main()
    assert result == 2.0