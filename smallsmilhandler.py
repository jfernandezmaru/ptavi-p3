#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# practica 3 Ptavi Javier Fernandez Marugan
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.etiquetas = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "bottom", "left", "right"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region", "fill"]}
        self.lista = []

    def startElement(self, name, attrs):
        dic = {}
        if name in self.etiquetas:
            dic["name"] = name
            for atributo in self.etiquetas[name]:
                dic[atributo] = attrs.get(atributo, "")
            self.lista.append(dic)

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
