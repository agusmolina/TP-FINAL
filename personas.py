


class Persona():
    def __init__(self,nombre):
        self.nombre=nombre

class Cliente(Persona):
    def __init__(self, nombre,apellido):
        super().__init__(nombre)
        self.apellido=apellido


class Encargado(Persona):
    def __init__(self, nombre,id,total=0):
        super().__init__(nombre)
     
        
