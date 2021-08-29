# proyectoFigueroa
Proyecto de documentos gubernamentales 

# Instalacion 

## Python 3

Este programa esta escrito en Python 3.
Si no tienes Python 3 instalado, instalalo de [aqui](https://www.python.org/downloads/).

## Pipenv

Lo mas facil para instalar las librerias necesarias es usar `pipenv`. Encuentre instrucciones para las instalacion y uso [aqui](https://packaging.python.org/tutorials/managing-dependencies/#installing-pipenv).

Cuando este instalado. Entre a este directorio y cora 
```
$ pipenv install
```

Si no quiere usar `pipenv` puede solo usar 
```
$ python -m pip install requests
```

## Ejecucion del Programa

Si esta usando `pipenv`:
```
$ pipenv shell
$ python scrape.py
```

Para despues salirse del entorno virtual de `pipenv`:

```
$ deactivate
```

Para ejecutar el programa si no esta usando `pipenv`:
```
$ python scrape.py
```

Despues de que el programa ejecute, deberia entontrar un nuevo directorio llamado `/scraped_documents` con un nuevo archivo llamado `test.html`.

Si habre `test.html` va encontrar el html puro de [esta pagina](http://banter.archivogeneral.gov.co/banter/vocab/index.php?tema=289&/licencias-ambientales-series).






