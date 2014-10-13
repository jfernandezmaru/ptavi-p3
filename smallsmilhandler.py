#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# practica 3 Ptavi Javier Fernandez Marugan

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """
    def __init__ (self,lista):
        """
        Constructor. Inicializamos las variables
        """
        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = "0s"
        self.end = "0s"
        self.fill = ""
        self.etiquetas = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "bottom", "left", "right" ],
            "img" : ["src", "region", "begin", "dur"],
            "audio" : ["src", "begin", "dur"],
            "textstream" : ["src", "region", "fill"] }
        
        self.lista = lista

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        dic = {}
        if name in self.etiquetas:
            dic["name"] = name
            for atributo in self.etiquetas[name]:
                dic[atributo] = attrs.get(atributo, "")
            self.lista.append(dic)

    def get_tags(self):
    
        return self.lista 

if __name__ == "__main__":
    """
    Programa principal
    """
    lista= []
    parser = make_parser()
    cHandler = SmallSMILHandler(lista)
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    #print cHandler.get_tags()

