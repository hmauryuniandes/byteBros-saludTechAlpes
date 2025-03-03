# Sistema saludtechalpes

## Miembros:

- Monica Muñoz
- Luz Ochoa
- Andres Lombo
- Humberto Maury

### Diagrama de la solución

![screenshot](saludtechalpes.drawio.png)

### Escenarios de calidad 

[Descargar Archivo](escenarios_calidad.pdf)

## Decisiones de diseño
-
-
-

## microservicio suscripciones

- Responsable: Humberto Maury
- Documentación: [README](./microservicio-suscripciones/README.md)
- Actividades: 

    [x] Definir la entidad raiz, entidades y objetos valor.

    [x] Implementar repositorios de acceso a datos usando postgresDB.

    [x] Implementar mappers para dtos de infraestructura.

    [x] Definir los camandos y eventos en la capa de aplicacion. 

    [x] Definir los queries en la capa de aplicacion.

    [x] Suscribirse a los topicos de eventos y comandos. 

    [x] Publicar eventos de integracion. 

    [x] Implementar mappers para dtos de aplicacion.

    [x] Configurar Dockerfile y actualizar el docker-compose.

- Comandos: 

    ### ComandoCrearSuscripcion:
        
        schema-type: Cloud event + AVRO

        version: v1

        Payload:
    ```py
            class ComandoCrearSuscripcionPayload(ComandoIntegracion):
                cliente_codigo = String()
                cliente_nombres = String()
                cliente_apellidos = String()
                cliente_usuario = String()
                cliente_rut = String()
                cliente_cedula = String()
                cliente_email = String()
                plan_codigo = String()
                plan_nombre = String()
    ```    
    ### ComandoCambiarPlanSuscripcion:
        
        Schema-type: Cloud event + AVRO

        Version: v1

        Payload: TBD

    ### ComandoCancelarSuscripcion:
        
        Schema-type: Cloud event + AVRO

        Version: v1

        Payload: TBD

    ### ComandoPagarSuscripcion:
        
        Schema-type: Cloud event + AVRO

        Version: v1

        Payload: TBD
        
- Eventos: 

    ### EventoSuscripcionCreada
        type: Integracion - Fact

    ### EventoSuscripcionCancelada
        type: Integracion - Fact

    ### EventoSuscripcionPlanModificado
        type: Integracion - Fact

    ### EventoSuscripcionPagada
        type: Integracion - Fact

## microservicio procesamiento

[README](./microservicio-suscripciones/README.md)

## microservicio notificaciones

[README](./microservicio-notificaciones/README.md)

## microservicio servicios de datos

[README](./microservicio-notificaciones/README.md)


## BFF WEB

- Responsable: Humberto Maury
- Documentación: [README](./bff_web/README.md)
- Actividades: 

    [x] Crear endpoint comando crear suscripcion.

    [x] publicar comando en el topico.

    [ ] Implementar queries.
    
    [x] Configurar Dockerfile y actualizar el docker-compose.

- Endpoints: 

    **Endpoint**: `/suscripciones/suscripcion-comando`

    **Método**: `POST`

    **Headers**: `Content-Type='aplication/json'`

    ```json
    {
    "cliente": {
            "codigo": "0001",
            "nombre": {
                "nombres": "Pablo",
                "apellidos": "Perez Prieto"
            },
            "usuario": "pperez",
            "rut": {
                "numero": 123457890
            },
            "cedula": {
                "numero": 123457890
            },
            "email": "pperez@domain.com"
    },
    "plan": {
            "codigo": "pro",
            "nombre": "PRO"
    },
    "facturas": []
    }
    ```


### Correr docker-compose usando profiles
```bash
docker-compose --profile pulsar --profile suscripciones --profile procesamiento --profile bff_web up --build
```


