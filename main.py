from task_manager import TaskManager


def print_menu():
    print("\n--- GESTOR DE TAREAS INTELIGENTE ----")
    print("1. Añadir tarea")
    print("2. Listar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


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
                    manager.list_tasks()
                case 3:
                    id = int(input("id de la tarea que completaste: "))
                    manager.complete_task(id)
                case 4:
                    id = int(input("id de la tarea a eliminar: "))
                    manager.delete_task(id)
                case 5:
                    print("Saliendo....")
                    break
                case _:
                    print("Opción no válida. Seleccione otra.")
        except ValueError:
            print("Opción no válida. Seleccione otra.")



if __name__ == "__main__":
    main()