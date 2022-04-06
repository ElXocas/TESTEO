class Casa():
    def __init__(self):
        self.ventana = "corrediza"
        self.puerta = "Madera"
        self.baño = "Un baño"
        self._cocina ="Una cocina"
    
    def get_ventana(self):
        return self.ventana

    def get_puerta(self):
        return self.puerta

    def get_baño(self):
        return self.baño

    def get_cocina(self):
        return self._cocina

    def set_cocina(self,cocina):
        self._cocina = cocina

micasa = Casa()
print("Tengo",micasa.get_cocina())
micasa.set_cocina("dos cocinas")
print("Ahora tengo", micasa.get_cocina())
