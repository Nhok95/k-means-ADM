# Unsupervides k-means


## Instrucciones instalacion

Ejecutamos el comando de virtual environment
```sh
py -m venv .venv
```

tmabien podemos instalar virtualenv para mas comodidad
```sh
pip3.10 install virtualenv
```

Y luego ejecutar
```sh
virtualenv .venv
```

Activamos el virtual environment
```sh
source .venv/Scripts/activate
```

Podemos actualizar pip para el entorno
```sh
py -m pip install --upgrade pip
```

Podemos ver los paquetes instalados en cualquier momento
```sh
pip list
```


## PIP
Podemos instalar los packages usando pip

### SKlearn
* pip install -U scikit-learn

### Python
* pip install pandas
* pip install -U matplotlib
* pip install ipykernel

## Requirements file
Podemos generar el archivo requirements con el siguiente comando
```sh
pip freeze > requirements.txt
```

Una vez tenemos el archivo requirement instalar los packages es sencillo ya que solo lanzamos el
siguiente comando
```sh
pip install -r requirements.txt
```

