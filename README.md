![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png) 

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

DESCRIPCION DEL PROYECTO </br>
El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente realizar un ETL, y luego disponibilizar los datos limpios para su consulta a través de una API construida en un entorno virtual.

Los datos serán provistos en archivos de diferentes extensiones, como *csv* o *json*. Se realizara un EDA para cada dataset y se correjiran los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, relacionaremos los datasets para así poder acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

DESCRIPCION DE LOS DATASETS

* amazon_prime_titles.csv: Contiene 12 dimensiones y 9668 registros. Tipo : csv
    * show_id: Id 
    * type: Tipo de titulo
    * title: Titulo
    * director : Director del titulo
    * cast:  Elenco del titulo
    * country: Pais 
    * date_added: Fecha en la que fue agregado el titulo
    * release_year: Fecha de lanzamiento del titulo
    * rating: Clasificación del titulo
    * duration: Duracion del titulo
    * listed_in: Clasificación dentro del listado de generos 
    * descripcion: Descripción del titulo

* disney_plus_titles.csv: Contiene 12 dimensiones y 1450 registros. Tipo : csv
    * show_id: Id 
    * type: Tipo de titulo
    * title: Titulo
    * director : Director del titulo
    * cast:  Elenco del titulo
    * country: Pais 
    * date_added: Fecha en la que fue agregado el titulo
    * release_year: Fecha de lanzamiento del titulo
    * rating: Clasificación del titulo
    * duration: Duracion del titulo
    * listed_in: Clasificación dentro del listado de generos 
    * descripcion: Descripción del titulo

* hulu_titles.csv: Contiene 12 dimensiones y 3073 registros. Tipo : csv
    * show_id: Id 
    * type: Tipo de titulo
    * title: Titulo
    * director : Director del titulo
    * cast:  Elenco del titulo
    * country: Pais 
    * date_added: Fecha en la que fue agregado el titulo
    * release_year: Fecha de lanzamiento del titulo
    * rating: Clasificación del titulo
    * duration: Duracion del titulo
    * listed_in: Clasificación dentro del listado de generos 
    * descripcion: Descripción del titulo

* netflix_titles.json: Contiene 12 dimensiones y 8807 registros. Tipo : json
    * show_id: Id 
    * type: Tipo de titulo
    * title: Titulo
    * director : Director del titulo
    * cast:  Elenco del titulo
    * country: Pais 
    * date_added: Fecha en la que fue agregado el titulo
    * release_year: Fecha de lanzamiento del titulo
    * rating: Clasificación del titulo
    * duration: Duracion del titulo
    * listed_in: Clasificación dentro del listado de generos 
    * descripcion: Descripción del titulo

FASES DEL PROYECTO

1. Ingesta y normalización de datos

2. Concatenar el conjunto de datos y crear la tabla necesaria para realizar consultas.

3. Exportar los datos a Mysql

4. Crear la API en un entorno Docker

5. Realizar consultas solicitadas

6. Realizar un video demostrativo

DESCRIPCION DEL TRABAJO REALIZADO

Se inicio cargando los datasets en un datframe de pandas se realizo el EDA correspondiente a cada uno para visulizar los valores duplicados, faltantes nulos, etc; se procedio a realizar un ETL con el cual se realizaron las transformaciones correspondientes, se importo una base de datos con los datasets concatenados por ultimo creamos un ambiente virtual, dockerizamos fastapi y creamos las consultas en la api dando solucion a los requerimientos minimos solicitados.

API:
http://127.0.0.1:8000/docs#/
![image](https://user-images.githubusercontent.com/105379715/218762906-c2e9e9f3-4a4b-4c93-86c8-d2a23b10b321.png)
