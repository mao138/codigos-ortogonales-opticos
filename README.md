# Códigos ortogonales opticos


## Código Ortogonal óptico. 

Este algoritmo determina si un conjunto dado es un código ortogonal óptico
en una dimensión con parámetros (n,w,a,c), por medio de la verificación de las propiedades de correlación.
Para su implementación en SAGE el algoritmo recibe una lista, la longitud n y los valores de la autocorrelación a 
y correlación cruzada c. Si la lista es un código ortogonal óptico retorna 1 y 0 en caso contrario.

## Cota de Johnson.

Este algoritmo calcula la Cota de Johnson para un código ortogonal óptico. 
El algoritmo recibe la longitud del código n, su peso w y la constante de correlación l.

## Construcción de Moreno y otros.

Este algoritmo construye las palabras del código ortogonal óptico 
construido por Moreno y otros en el artículo titulado A Generalized Bose-Chowla Family of Optical Orthogonal 
Codes and Distinct Difference Sets. Recibe los valores de un número primo  q, un entero positivo m y construye 
las palabras del código ortogonal óptico óptimo de parámetros (q^m-1,q,1).

## Construcción de Wilson.

Este algoritmo construye las palabras del código ortogonal óptico que aparece
en el artículo titulado Cyclotomy and difference families in elementary abelian groups. Recibe el valor del número
primo  p, el entero positivos c y construye un código ortogonal óptico de longitud p, peso (p-1)/c y constante de 
correlación igual a 1.

## Tabla de diferencias.

Este algoritmo construye la tabla de diferencias de dos palabras de un 
código ortogonal óptico. Recibe  dos palabras $X,Y$ del código (no necesariamente distintas), el módulo $n$
y construye la tabla.

## Contrucción de Bose.

Este algoritmo construye un conjunto de Sidon tipo Bose. El algoritmo recibe
la potencia prima q y calcula un conjunto de Sidon módulo q^2-1 con q elementos.

## Construcción de Ruzsa.

Este algoritmo construye un conjunto de Sidon tipo Ruzsa. El algoritmo 
recibe el número primo p, una raíz primitiva r módulo p y calcula un conjunto de Sidon módulo p(p-1) con 
p-1 elementos.

## Construcción A.

Los siguientes algoritmos permiten construir el código ortogonal A asintóticamente
óptimo que se encuentra en el artículo titulado Asymptotically optimal optical orthogonal codes with new
parameters.
