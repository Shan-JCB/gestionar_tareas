class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def ver_tareas(self):
        return self.tareas

    def marcar_completada(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.completada = True
                return
        raise ValueError("Tarea no encontrada")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                return
        raise ValueError("Tarea no encontrada")