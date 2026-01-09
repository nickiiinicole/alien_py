# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# 1. Obtener la ruta absoluta del directorio donde está conf.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Subir dos niveles para llegar a la raíz del proyecto (alien_py)
project_root = os.path.abspath(os.path.join(current_dir, '../../'))

# 3. Apuntar a la carpeta 'src' (porque tu paquete está dentro de src)
sys.path.insert(0, os.path.join(project_root, 'src'))
sys.path.insert(0, os.path.join(project_root, 'src', 'alien')) # Por si acaso

project = 'Alien Game'
copyright = '2026, Nickiniiicole'
author = 'Nickiniiicole'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon' # esta es para el google style
]

templates_path = ['_templates']
exclude_patterns = [

]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
# --- Configuración para CSS Personalizado ---

# Asegúrate de que esta línea esté (suele estar por defecto):
html_static_path = ['_static']

# Añade esta función para cargar tu CSS:
def setup(app):
    app.add_css_file('custom.css')



ç