# Reto FastApi
En este Readme se detalla la ejecución del test enviado tanto local como en Docker, se uso una base de datos sqlite con 10000 registros de patentes con el formato ***BBB123*** en el cual fue propuesto en el documento. La prueba cuenta ademas con una suite de testing con 9 casos aprobados. Espero sea de su agrado.

## Ejecutar localmente

Ejecutamos el entorno virtual:
```
    source venv/bin/activate
```

Primero instalamos las librerias:
```
	pip install -r requirements.txt
```
Luego ejecutamos localmente el servidor del fastapi:
```
	uvicorn main:app --reload
```

### Ejecutar testing
```
	pytest
```
## Dockerizing

Primero construimos la imagen:
```
	docker-compose build
```

Luego corremos el contenedor:
```
	docker-compose up
```
