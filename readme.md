# Algoritmo del Banquero

Este proyecto implementa el Algoritmo del Banquero de Dijkstra en Python3. El Algoritmo del Banquero es utilizado para gestionar la asignación de recursos en sistemas operativos, asegurando que se evite la condición de deadlock (bloqueo).

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `bankerImplentation.py`: Implementa la lógica del Algoritmo del Banquero.
- `interface.py`: Proporciona una interfaz de línea de comandos para interactuar con el Algoritmo del Banquero.
- `correrTests.sh`: Script de Bash para ejecutar múltiples archivos de configuración y guardar los resultados.
- `tests/`: Directorio que contiene los archivos de configuración de prueba.
- `outputs/`: Directorio donde se almacenan los resultados de las pruebas.

## Archivos de Configuración

Los archivos de configuración (`config1.txt`, `config2.txt`, etc.) contienen la configuración inicial del sistema en el siguiente formato:

1. Primera línea: Recursos disponibles.
2. Siguientes n líneas: Demanda máxima de cada proceso.
3. Últimas n líneas: Asignación actual de recursos para cada proceso.

### Ejemplo de Archivo de Configuración (config1.txt)

```
3 3 2
7 5 3
3 2 2
9 0 2
2 2 2
4 3 3
0 1 0
2 0 0
3 0 2
2 1 1
0 0 2
```

## Uso

### Ejecutar la Interfaz de Línea de Comandos

Para ejecutar la interfaz de línea de comandos y probar un archivo de configuración específico:

`python3 interface.py tests/config1.txt`


### Ejecutar Pruebas automáticas

- Dar permisos de ejecución a correrTests.sh: `chmod +x correrTests.sh`
- Correr en la terminal: `./correrTests.sh`

## Ejemplo de salida

### Recursos Disponibles:

|   | R1 | R2 | R3 |
|---|----|----|----|
|   |  3 |  3 |  2 |

### Demanda Máxima:

| P | R1 | R2 | R3 |
|---|----|----|----|
| 0 |  7 |  5 |  3 |
| 1 |  3 |  2 |  2 |
| 2 |  9 |  0 |  2 |
| 3 |  2 |  2 |  2 |
| 4 |  4 |  3 |  3 |

### Asignación:

| P | R1 | R2 | R3 |
|---|----|----|----|
| 0 |  0 |  1 |  0 |
| 1 |  2 |  0 |  0 |
| 2 |  3 |  0 |  2 |
| 3 |  2 |  1 |  1 |
| 4 |  0 |  0 |  2 |

### Estado Inicial Seguro:

([True, True, True, True, True], [1, 3, 4, 0, 2])

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, revisa el archivo LICENSE.