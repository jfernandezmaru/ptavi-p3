#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# practica 3 Ptavi Javier Fernandez Marugan

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    """
    Clase para manejar chistes malos
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        
#        self.inroot-layout = 0
#        self.inregion = 0
#        self.inimg = 0
#        self.inaudio = 0
#        self.intextstream = 0
                        
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


    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':

            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.background_color = attrs.get('background-color',"")
            print self.width
            print self.height
            print self.background_color

        elif name == 'region':
       
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
            print self.id
            print self.top
            print self.bottom
            print self.left
            print self.right
            
        elif name == 'img':

#                                        hay varios src, dur, region se sobreescriben???  
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            self.end = attrs.get('end',"")
            print self.src
            print self.region
            print self.begin
            print self.dur
            print self.end
                               
        elif name == 'audio':

            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            print self.src
            print self.begin
            print self.dur
      
        elif name == 'textstream':

            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.fill = attrs.get('fill', "")
            print self.src
            print self.region
            print self.fill

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':

            self.width = ""
            self.height = ""
            self.background_color = ""

        elif name == 'region':
      
            self.id = ""
            self.top = ""
            self.bottom = ""
            self.left = ""
            self.right = ""
            
        elif name == 'img':

#                                        hay varios src, dur, region se sobreescriben???  
            self.src = ""
            self.region = ""
            self.begin = ""
            self.dur = ""
                               
        elif name == 'audio':

            self.src = ""
            self.begin = ""
            self.dur = ""
      
        elif name == 'textstream':

            self.src = ""
            self.region = ""
            
#    			def get_tags 
    
    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
  

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))

