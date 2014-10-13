#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# practica 3 Ptavi Javier Fernandez Marugan

import sys
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
#class KaraokeLocal(SmallSMILHandler):


if __name__ == "__main__":

    lista= []
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler(lista)
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1],"r"))
    lines= cHandler.get_tags()

    for line in lines:
        for x in line.keys():
            if line[x]=="name":
                print line["name"]
                
     


