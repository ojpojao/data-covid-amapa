# Playing with requests module
Download microdados.csv file about covid-19 from http://painel.corona.ap.gov.br/dados/microdados.csv in the state of Amapá, Brazil.


This code downloads the file "microdados.csv" which contains information about COVID-19 in the state of Amapá, Brazil. 
The Archive is hosted at: http://painel.corona.ap.gov.br/dados/microdados.csv. I am not an experienced programmer, so please 
criticize as much as you can and with all your soul. At the moment this code only provides the download without any analysis of the data.
To use, first install requirements.txt:

```shell
    $ pip3 install -r requerements.txt
    $ python3 webrequest.py
```

After, can import into Pandas as a DataFrame as follow:
```python
import pandas as pd

encoding = "UTF-8"
delimiter = "'"
file = "microdados.csv"
sep = ","
names = ["Data", "Municipio", "Municipio_COD", "SEXO", "BAIRRO", "IDADE", "FAIXA_ETARIA", "COMORBIDADES"]

df = pd.read_csv(filepath_or_buffer=file, encoding=encoding, names=names)
df.drop(index=0, inplace=True)
```
**Pay ATTENTION: this repository there is no analysis about the dataframe.**
