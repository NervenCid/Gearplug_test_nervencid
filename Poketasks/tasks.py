from celery import shared_task

@shared_task
def mi_tarea_test():
    # Agrega aquí la lógica de tu tarea
    print("Tarea completada")
    return "Tarea completada"