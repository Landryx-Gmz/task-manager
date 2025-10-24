# TaskManager

Un gestor de tareas inteligente que combina la gestión tradicional de tareas con la capacidad de desglosar tareas complejas en subtareas manejables utilizando inteligencia artificial.

## 🌟 Características

- Gestión básica de tareas (añadir, listar, completar, eliminar)
- Desglose automático de tareas complejas usando IA (OpenAI GPT-3.5)
- Persistencia de datos en formato JSON
- Interfaz de línea de comandos intuitiva
- Marcado visual de tareas completadas

## 🛠️ Requisitos Previos

- Python 3.x
- API key de OpenAI (para funcionalidades de IA)
- Las dependencias listadas en `requirements.txt`

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Landryx-Gmz/task-manager.git
cd task-manager
```

2. Crea y activa un entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura tu API key de OpenAI:
   - Crea un archivo `.env` en la raíz del proyecto
   - Añade tu API key: `OPENAI_API_KEY=tu_api_key_aquí`

## 💻 Uso

Ejecuta el programa:
```bash
python main.py
```

### Menú de Opciones:
1. Añadir tarea simple
2. Añadir tarea compleja (usando IA)
3. Listar tareas
4. Completar tarea
5. Eliminar tarea
6. Salir

## 🧪 Tests

El proyecto incluye tests unitarios. Para ejecutarlos:
```bash
pytest tests/
```

## 📁 Estructura del Proyecto

- `main.py`: Punto de entrada y menú interactivo
- `task_manager.py`: Lógica principal de gestión de tareas
- `ai_service.py`: Servicios de IA para desglose de tareas
- `tests/`: Pruebas unitarias
- `tasks.json`: Almacenamiento persistente de tareas (generado automáticamente)

## 📝 Licencia

Este proyecto está bajo la Licencia Apache 2.0 - ver el archivo [LICENSE](LICENSE) para más detalles.

## ✨ Características de la IA

El sistema utiliza GPT-3.5 de OpenAI para:
- Analizar tareas complejas
- Desglosar en 3-5 subtareas accionables
- Generar pasos claros y específicos

## 👥 Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request 
