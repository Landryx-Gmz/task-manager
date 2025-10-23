class Task:

    def __init__(self,id, description, complete = False):
        self.id = id
        self.description = description
        self.complete = complete

    def __str__(self):
        status = "✓" if self.complete else " "
        return f"[{status}] #{self.id}: {self.description}"

class TaskManager:

    def __ini__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f'Tarea añadida {description}')


    def list_task(self):
        if not self._tasks:
            print(f'No existen tareas, crea alguna')
        else:
            for task in self._tasks:
                print(task)

    def complet_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.complete = True
                print(f"Tarea completada: {task}")
                return
        print(f"Tarea no encontrada : #{id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f'Tarea #{id} ha sido eliminada')
                return
        print(f"Tarea no encontrada : #{id}")