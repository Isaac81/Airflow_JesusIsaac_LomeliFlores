# Universidad de Guadalajara - Centro Universitario de Ciencias Exactas e Ingenierias
## Departamento de ciencias computacionales
Computacion Tolerante a fallas - Seccion D06

Profesor: *Lopez Franco Michel Emanuel*

Alumno: *Lomeli Flores Jesus Isaac*

## Airflow

### Introducción

<p align="justify">
  Al igual que en la práctica anterior en la cual se utilizó Prefect como manejador de flujo, en la actual se hace uso de Airflow, que si bien ambas herramientas 
  tienen el mismo propósito, airflow trabaja de forma distinta comenzando con las configuraciones necesarias que este requiere para funcionar, sin mencionar la enorme
  mejora en la interfaz gráfica y los detalles que proporciona acerca del flujo de trabajo de las aplicaciones.
</p>


</div>

### Desarrollo

<p align="justify">
  Para el desarrollo de esta práctica se utilizó el lenguaje de programación python en su versión 3.10.6 puesto que airflow no se encontraba disponible en las 
  versiones superiores al momento de realizar la práctica. Al igual que en la práctica de workflow el código trata de simular la creación y ejecución de procesos, para
  lo cual es necesario crear una función que será el flujo de trabajo dentro de la cual se anidaran las tareas a realizar. Esta estructura resulta un cambio notorio
  con respecto a prefect donde se declaraba un flujo y por separado las tareas a realizar.
</p>


<p align="justify">
  En la parte inferior se muestra el código utilizado como ejemplo para esta práctica.
</p>


```py
from airflow.decorators import dag, task
from datetime import datetime
from time import sleep

import random


@dag(
    schedule = None,
    dag_id = "process_1",
    start_date = datetime(2023,3,12),
    tags = ["process"]

)


def main_flow():


    @task()    
    def create_process ():
        process = {
            "num1": random.randint(0, 1),
            "num2": random.randint(0, 1),
            "tme": random.randint(1, 5)
        }

        return process

    
    @task()
    def execute(process):
        result = process['num1'] / process['num2']
        sleep(process['tme'])

        return result


    p = create_process()
    result = execute(p)
    print(f"Process completed in {p['tme']} seconds. Result: {result}")


main_flow()
```


<p align="justify">
 Al igual que en perfect, se debe llamar a la funcion principal que representa el flujo de trabajo, en este caso main_flow().
</p>


<p align="justify">
 Para comenzar la ejecucion de airflow es necesario ingresar el comando aiflow standalone que mostrara la siguiente pagina en el puerto 8080 del localhost.
</p>

![Ejecución del airflow](/Imagenes/Screenshot_28.png)

<p align="justify">
 En la captura de pantalla superior se muestan algunos ejemplos de airflow, por lo que se hace uso de un filtro para mostrar solo el desarrollado para esta práctica
 el cual tiene la etiqueta process.
</p>

![Ejecución del airflow](/Imagenes/Screenshot_29.png)

<p align="justify">
 Una vez localizado el DAG se ejecuta en varias ocasiones hasta que el el flujo tenga un error en la ejecución, pues, al igual que en la práctica del workflow puede
 darse el caso donde se realice una división entre cero. Una vez que este evento ocurra airflow nos notificara que hubo un error en el flujo de trabajo como en la
 siguiente imagen.
</p>

![Ejecución del airflow](/Imagenes/Screenshot_30.png)

<p align="justify">
Si por el contrario, el programa se ejecuto correctamente finalizara el proceso mostrando las salidas de las diferentes tareas del flujo.
</p>

![Comprobar ejecución del servicio](/Imagenes/Screenshot_25.png)

### Conclusión

<p align="justify">
Se logró comprender la utilidad que tienen las herramientas cómo prefect para el desarrollo de aplicaciones mas seguras y de facil depuración, pues al mostrar 
exactamente en que parte de flujo del sistema ocurrio el error se ahorra tiempo al no tener que buscar la ubicación del problema y centrarse en la posible solución.
</p>


### Bibliografia
* queue — A synchronized queue class. (s. f.). Python documentation. Recuperado el 5 de Marzo de 2023, de https://docs.python.org/3/library/queue.html *
