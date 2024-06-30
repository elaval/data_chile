import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def test_fetch_file(url, dest_path):
    # Set up session with retries and timeout
    session = requests.Session()
    retries = Retry(
        total=10,  # Increase the total number of retries
        backoff_factor=2,  # Increase the backoff factor
        status_forcelist=[500, 502, 503, 504]  # Retry on server errors
    )
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        response = session.get(url, timeout=180)  # Set a longer timeout
        response.raise_for_status()
        with open(dest_path, 'wb') as file:
            file.write(response.content)
        print(f"Successfully downloaded {url} to {dest_path}")
    except requests.exceptions.Timeout:
        print(f"Timeout error: Unable to download {url} within the timeout period.")
    except requests.exceptions.TooManyRedirects:
        print(f"Too many redirects: Unable to download {url}.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

# Test URL
url = "https://repositoriodeis.minsal.cl/DatosAbiertos/VITALES/DEFUNCIONES_FUENTE_DEIS_2022_2024_25062024.zip"
dest_path = "DEFUNCIONES_FUENTE_DEIS_2022_2024_25062024.zip"

test_fetch_file(url, dest_path)
