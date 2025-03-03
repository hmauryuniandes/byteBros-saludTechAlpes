# byteBros-suscripciones: Microservicio Suscripciones

## Miembros:

- Monica Muñoz
- Luz Ochoa
- Andres Lombo
- Humberto Maury


## Instalar dependecias
```bash
pyenv install 3.10.7 -f && pyenv local 3.10.7
```

```bash
pip install -r requirements.txt
```

## Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/suscripciones./api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/suscripciones./api --debug run
```

### docker build 
```bash
docker build . -f suscripciones.Dockerfile -t suscripciones/flask
```

### Correr docker-compose usando profiles
```bash
docker-compose --profile pulsar --profile suscripciones up
```

### Escenario de calidad 

![screenshot](escenario_modificabilidad.png)

### Escenarios de calidad 

[Descargar Archivo](escenarios_calidad.pdf)