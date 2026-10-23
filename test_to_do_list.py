from to_do_list import delete_task, show_progress
def show_progress_judge():
    tasks=[
        {"description":"buy milk","done":False},
        {"description":"finish week5","done":True},
        {"description":"read book","done":False}
    ]
    finished,waiting=show_progress(tasks)
    assert finished==1
    assert waiting==2
def test_progress_judge_empty():
    finished,waiting=show_progress([])
    assert finished==0
    assert waiting==0
def test_delete_task_valid(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda prompt:"1")
    tasks=[
        {"description":"task A","done":False},
        {"description":"task B","done":True}
    ]
    result=delete_task(tasks)
    assert result is True
    assert len(tasks)==1
    assert tasks[0]["description"]=="task B"
def test_delete_task_invalid(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda prompt:"99")
    tasks=[{"description":"task A","done":False}]
    result=delete_task(tasks)
    assert result is False