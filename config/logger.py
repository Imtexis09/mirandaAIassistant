import logging
import sys
import os

# Asegurar que exista la carpeta de logs
os.makedirs("logs", exist_ok=True)

def setup_logger():
    logger = logging.getLogger("MirandaCore")
    logger.setLevel(logging.DEBUG)

    # Formato del log
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Salida por consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Salida a archivo
    file_handler = logging.FileHandler("logs/miranda.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

log = setup_logger()