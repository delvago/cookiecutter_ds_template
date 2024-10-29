# {{cookiecutter.project_name}}

Proyecto creado por {{cookiecutter.author_name}}.

## Descripción

{{cookiecutter.project_description}}

- **data/**: Contiene todos los datos sin procesar y los datos procesados.
- **notebooks/**: Contiene todos los notebooks de Jupyter para análisis exploratorio y modelado.
- **src/**: Código fuente que contiene scripts para procesamiento de datos y modelos.
- **tests/**: Contiene pruebas unitarias para asegurar la calidad del código.

## Requisitos
- Python {{cookiecutter.python_version}}
- Dependencias: Ver 'environment.yml' o 'requirements.txt' para instalar las bibliotecas necesarias.

## Instalación
Para configurar el entorno, ejecuta el siguiente comando:

```bash
conda env create -f environment.yml
```