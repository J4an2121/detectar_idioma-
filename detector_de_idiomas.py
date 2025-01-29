from langdetect import detect #Aquí se importa la función detect del módulo langdetect, que permite identificar el idioma de un texto.

def detectar_idioma(texto): #Se define la función detectar_idioma, que recibe un texto como parámetro.
    idioma = detect(texto)
    print(f'idioma detectado es:{idioma}')


if __name__== "__main__": #comprueba si el script se está ejecutando directamente.
    texto = input('Ingresar texto para detectar el idioma:')
    detectar_idioma(texto)