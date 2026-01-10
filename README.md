#PROYECTO APP DE ENVIO DE RECORDATORIO
Este es un proyecto desarrrolado con Django diseñado para la gestion  envìo de recordatorios.
El sistema permite organizar tareas o eventos y aseguar que las notificaciones lleguen de manera oportuna.

#CARACTERISTICAS
° Gestion de recordatorios
° Configuración de seguridad mediante variables de entorno
° Estructura modular escalable

#INSTALACION Y CONFIGURACION
Sigue esos pasos para ejecutar el proyecto localmente.
1 clonar el repositorio
git clone
2 crear un entorno virtual
python -m venv
3 instalar dependencias
pip install -r requiriment.txt
4 Variable de entorno 
Asegurate de configurar tu archivo env. o las variables de entorno necesarias  SECRET_KEY, DEDBUG, configuracion  de la base de datos  
5 Ejecutar migraciones 
pytho manage.py migrate 
6 Iniciar el servidor 
python manage.py runserver

# ESTRUCTURA DEL PROYECTO
- mi_proyecto/: configuraciones principales de Django
- mi_app/ : lógica de negocios, modelos y vistas de la aplicacion
- manage.py : Utilidad de linéa de comandos de Django
