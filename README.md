![Python 3.7.0](https://img.shields.io/badge/python-3.7.0-blue.svg)

*No dudes en pedirme ayuda o explicaciones más detalladas.* *[@daavm98](https://twitter.com/daavm98?lang=en)*

# Trump Markov Bot

Bot de generación de lenguaje natural simple a través de una Cadena de Markov. Utiliza como base los últimos 15000 tweets de Donald Trump ![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?style=social&label=Follow%20%40MarkovDTrump)


## How to setup

### Dependencias

1. Primero, asegurémonos de tener `pip` instalado y actualizado:

    ```
    pip install --upgrade pip
    ```
    
1. Ahora simplemente instalaremos los requisitos:

    ```
    pip install -r requirements.txt
    ```
    
    
### Estructura

- TrumpMarkovBot

  - :file_folder: markovbot 
  - generated_sentences.txt
  - generator.py
  - keys.py
  - poster.py
  - README.md
  - requirements.txt
  - tweets.py
  - (*)

(*) Se han obviado los archivos txt que utiliza generator.py para generar los tweets. Más adelante veremos cómo generar estos *.txt.


### Uso

1. Al ejecutar el archivo *get_all_tweets.py", y pasado un tiempo (dependiendo del nivel de tweets que generemos tardará más o menos) se nos habrá generado un archivo llamado all_ids.json.
2. Una vez hecho el paso 1, deberemos ejecutar el archivo *tweets.py", que nos devolverá un archivo *.txt con los tweets que hayamos extraído, el cual ya podrá leer el generador de nuevos tweets.
3. Ejecutando el archivo *generator.py*, el bot leerá los tweets que hayamos extraído anteriormente y generará una lista con el número de tweets que elijamos dentro de este mismo archivo.
4. Ejecutando el archivo *poster.py*, el bot publicará los tweets del archivo *generated_sentences.txt*, esperando un número de horas igual al valor de la variable `hours` entre publicación y publicación.

Los tweets son escritos en un archivo y no publicados directamente para darnos la posibilidad de filtrarlos y de decidir el orden de publicación de los mismos.

##


