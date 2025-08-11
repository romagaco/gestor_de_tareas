📋 To-Do App
¡Bienvenido/a a To-Do App, una aplicación web sencilla y funcional para gestionar tus tareas diarias! Construida con Django, esta aplicación te permite organizar tu tiempo de manera eficiente con funcionalidades como registro de usuarios, inicio de sesión, creación de tareas, visualización de listas de tareas y un calendario integrado.
🚀 Características

Registro de Usuarios: Crea una cuenta personalizada para gestionar tus tareas.
Inicio de Sesión: Accede de forma segura a tu espacio personal.
Nueva Tarea: Añade tareas con detalles como título, descripción y fechas límite.
Lista de Tareas: Visualiza todas tus tareas en una interfaz clara y ordenada.
Calendario: Organiza tus tareas con un calendario interactivo para un mejor seguimiento.

🛠️ Tecnologías Utilizadas

Backend: Django 4.2.23
Frontend: HTML, CSS, Bootstrap 5 (con django-bootstrap-v5 y crispy-bootstrap5)
Gestión de Imágenes: Pillow 11.3.0
Otras Librerías: BeautifulSoup4, django-crispy-forms, y más (ver requisitos completos abajo)

📦 Requisitos
Asegúrate de tener instalado Python 3.8+ y pip. Los paquetes necesarios están listados en el archivo requirements.txt:

asgiref==3.9.1
beautifulsoup4==4.13.4
crispy-bootstrap5==2025.6
Django==4.2.23
django-bootstrap-v5==1.0.11
django-crispy-forms==2.4
pillow==11.3.0
soupsieve==2.7
sqlparse==0.5.3
typing_extensions==4.14.1
tzdata==2025.2

⚙️ Instalación
Sigue estos pasos para configurar el proyecto en tu máquina local:

Clona el repositorio:
https://github.com/romagaco/gestor_de_tareas



Crea un entorno virtual:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate


Instala los requisitos:
pip install -r requirements.txt


Configura la base de datos:
python manage.py migrate


Inicia el servidor:
python manage.py runserver


Abre tu navegador en http://localhost:8000 y ¡disfruta de la aplicación!


📝 Uso

Registro: Ve a /register para crear una cuenta.
Inicio de Sesión: Usa /login para acceder.
Crear Tarea: Dirígete a la sección de "Nueva Tarea" para añadir tareas.
Lista de Tareas: Consulta todas tus tareas en la página principal.
Calendario: Visualiza tus tareas en el calendario para planificar tu semana.

🌟 Contribuciones
¡Las contribuciones son bienvenidas! Si quieres mejorar la aplicación, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m "Añadir nueva funcionalidad").
Sube los cambios (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.

📜 Licencia
Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo y modificarlo según tus necesidades.
📬 Contacto
Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactarme a través de roberdex26@gmail.com o romagacotech@gmail.com

⭐ ¡No olvides darle una estrella al repositorio si te gusta el proyecto! ⭐
