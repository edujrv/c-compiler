class TablaSimbolos:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
           cls._instance = super(TablaSimbolos, cls).__new__(cls)
        return cls._instance
    
    ts = [dict()]

    """cuando estamos en el contexto global, osea en el dict 0, no lo borramos xq ahi estan las variables globales"""
    
    def addContex(self):
        """agrega un nuevo diccionario vacio al final de la lista.
        esto es crear un nuevo contexto.
        El contexto se crea cada vez que entramos a un bloque de codigo, es decir cada vez que abrimos llaves {"""
        self.ts.append(dict())
    
    def removeContex(self):
        """elimina el ultimo diccionario de la lista, osea el contexto mas reciente
        salir de un contexto, es cerrar una llave }"""
        self.ts.pop()
        
    def addId(self, id):
        """agrega un ID al diccionario del contexto actual"""
        self.ts[-1][id.name] = id
    
    def findByKey(self,key):
        """busca un ID en todos los diccionarios de la lista"""
        #print(f'TS -> {self.ts}')
        #print(f'TS -> key:{key}')
        for context in self.ts:
            if key in context:
                return True
        return False
    
    def returnKey(self,key):
        """devuelve el ID, retorna False si no se encuentra"""
        for context in self.ts:
            if key in context:
                return context[key]
        return False


class Id:
    def __init__(self,name, type):
        self.name = name
        self.type = type
        self.initialized = False
        self.used = False
        self.varFunc = "variable"  #indica si es una VARIABLE o una FUNCION
        
    def toString(self):
        return f'(name->{self.name},type->{self.type},init->{self.initialized},used->{self.used},varFun->{self.varFunc})'
    

class Variable(Id):
    pass

class Function(Id):
    def __init__(self, name, type, parameters):
        super().__init__(name, type)
        self.parameters = parameters
        self.varFunc = "function"
        # el valor que retorna la funcion es: type
    
        