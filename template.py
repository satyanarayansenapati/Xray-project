import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s : ')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utilis/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'
]


#loop to create all the files in the list
for path in list_of_files:
    filepath = Path(path)

    #splliting the path and file
    file_dir, file_name = os.path.split(filepath)

    #creating the folder
    if file_dir !='':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f'Creating directory {file_dir} for the file {file_name}')



    #creating the file
    if (not os.path.exists(filepath)) or (os.path.getsize == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file path {filepath}')
    else:
        logging.info(f'{file_name} already exists')
