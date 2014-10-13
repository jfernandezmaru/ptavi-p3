#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# practica 3 Ptavi Javier Fernandez Marugan

import sys
from smallsmilhandler import SmallSMILHandler
import os

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):

        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fichero)
        self.lines = cHandler.get_tags()

    def __str__(self):

        string = ""
        for line in self.lines:

            for x in line.keys():

                if x == "name":
                    string = string + line[x] + '\t'

            for x in line.keys():

                if x != "name" and line[x] != '' and line[x] != '\t':
                    string = string + x + '=' + '"' + line[x] + '"' + '\t'

            string = string + "\n"
        return string

    def do_local(self):

        for line in self.lines:

            for x in line.keys():

                if x != "name" and line[x] != '' and line[x] != '\t':

                    if x == "src":

                        recurso = line[x]
                        os.system("wget -q " + recurso)

                        if (line[x])[0:7] == "http://":
                            helper = line[x].split('/')
                            line[x] = helper[-1]

if __name__ == "__main__":

    try:
        fich = (open(sys.argv[1], "r"))

    except ValueError:

        print 'Usage: python karaoke.py file.smil'
        raise SystemExit

    Karaoke = KaraokeLocal(fich)
    print Karaoke.__str__()
    Karaoke.do_local()
    print Karaoke.__str__()
