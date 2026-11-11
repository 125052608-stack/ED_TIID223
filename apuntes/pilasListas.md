# Pilas

## Estructura de datos lineal 

Oganiza elementos bajo el principio LIFO

Sirve para el historial de navegación

- Call stack: Control de ejecución de aplicaciones en lenguaje de programación


## Características:
- Solo se trabaja con último elemento de la pila 
- Tamaño dinámico

## Operaciones Básicas:
- Push: Agregar un elemento
- Pop: Eliminar el último elemento
- peek o top: Consultar el elemento superior, no elimina elementos
- is_empty: verificar si está vacía

## Declarar
nombre_pila = []

# Listas Enlazadas

- Se guardan en una Lista.
- Se guardan dos datos, uno para el contenido y otro para la referencia del siguiente nodo.

## Como funcionan
- Su usan cadenas de bloques llamadas nodos
- Comienzan en la cabeza del nodo y pueden ir avanzando para el siguiente nodo por medio de un puntero  

## Características
- Se forman por nodos con un enlace.
- Acceso secuencial.
- Requiere un espacio adicional en la memoria para almacenar el enlace. 
- head: primer nodo.
- El último nodo = final de la lista.
- Facilitan la inserción y eliminación de datos.

## Operaciones
- Recorrido: consiste en imprimir los elementos de una lista enlazada
- Inserción: Permite añadir un nodo nuevo a una lista enlazada
- Eliminar: Consiste en retirar un nodo de la lista enlazada y configurar el puntero del anterior
- Búsqueda: Permite encontrar un nodo que contiene un valor recorriendo la lista de formam secuencial