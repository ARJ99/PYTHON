from email.errors import MalformedHeaderDefect


class Moto(): #--Parent Class
    
    def __init__(self,cilindraje,modelo): #---Constructor para objetos
        
        self.marca1 = "Honda"
        self.marca2 = "Yamaha"
        self.cilindraje = cilindraje
        self.modelo =modelo
        self.estado="Apagado"
        
    def Arrancar(self):               #--Metodo 1
        self.estado="Encendido"
        
        if self.estado == "Encendido":
            print("La moto  "+ self.marca1, "tiene un cilindraje de : ",self.cilindraje)
            print(self.estado)
            

                
            
motocicleta = Moto(250,2019)   #--Instanciar un objeto

motocicleta.Arrancar()          