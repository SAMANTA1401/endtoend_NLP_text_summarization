import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
     ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # separate file directory and file name

    # for creating filedir
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # create directory if not exist
        logging.info(f"Created directory: {filedir} for the file name {filename}")

    #for creating filename
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0 ): #if filepath (filename) is not exist or size of the file is zero. 
        # then only created the file if file is already present and contain some code then the file is not created
        # neither i lose my code inside the file if it is empty then it will replaced
        with open(filename, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")
