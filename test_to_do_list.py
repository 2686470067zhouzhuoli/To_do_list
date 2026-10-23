from to_do_list import add_task
def test_add_task_valid(monkeypatch):
    task_list = []

    monkeypatch.setattr("builtins.input",lambda _:"buy milk")
    add_task(task_list)

    assert len(task_list) == 1
    assert task_list[0]["description"] == "buy milk"
    assert task_list[0]["done"] is False

def test_add_task_empty_input(monkeypatch):
    task_list = []

    monkeypatch.setattr("builtins.input",lambda _:"")
    add_task(task_list)
    assert len(task_list) == 0