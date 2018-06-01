#!/usr/bin/env python3
"""
Módulo Main: Programa principal (controlador).

Proyecto de Farmacia -
Ejecute "menu" para más información
"""
from Modelo.farmacia import Farmacia
from estante import Estante
from Vista.repl import REPL
from Vista.repl import strip
import os


class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.comandos = {
        "agregar": self.agregar,
        "borrar": self.borrar,
        "listar": self.listar,
        "modificar": self.modificar,
        "buscar": self.buscar,
        "menu": self.menu,
        "salir": self.salir
        }
        archivo = "farmacia.db"
        introduccion = strip(__doc__)
        self.medicina = Estante(archivo)
        if not self.medicina.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, medicamento, codigo):
        """
        Agrega un medicamento con su codificacion.

        Ingrese: agregar "nombre de su medicamento"  "codigo"
        """
        self.medicina[medicamento] = Farmacia(medicamento, codigo, "No vencido")

    def borrar(self, medicamento):
        """
        Borrar un medicamento.

        Ingrese: borrar "nombre de su medicamento"
        """
        del self.medicina[medicamento]
        return print("Se borro el medicamento")

    def listar(self):
     """
     Retorna todos los medicamentos del stock

     Este comando no requiere de parámetros.
     """
     if os.stat("farmacia.db.dat").st_size==0:
            return ("No existen medicamentos")
     else:
            return (self.medicina[medicamento]
            for medicamento in sorted(self.medicina))

    def modificar(self, medicamento, estado_vencimiento):
        """
        Modificar un Medicamento

        Ejemplo: modificar [nombre de su Medicamento] [estado_vencimiento]
        """
        self.medicina[medicamento] = Farmacia(medicamento, "Vencido")
        return "{}--> Se modifico exitosamente".format(self.medicina[medicamento])

    def buscar(self, cadena):
        """
        Retorna un medicamento.

        Ingrese: buscar "nombre de su  medicamento"
        """
        return (self.medicina[medicamento]
        for medicamento in sorted(self.medicina)
        if cadena in medicamento)

    def menu(self, comando=None):
        """
        Retorna la lista de comandos disponibles.

        comando -- Comando del que se desea obtener ayuda (opcional).
        """
        if comando in self.comandos:
            salida = strip(self.comandos[comando].__doc__)
        else:
            salida = "Sintaxis: comando [parámetro1] [parámetro2] [parámetro3][..]\n" + \
            "Comandos: " + \
            ", ".join(sorted(self.comandos.keys()))
            return salida

    def salir(self):
        """
        Sale de la aplicación.

        Este comando no requiere de parámetros.
        """
        quit()


if __name__ == "__main__":
    Main()