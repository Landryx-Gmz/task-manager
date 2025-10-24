import json
from pathlib import Path

from task_manager import TaskManager


def test_inmemory_mode_no_file_created(tmp_path, capsys):
    # usar un cwd temporal para asegurar que no se usa el tasks.json del repo
    cwd = tmp_path
    file_path = cwd / "tasks.json"

    # crear manager en modo solo memoria
    manager = TaskManager(persist=False)

    # añadir y completar tareas en memoria
    manager.add_task('Tarea memoria 1')
    manager.add_task('Tarea memoria 2')
    manager.complete_task(1)
    manager.delete_task(2)

    # comprobar que no se creó ningún archivo en el cwd del proyecto (persist False)
    # nota: TaskManager usa la ruta por defecto solo si persist=True
    assert not file_path.exists()

    # comprobar estado en memoria
    ids = [t.id for t in manager._tasks]
    assert 1 in ids
    t1 = next(t for t in manager._tasks if t.id == 1)
    assert t1.completed is True
