import requests

'''
Este programa es un ejemplo basico de como hacer "Web Scraping" con python
El Url que uso es do una de las pajinas del citio web que tiene la informacion que queremos
'''

def export_to_file(response, filename):
    f = open(filename, 'w')
    f.write(response.text)
    f.close()
    print(f'Response has been succesfully exported to file: {filename}')

def scrape(url):
    # GET request al url
    r = requests.get(url)
    export_to_file(r, 'scraped_documents/test.html')

def main():
    # url for government websit
    # url del citio web gubernamental 
    url = 'http://banter.archivogeneral.gov.co/banter/vocab/index.php?tema=289&/licencias-ambientales-series'
    
    # Cuando hacemos el request a este url, nos devuelve puro html
    # Cojemos el html y lo guardamos en un archivo que en este momento se llama 'test.html'
    # Para sacarle la informacion que queremos nos va tocar sacarla del html puro
    # Hay librerias en python para hacer esto (BeautifulSoup), pero antes de desaroyarlo, es mejor saber que informacion queremos especificamente
    scrape(url)

if __name__ == '__main__':
    main()