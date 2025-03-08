def enviar_notificacion(event):
    try:
        if event == "ProcesoFinalizado":
            mensaje = "La transacción ha sido finalizada exitosamente."
        else:
            mensaje = f"Evento recibido: {event}"

        print(f"Notificación: {mensaje}")
        return True
    except Exception as e:
        print(f"Error al enviar notificación: {e}")
        return False
