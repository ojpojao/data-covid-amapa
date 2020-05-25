import requests
from requests.exceptions import HTTPError
import time
from os import path
from os import rename
from os import remove
import hashlib

"""
This code downloads the file "microdados.csv" which contains information about COVID-19 in the state of Amapá, Brazil. 
The Archive is hosted at: http://painel.corona.ap.gov.br/dados/microdados.csv. I am not an experienced programmer, so please 
criticize as much as you can and with all your soul. At the moment this code only provides the download without any analysis of the data.
To use, first install requirements.txt:
    $ pip3 install -r requerements.txt
    $ python3 webrequest.py
"""

__author__ = "ojpojao"
__version__ = "0.1"
__email__ = "ojpojao@gmail.com"

# download_csv() function is a sample from @realpython: https://realpython.com/python-requests/


def download_csv(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

    except HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
    except Exception as err:
        print(f"Erro: {err}")
    else:
        print(f"Getting newfile!!!!!")
    return response


def file_exists(file):
    return path.exists(file)


def file_path(file):
    return path.abspath(file)


def salve_file(content, name="microdados.csv"):
    with open(name, 'wb') as f:
        f.write(content)
    return name


def md5sum(file):
    with open(file, 'rb') as f:
        md5sum = hashlib.md5(f.read()).hexdigest()
    return md5sum


def main():

    url = "http://painel.corona.ap.gov.br/dados/microdados.csv"
    current_file = "microdados.csv"
    headers = {"Content-Type": "text/csv"}

    raw_requests = download_csv(url, headers)

    if not file_exists(file_path(current_file)):
        print(f"Creating CSV File - {current_file}.")
        salve_file(raw_requests.content)
        print("Complete.")

    else:
        newfile = salve_file(raw_requests.content, "newfile.csv")
        files = [current_file, newfile]
        hashs = []

        # Teste MD5SUM
        for i in files:
            hashs.append(md5sum(i))

        if not hashs[0] == hashs[1]:
            print("Hash was changed!!!\nUpdate File.")
            print(f"{hashs[0]} *{current_file}, current_file Will Be Deleted.")
            print(f"{hashs[1]} *{newfile}, newfile")
            remove(current_file)
            print("Current File REMOVED!")
            rename(newfile, current_file)
            print(f"{newfile} renamed to {current_file}")

        time.sleep(2.5)

        if file_exists(newfile):
            remove(newfile)
        print("Success!!!")


if __name__ == "__main__":
    main()

