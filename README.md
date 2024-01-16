# fonasa-project
1. **Crear conexión MySQL en localhost:3306**

2. Crear un entorno virtual con Python:
    ```bash
    python -m venv venv
    ```

3. Activar el entorno virtual:
    ```bash
    .\venv\Scripts\activate
    ```

4. Instalar las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

5. Realizar migraciones en la base de datos:
    ```bash
    python manage.py makemigrations
    ```

6. Aplicar las migraciones a la base de datos:
    ```bash
    python manage.py migrate
    ```

7. Iniciar el servidor local:
    ```bash
    python manage.py runserver
    ```
