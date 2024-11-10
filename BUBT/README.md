## Note please delete the venv file (also have inside one) and create new after you can follow the process and run the project.

1. ### Prepare project directory
    - Make your project directory (must be the same name as your github repository name)
    - Work from the project directory as current directory using `cd`.
    - Create a virtual environment using `python`. (Test via `python -V`. Must be python 3.6+)
    - `Activate` the virtual environment. (Windows: `source venv/Scripts/activate`)
    - Install `Django` using `pip`.
    ```shell script
    mkdir <project_name> && cd $_
    python -m venv venv
    source venv/bin/activate
    # Windows: source venv/Scripts/activate
    python -m pip install --upgrade pip
    ```

2. ### Install Django and startproject
    - Install `Django` v3 using `pip` within your `venv`
    ```shell script
    pip install django
    python -m pip install Pillow
    pip install celery
    sudo apt-get update
    sudo apt-get install redis-server
    ```
