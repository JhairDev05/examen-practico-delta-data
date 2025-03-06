📊 Aplicación de Gestión de Créditos con Flask

Esta aplicación permite gestionar créditos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), además de visualizar gráficos con el total de créditos otorgados.

📌 Características

Crear, listar, actualizar y eliminar créditos.

Validación de formularios.

Confirmación antes de eliminar un registro.

Gráficos dinámicos del total de créditos otorgados.

📋 Requisitos previos

Asegúrate de tener instalado lo siguiente:

Python 3.10 o superior

pip (administrador de paquetes de Python)

📦 Instalación

Clona este repositorio:

git clone <URL_DEL_REPOSITORIO>
cd nombre-del-repositorio

Crea un entorno virtual (opcional pero recomendado):

En Linux/MacOS:

python -m venv venv
source venv/bin/activate

En Windows:

python -m venv venv
venv\Scripts\activate

Instala las dependencias:

pip install -r requirements.txt

▶️ Ejecutar la aplicación

Inicia la aplicación con el siguiente comando:

python index.py

Abre tu navegador y accede a:

http://localhost:5000

📊 Uso de la aplicación

Crear un crédito: Completa el formulario y envíalo para registrar un nuevo crédito.

Actualizar un crédito: Haz clic en "Editar" para modificar un crédito existente.

Eliminar un crédito: Haz clic en "Eliminar" y confirma la acción para borrar un crédito.

Visualizar gráficos: La aplicación muestra un gráfico con el total de créditos otorgados.

🔄 Actualizar dependencias

Si agregas nuevas librerías, actualiza el archivo requirements.txt con:

pip freeze > requirements.txt

🧹 Desactivar el entorno virtual

Cuando termines, puedes salir del entorno virtual con:

deactivate

📄 Licencia

Este proyecto se encuentra bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

¡Disfruta de la aplicación! 🚀
