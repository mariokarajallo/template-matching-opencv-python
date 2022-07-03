#ejemplo de reconocimiento de patrones
# buscar patrones e identificar el area donde se encuentra el patron
# se puede contar la cantidad de elementos reconocidos y guardar esa informacion
# en una base de datos y en base de esa informacion realizar una accion determinada 
# podemos trabajar con imagenes inportadas o camaras 

import cv2
import numpy as np

#importar imagenes en escala de grises facilita el procesamiento de comparacion
#imread_grayscale lee un archivo o una imagen y convierte a una matriz
#todas las imagenes se almacenan como matrices
tarjeta = cv2.imread('tarjeta.jpg',cv2.IMREAD_GRAYSCALE)
plantilla = cv2.imread('circuito.jpg',cv2.IMREAD_GRAYSCALE)

#para dibucar un regtangulo del area que se reconocio lo que queremos
#debemos saber el largo y anchod e nuestra plantilla
# shape() obtiene esos datos
alto, ancho = np.shape(plantilla)

print (alto, ancho)

#cv2.matchTemplate() permite aplicar funciones matematicas a matrices
# e identificar si existe ciertas semejanzas, la funcion correlacion, significa que reconocio un patron
# si tiende de -1 a 0 no existe semejante si tiende a 1 si es semejante
# devuelve una matriz para poder identificar en que posicion hay una coincidenta
resultado= cv2.matchTemplate(tarjeta,plantilla,cv2.TM_CCOEFF_NORMED)

#la funcion minMaxLoc busca dentro de una matriz de resultado los valors
#el valor min y max representa el valor minimo del resultado de la funcion de correlacion
# por_min y pos_max representan la posiciones de min y max
min, max, pos_min, pos_max = cv2.minMaxLoc(resultado)

#para dibujar un rectagunlo necesitamos determinar las posiciones esquina superior izquierda y la esquina inferior derecha
#pos_max es un valor par que indica las coordenas X, Y
# de la esquina superior izquierda donde esta ubicado el elemento reconocido
#pos_min indica las coordendas de esquina inferior derecha

pixel_superior_izq= pos_max
#sabemos que pos_max es la posicion de la esquina superior izquierda
# el primer valor (pos_max[0]) del par de valores de pos_max va a representar
# el ancho de donde se ubica el pixel (el eje x) y la posicion del eje vertial
# el valor (pos_max[1])
pixel_inferior_der= (pos_max[0]+ancho, pos_max[1]+alto)


#importar imagen a compar pero esta vez a colar
#IMREAD_COLOR es la funcion por defecto al importar una imagen
tarjeta=cv2.imread('tarjeta.jpg',cv2.IMREAD_COLOR)
color_rojo=(0,0,2255)
#dibujar el rectangulo usando una funcion
cv2.rectangle(tarjeta,pixel_superior_izq,pixel_inferior_der,color_rojo,4)

cv2.imshow('resultado',tarjeta)
cv2.waitKey(0)
cv2.destroyAllWindows()









# #mostrar en una ventana la imagen
# cv2.imshow('tarjeta',tarjeta)
# cv2.imshow('plantilla',plantilla)

# #esperar que se precione una tecla cualquiera
# cv2.waitKey(0)
# #borrar o destruir todas las ventanas abiertas
# cv2.destroyAllWindows()
