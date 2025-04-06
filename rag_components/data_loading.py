import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO  # Importa StringIO

def cargar_datos(url):
    """
    Carga los datos de departamentos y capitales desde una página web.

    Args:
        url (str): La URL de la página web.

    Returns:
        pandas.DataFrame: Un DataFrame con la información de departamentos y capitales,
                          o None si no se encuentra la tabla.
    """
    try:
        # Fetch the page content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscar todas las tablas en la página
        tables = soup.find_all('table')

        # Verificar si alguna tabla contiene información sobre departamentos y capitales
        tabla = None
        for table in tables:
            if "Departamento" in table.get_text() and "Capital" in table.get_text():
                tabla = table
                break

        # Si se encuentra la tabla, convertirla en un DataFrame
        if tabla:
            # Use StringIO to wrap the literal html string
            html_string = StringIO(str(tabla))
            df_departamentos = pd.read_html(html_string)[0]
            return df_departamentos
        else:
            print("No se encontró una tabla con información de departamentos y capitales.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")
        return None


def preparar_datos(df_departamentos):
    """
    Prepara los datos del DataFrame para generar embeddings.

    Args:
        df_departamentos (pandas.DataFrame): El DataFrame con la información de departamentos y capitales.

    Returns:
        list: Una lista de strings formateados con la información de cada departamento y capital.
    """
    try:
        # Eliminar la columna 0 y la primera fila (si existen)
        df_departamentos = df_departamentos.iloc[1:, 1:]

        # Establecer los nuevos nombres de las columnas desde la primera fila
        new_column_names = df_departamentos.iloc[0]
        df_departamentos.columns = new_column_names.values
        df_departamentos = df_departamentos.iloc[1:]

        # Crear la lista de documentos
        documentos = []
        for index, row in df_departamentos.iterrows():
            documento = f"Departamento: {row['Departamento']}, Capital: {row['Capital']}"
            documentos.append(documento)

        return documentos

    except Exception as e:
        print(f"Error al preparar los datos: {e}")
        return None