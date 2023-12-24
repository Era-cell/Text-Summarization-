import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

folder = "text-summarization"

list_of_files = [
    ".github/workflows/.gitkeep",
    "app.py",
    "params.yaml",
    "setup.py",
    "main.py",
    "config/config.yaml",
    "Dockerfile",
    "requirements.txt",
    "research/trails.ipynb"
    f"src/{folder}/__init__.py"
    f"src/{folder}/config/configuration.py",
    f"src/{folder}/entity/__init__.py",
    f"src/{folder}/config/__init__.py",
    f"src/{folder}/utils/__init__.py",
    f"src/{folder}/utils/common.py",
    f"src/{folder}/components/__init__.py",
    f"src/{folder}/constants/__init__.py",
    f"src/{folder}/logging.py",
    f"src/{folder}/pipeline/__init__.py",
    "template.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")