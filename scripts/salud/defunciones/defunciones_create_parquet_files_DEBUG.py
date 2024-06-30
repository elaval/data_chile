#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd

# Check if running in the GitHub Actions environment
if 'GITHUB_ACTIONS' in os.environ:
    project_path = os.getcwd()
else:
    # Assuming your script is in the 'scripts' directory
    project_path = os.path.abspath(os.path.join(os.getcwd(), '../../..'))

# Add the project directory to the PYTHONPATH if it's not already there
if project_path not in sys.path:
    sys.path.append(project_path)

# Now you can import your custom module
from data_utils.data_processing import download_file, process_zip_file

# Debug: Print PYTHONPATH
print(f"PYTHONPATH: {sys.path}")

# Define headers for CSV files without headers
DEFAULT_HEADERS = [
    "AÑO", "FECHA_DEF", "SEXO_NOMBRE", "EDAD_TIPO", "EDAD_CANT", "COD_COMUNA", "COMUNA", "NOMBRE_REGION",
    "DIAG1", "CAPITULO_DIAG1", "GLOSA_CAPITULO_DIAG1", "CODIGO_GRUPO_DIAG1", "GLOSA_GRUPO_DIAG1",
    "CODIGO_CATEGORIA_DIAG1", "GLOSA_CATEGORIA_DIAG1", "CODIGO_SUBCATEGORIA_DIAG1", "GLOSA_SUBCATEGORIA_DIAG1",
    "DIAG2", "CAPITULO_DIAG2", "GLOSA_CAPITULO_DIAG2", "CODIGO_GRUPO_DIAG2", "GLOSA_GRUPO_DIAG2",
    "CODIGO_CATEGORIA_DIAG2", "GLOSA_CATEGORIA_DIAG2", "CODIGO_SUBCATEGORIA_DIAG2", "GLOSA_SUBCATEGORIA_DIAG2",
    "LUGAR_DEFUNCION"
]

def get_data_paths():
    # Check if running in the GitHub Actions environment
    if 'GITHUB_ACTIONS' in os.environ:
        base_path = os.getcwd()
    else:
        # Assuming your script is in the 'scripts' directory
        base_path = os.path.abspath(os.path.join(os.getcwd(), '../../../data'))

    source_path = os.path.join(base_path, "source/salud/defunciones")
    processed_path = os.path.join(base_path, "processed/salud/defunciones")
    
    # Debug: Print base path and data paths
    print(f"Base Path: {base_path}")
    print(f"Source Path: {source_path}")
    print(f"Processed Path: {processed_path}")
    
    return source_path, processed_path

# Create directories if they don't exist
source_dir, processed_dir = get_data_paths()
os.makedirs(source_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)

# Debug: List files in source and processed directories
print(f"Files in source directory ({source_dir}): {os.listdir(source_dir)}")
print(f"Files in processed directory ({processed_dir}): {os.listdir(processed_dir)}")

# List of file URLs and corresponding CSV filenames to extract
file_info = [
    ("https://repositoriodeis.minsal.cl/DatosAbiertos/VITALES/DEFUNCIONES_FUENTE_DEIS_2022_2024_25062024.zip", "DEFUNCIONES_FUENTE_DEIS_2022_2024_25062024.csv"),
    ("https://repositoriodeis.minsal.cl/DatosAbiertos/VITALES/DEFUNCIONES_FUENTE_DEIS_1990_2021_CIFRAS_OFICIALES.zip", "DEFUNCIONES_FUENTE_DEIS_1990_2021_CIFRAS_OFICIALES.csv")
]

# Debug: Check file existence without processing
for url, extract_filename in file_info:
    zip_filename = url.split('/')[-1]
    zip_path = os.path.join(source_dir, zip_filename)
    if not os.path.exists(zip_path):
        print(f"{zip_path} does not exist and would be downloaded.")
    else:
        print(f"{zip_path} already exists and would not be downloaded.")

# Placeholder for actual processing code (commented out for debugging)
# for url, extract_filename in file_info:
#     header_option = None if '2022_2024' in extract_filename else 'infer'
#     names_option = None if header_option == 'infer' else DEFAULT_HEADERS
#     process_zip_file(url, extract_filename, source_dir, processed_dir, header=header_option, names=names_option)

# Placeholder for merging and saving files (commented out for debugging)
# df1 = pd.read_parquet(os.path.join(processed_dir, "DEFUNCIONES_FUENTE_DEIS_2022_2024_25062024.parquet"))
# df2 = pd.read_parquet(os.path.join(processed_dir, "DEFUNCIONES_FUENTE_DEIS_1990_2021_CIFRAS_OFICIALES.parquet"))
# df_combined = pd.concat([df1, df2], ignore_index=True)
# df_filtered = df_combined[df_combined['AÑO'] >= 2003]
# combined_parquet
