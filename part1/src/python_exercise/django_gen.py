import os
import os.path
from .palindrome import is_palindrome

def create_project(project_name, path='.'):
    if not os.path.exists(path):
        print('Incorrect project path provided')

    print(f'#####--Succeffully created "{project_name}" project skeleton files--#####')
    os.system(f'django-admin startproject {project_name} {path}')
