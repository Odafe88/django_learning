# Django Learning
This is a repository documenting my Django learning.
It will also serve as a reference for anyone learning django.

## Creating a Django Project
1. First you need to create a virtual environment. This ensures that whatever packages you have in your project does not cause dependency Issues in the global django module.
    To do this run this command below in your terminal
   
    ```
   python -m venv virtualenv_name_env
    ```
   This Creates a folder in your root directory.
3. Activiate the virtual environment.
   You do this by executes the Activate script in the Virtual env folder
   
   ```
   ./virtualenv_name_env/scripts/activate
   ```
4. Next step is to install django.
   
   ```
   pip3 install django
   ```
5. Next, create a Django project (PS: The project folder contains all your apps)

   ```
   django-admin startproject project_name
   ```
6. Create apps (Make sure you are in the projects directory)
   ```
   python manage.py startapp app_name
   ```
7. Finally, to start your Django server simply run
   ```
   python manage.py runserver
   ```

   ## Thank you!
