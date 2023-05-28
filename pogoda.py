import requests
from datetime import datetime

whole_datetime = datetime.now()

data_dzis = whole_datetime.strftime("%Y%m%d")

image_url = f'https://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate={data_dzis}06&row=406&col=250&lang=pl'

img_data = requests.get(image_url).content

with open('mgram_pict.png', 'wb') as f:
    f.write(img_data)