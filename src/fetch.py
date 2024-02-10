import requests
import pandas as pd


def download_file(url, destination):
    """Download a file from a URL to a local destination."""
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    with open(destination, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded to {destination}")


def download_spreadsheet(url: str):
    df = pd.read_excel(url)
    df = pd.read_excel(url, sheet_name="Sheet1")
    df.to_csv("./datasets/products.csv")
    print("File downloaded")


if __name__ == "__main__":
    gsheetkey = "1lQ6szSpMN89Vxba7oTpuJPAf6NZJu0VtQdtYG0Sclos"
    url = f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
    download_spreadsheet(url)
