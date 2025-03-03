# byteBros-suscripciones: Microservicio Suscripciones

## Miembros:

- Monica Muñoz
- Luz Ochoa
- Andres Lombo
- Humberto Maury

## Request de ejemplo

Los siguientes JSON pueden ser usados para probar el API:

### docker build 
```bash
docker build . -f procesamiento.Dockerfile -t procesamiento/flask
```

### Correr docker-compose usando profiles
```bash
docker-compose --profile pulsar --profile procesamiento up
```

### Procesar imagen

- **Endpoint**: `/anonimizar`
- **Método**: `POST`
- **Headers**: `Content-Type='aplication/json'`

```json
{
    "id_imagen": "46769a88-581f-4468-8a14-15f715887d01",
    "modalidad": "Rayos X",
    "patologia": "Neumonía",
    "region_anatomica": "Cráneo",
    "formato_imagen": "DICOM",
    "fuente_de_datos": "Hospital del norte",
    "antecedentes": "Diabético",
    "id_paciente" : "46769a88-181f-4468-8i34-15f750381d01",
    "fecha_ingesta": "2024-02-01 09:10:00"
}
```

