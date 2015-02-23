#!/usr/bin/python

import webapp

class Adios_Webapp (webapp.webApp):
    def parse(self, request):
        return None

    def process(self, parsedRequest):
        return("200 OK", "ADIOS MUNDO CRUEL")

if __name__ == "__main__":
    servidor = Adioss_Webapp("localhost", 1234)
