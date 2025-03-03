## Request de ejemplo

Los siguientes JSON pueden ser usados para probar el API:

### Crear suscripción

- **Endpoint**: `/suscripciones/suscripcion-comando`
- **Método**: `POST`
- **Headers**: `Content-Type='aplication/json'`

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
            "numero": 11111111
        },
        "cedula": {
            "numero": 22222222
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

### docker build 
```bash
docker build . -f bff_web.Dockerfile -t bff_web/flask
```
