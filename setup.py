# Importa la función setup (define el paquete) y find_packages (descubre paquetes automáticamente)
from setuptools import setup, find_packages

# Llama a setup() para configurar el empaquetado del proyecto
setup(
    name = "dab_project",
    version = "0.0.3",
    description = "This contains the code in the ./src directory of the project",
    author = "Kevin Gonzales",
    # Busca automáticamente todos los subpaquetes (carpetas con __init__.py) dentro de ./src
    packages = find_packages(where="./src"),
    # Indica que la raíz de los paquetes (el paquete "") está en la carpeta ./src
    package_dir = {"": "./src"},
    # Lista de dependencias necesarias para instalar este paquete
    install_requires = ["setuptools"],
    entry_points = {
        "packages": [
            "main=dab_project.main:main"
        ]
    }
)