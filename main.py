from task_manager import TaskManager
from ai_service  import create_simple_task


def print_menu():
    print("\n--- GESTOR DE TAREAS INTELIGENTE ----")
    print("1. Añadir tarea")
    print("2. Añadir tarea compleja (con IA)")
    print("3. Listar tarea")
    print("4. Completar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")


def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:

            choise = int(input("\nElige una opcion: "))

            match choise:
                case 1:
                    description = input("Descripcion de la tares: ")
                    manager.add_task(description)

                case 2:
                    description = input("Descripcion de la tares compleja: ")
                    subtasks =create_simple_task(description)
                    
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"): 
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break

                case 3:
                    manager.list_tasks()

                case 4:
                    id = int(input("id de la tarea que completaste: "))
                    manager.complete_task(id)

                case 5:
                    id = int(input("id de la tarea a eliminar: "))
                    manager.delete_task(id)

                case 6:
                    print("Saliendo....")
                    break

                case _:
                    print("Opción no válida. Seleccione otra.")
        except ValueError:
            print("Opción no válida. Seleccione otra.")



if __name__ == "__main__":
    main()