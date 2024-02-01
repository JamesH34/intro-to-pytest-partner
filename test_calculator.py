import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_add_negative():
    assert calculator.calculate(2, -3, "add") == -1

def test_subtract():
    assert calculator.calculate(10, 5, "subtract") == 5

# Add more functional tests for subtract, multiply, and divide

    
def test_terminal_output(capsys):
    value = calculator.calculate(10, 2, "multiply")
    print("Result:", value)
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"



def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0