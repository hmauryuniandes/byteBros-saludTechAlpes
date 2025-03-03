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

- Responsable: Andrés Lombo
- Documentación: [README](./microservicio-suscripciones/README.md)
- Actividades: 

    [x] Definir la entidad raiz, entidades y objetos valor.

    [x] Implementar repositorios de acceso a datos usando postgresDB.

    [x] Definir los comandos en la capa de aplicacion. 

    [x] Definir los queries en la capa de aplicacion.

    [x] Definir los eventos en la capa de dominio.

    [x] Definir consumidores que se suscriben a los topicos de eventos y comandos. 

    [x] Definir despachadores para publicar eventos de dominio. 

    [x] Configurar Dockerfile y actualizar el docker-compose.

- Comandos: 

    ### ComandoCrearSuscripcion:
        
        schema-type: AVRO

        Payload:
    ```py
            class ImagenAnonimizada(Entidad):
                self.id_imagen = id_imagen
            self.modalidad = modalidad
            self.patologia = patologia
            self.region_anatomica = region_anatomica
            self.formato_imagen = formato_imagen
            self.fuente_de_datos = fuente_de_datos
            self.antecedentes = antecedentes
            self.id_paciente = id_paciente
            self.fecha_ingesta = fecha_ingesta
    ```   

- Queries:
    ### ObtenerImagenAnonimizada

- Eventos:
    ### EventoAnonimizacion
        type: Dominio

    ### EventoConsultaAnonimizacion
        type: Dominio

- Endpoints: 

    **Endpoint**: `/anonimizar`

    **Método**: `POST`

    **Headers**: `Content-Type='aplication/json'`

    ```json
    {
        "id_imagen": "46769a88-581f-4468-8a14-14f705887d01",
        "modalidad": "Rayos X",
        "patologia": "Neumonía",
        "region_anatomica": "Cráneo",
        "formato_imagen": "DICOM",
        "fuente_de_datos": "Hospital del norte",
        "antecedentes": "Diabético",
        "id_paciente" : "46769a88-101f-4468-8i34-15750381d01",
        "fecha_ingesta": "2024-02-01 09:10:00"
    }
    ```

    **Endpoint**: `/anonimizado/<int:id_datos>`

    **Método**: `GET`


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
docker-compose --profile pulsar --profile suscripciones --profile procesamiento --profile bff_web up --profile notificaciones --profile serviciodatos up -d --build
```


