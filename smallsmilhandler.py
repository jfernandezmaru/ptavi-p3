#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# practica 3 Ptavi Javier Fernandez Marugan

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler)

    """
    Clase para manejar chistes malos
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.width = ""
        self.height = ""
        self.background-color = ""
        self.id = ""
        self.top = ""
        self.left = 0
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = "0s"
        
        self.fill = ""


    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':

        elif name == 'region':
            
        elif name == 'img':
       						
        elif name == 'audio':
      
        elif name == 'textstream':

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':

        elif name == 'region':
            
        elif name == 'img':
       						
        elif name == 'audio':
      
        elif name == 'textstream':
        
#    def get_tags 
    
    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
  

if __name__ == "__main__":
    """
    Programa principal
    """
	




















