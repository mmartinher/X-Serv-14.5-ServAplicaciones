#!/usr/bin/python

import webapp

class Saludos_Webapp (webapp.webApp):
    def parse(self, request):
        return None

    def process(self, parsedRequest):
        return("200 OK", "HOLA MUNDO")

if __name__ == "__main__":
    servidor = Saludos_Webapp("localhost", 1234)
