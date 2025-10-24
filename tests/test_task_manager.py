import json
from pathlib import Path
import pytest

from task_manager import TaskManager, Task


def test_add_and_list_tasks(tmp_path, capsys, monkeypatch):
    # Aislar archivo de datos
    data_file = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, 'FILENAME', str(data_file))

    manager = TaskManager()
    # añadir tarea
    manager.add_task('Primera tarea')

    # comprobar salida de add
    captured = capsys.readouterr()
    assert 'Tarea añadida: Primera tarea' in captured.out

    # comprobar que el archivo se creó y contiene la tarea
    assert data_file.exists()
    data = json.loads(data_file.read_text(encoding='utf-8'))
    assert len(data) == 1
    assert data[0]['description'] == 'Primera tarea'
    assert data[0]['completed'] is False

    # comprobar list_tasks imprime la tarea
    manager.list_tasks()
    captured = capsys.readouterr()
    assert 'Primera tarea' in captured.out


def test_complete_task_and_not_found(tmp_path, capsys, monkeypatch):
    data_file = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, 'FILENAME', str(data_file))

    manager = TaskManager()
    manager.add_task('Tarea A')
    manager.add_task('Tarea B')

    # completar tarea 1
    manager.complete_task(1)
    captured = capsys.readouterr()
    assert 'Tarea completada' in captured.out
    assert 'Tarea A' in captured.out

    # comprobar estado en memoria
    t1 = next(t for t in manager._tasks if t.id == 1)
    assert t1.completed is True

    # comprobar persistencia
    data = json.loads(data_file.read_text(encoding='utf-8'))
    assert any(item['id'] == 1 and item['completed'] is True for item in data)

    # intentar completar tarea inexistente
    manager.complete_task(999)
    captured = capsys.readouterr()
    assert 'Tarea no encontrada' in captured.out


def test_delete_task_and_not_found(tmp_path, capsys, monkeypatch):
    data_file = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, 'FILENAME', str(data_file))

    manager = TaskManager()
    manager.add_task('Eliminar 1')
    manager.add_task('Eliminar 2')

    # eliminar la primera
    manager.delete_task(1)
    captured = capsys.readouterr()
    assert 'ha sido eliminada' in captured.out

    # comprobar que ya no exista en memoria ni en archivo
    ids = [t.id for t in manager._tasks]
    assert 1 not in ids
    data = json.loads(data_file.read_text(encoding='utf-8'))
    assert all(item['id'] != 1 for item in data)

    # intentar eliminar inexistente
    manager.delete_task(999)
    captured = capsys.readouterr()
    assert 'Tarea no encontrada' in captured.out


def test_persistence_load_sets_next_id(tmp_path, monkeypatch):
    data_file = tmp_path / "tasks.json"
    # crear un archivo con dos tareas
    tasks = [
        {"id": 5, "description": "Tarea 5", "completed": False},
        {"id": 7, "description": "Tarea 7", "completed": True},
    ]
    data_file.write_text(json.dumps(tasks, indent=4), encoding='utf-8')

    monkeypatch.setattr(TaskManager, 'FILENAME', str(data_file))
    manager = TaskManager()

    # debe cargar las tareas
    assert any(t.id == 5 for t in manager._tasks)
    assert any(t.id == 7 for t in manager._tasks)

    # next id debe ser la última id + 1 (usa la última en la lista cargada)
    assert manager._next_id == manager._tasks[-1].id + 1
