import pytest
from lab2 import load_from_csv, save_to_csv, students, addNewElement, deleteElement, updateElement

@pytest.fixture(autouse=True)
def reset_students():
    global students
    students = [
        {"name": "Lili", "surname": "Fiduk", "phone": "0967754765", "email": "Lili@email.com"},
        {"name": "Sasha", "surname": "Suska", "phone": "0636653456", "email": "Sasha@email.com"},
        {"name": "Sofi", "surname": "Derevas", "phone": "069875467", "email": "Sofi@email.com"},
        {"name": "Nadia", "surname": "Yopsis", "phone": "0968403658", "email": "Nadia@example.com"},
        {"name": "Kristina", "surname": "Ylot", "phone": "0934421435", "email": "Kristina@email.com"}
    ]

def test_load_from_csv(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("name,surname,phone,email\nLili,Fiduk,0967754765,Lili@email.com\n")
    load_from_csv(file)
    assert students[0]["name"] == "Lili"

def test_save_to_csv(tmp_path):
    file = tmp_path / "output.csv"
    save_to_csv(file)
    assert file.read_text().startswith("name,surname,phone,email")

def test_addNewElement(monkeypatch):
    inputs = iter(["Kristina", "Ylot", "0934421435", "Kristina@email.com"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    addNewElement()
    assert students[-1]["name"] == "Kristina"

def test_deleteElement(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Garik")
    deleteElement()
    assert not any(s["name"] == "Garik" for s in students)

def test_updateElement(monkeypatch):
    inputs = iter(["Nada", "Nadia", "Yopsis", "0968403658", "Nadia@example.com"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    updateElement()
    assert any(s["name"] == "Nadia" for s in students)


