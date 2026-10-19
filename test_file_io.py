"""Unit tests for the File I/O module (development stage).

At integration time these tests are copied into ``test_to_do_list.py`` and the
import line changes from ``filerw_selfedit`` to ``to_do_list``.
"""

from filerw_selfedit import load_tasks, save_tasks


def test_load_tasks_missing_file(tmp_path, monkeypatch):
    """A missing tasks.json yields an empty list instead of crashing."""
    # Arrange
    monkeypatch.chdir(tmp_path)

    # Act
    tasks = load_tasks()

    # Assert
    assert tasks == []


def test_save_and_load_tasks(tmp_path, monkeypatch):
    """Tasks written by save_tasks come back unchanged from load_tasks."""
    # Arrange
    monkeypatch.chdir(tmp_path)
    tasks = [
        {"description": "Buy milk", "done": False},
        {"description": "Write the COMP1850 report", "done": True},
    ]

    # Act
    save_tasks(tasks)
    loaded = load_tasks()

    # Assert
    assert loaded == tasks


def test_save_tasks_creates_json_file(tmp_path, monkeypatch):
    """save_tasks creates tasks.json with valid JSON content."""
    # Arrange
    monkeypatch.chdir(tmp_path)

    # Act
    save_tasks([{"description": "Buy milk", "done": False}])

    # Assert
    assert (tmp_path / DAIA_FILE).exists()


def test_load_tasks_corrupt_file_returns_empty(tmp_path, monkeypatch):
    """A malformed JSON file yields an empty list, not an exception."""
    # Arrange
    monkeypatch.chdir(tmp_path)
    (tmp_path / DATA_FILE).write_text("{not valid json", encoding="utf-8")

    # Act
    tasks = load_tasks()

    # Assert
    assert tasks == []


def test_save_empty_list_round_trip(tmp_path, monkeypatch):
    """Saving an empty list and loading it back keeps it empty."""
    # Arrange
    monkeypatch.chdir(tmp_path)

    # Act
    save_tasks([])

    # Assert
    assert load_tasks() == []
