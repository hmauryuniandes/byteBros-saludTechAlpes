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
        type: Integración

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

## Microservicio de notificaciones
- Responsable: Luz Ochoa

Este microservicio está diseñado para gestionar y enviar notificaciones basadas en eventos dentro de un sistema distribuido. Utiliza Apache Pulsar como sistema de mensajería para recibir eventos y generar notificaciones correspondientes.

- Descripción
El microservicio de Notificaciones escucha eventos desde un sistema de mensajería basado en Apache Pulsar y procesa estos eventos para generar notificaciones a los usuarios o realizar otras acciones específicas. Utiliza Flask como servidor web para exponer algunos endpoints, y procesa los eventos utilizando un consumidor en segundo plano.

Este microservicio sigue un enfoque Event-driven, lo que significa que reacciona a los eventos generados en otros microservicios o sistemas, y no depende de consultas directas a bases de datos. En lugar de almacenar el estado de las notificaciones, se procesan eventos para cada acción, siguiendo el patrón de Event Sourcing.

- Actividades del Microservicio

### Recepción de eventos: 
El microservicio se suscribe a un tópico de eventos de Apache Pulsar (por ejemplo, suscripciones-topic).
Escucha los mensajes que se publican en el tópico y procesa los eventos de suscripciones que llegan.

### Generación de notificaciones:
Cuando un evento de suscripción es recibido, el microservicio genera una notificación asociada a dicho evento.
La notificación puede ser enviada a un sistema externo o almacenada internamente según los requisitos del sistema.

### Almacenamiento de eventos:
Los eventos de suscripción recibidos se almacenan en un Event Store.
Este enfoque permite reconstruir el estado o realizar auditorías sin necesidad de una base de datos centralizada.

### Publicación de mensajes:
El microservicio puede generar eventos de salida (notificaciones procesadas) y publicarlos en un sistema de mensajería como Pulsar para otros servicios.

### Consumo de mensajes en segundo plano:
Los mensajes son procesados en un hilo separado para evitar que el servidor web de Flask se bloquee y para poder manejar múltiples eventos de manera concurrente.

### Exposición de API REST:
El microservicio expone endpoints HTTP a través de Flask para verificar el estado del servicio y manejar ciertos eventos de manera manual, si es necesario.

-  Eventos de microservicio

### Evento de Notificación Creada: 
Se emite cuando una notificación es generada en respuesta a un evento de suscripción.

### Evento de Notificación Enviada: 
Se emite cuando la notificación ha sido enviada con éxito al usuario.

### Evento de Error en el Procesamiento de Notificación: 
Se emite cuando ocurre un error al procesar o enviar una notificación.

### Evento de Confirmación de Notificación: 
Se emite como una confirmación de que la notificación fue procesada correctamente.

- Endpoints 

### GET /: Verifica si el microservicio está en ejecución.
   # Respuestas:
    {
    "message": "Microservicio de notificaciones en ejecución"
    }

### POST /notificaciones: Crea una notificación a partir de los eventos recibidos.
# Cuerpo de la solicitud (JSON):
    {
        "id_suscripcion": "12345",
        "mensaje": "Tu suscripción se ha creado exitosamente."
    }

### POST /suscripcion-comando: Endpoint para recibir un comando de suscripción y crear una notificación basada en ello.
# Cuerpo de la solicitud (JSON):
    {
    "id_suscripcion": "67890",
    "cliente": "Juan Pérez",
    "plan": "Premium"
    }



### Correr docker-compose usando profiles
```bash
docker-compose --profile pulsar --profile suscripciones --profile procesamiento --profile bff_web up --profile notificaciones --profile serviciodatos up -d --build
```


