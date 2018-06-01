#!/usr/bin/env python3
"""
Módulo Agenda: Clase principal (modelo).

Proyecto de ejemplo - Paradigmas de la Programación
"""


class Farmacia:
    """Stock de medicamentos para la venta."""

    def __init__(self, medicamento, codigo, estado_vencimiento):
        """Constructor: Inicializa propiedades de instancia."""
        self.medicamento = medicamento
        self.codigo = codigo
        self.estado_vencimiento = estado_vencimiento

    def __str__(self):
        """Cadena de representación."""
        return "Medicamento:{} Codigo:{} Estado de Vencimiento:{}".format(self.medicamento, self.codigo, self.estado_vencimiento)

def main():
    """Función principal (ejemplo de uso)."""
    medicamento = {}

    medicamento["paracetamol"] = Farmacia("paracetamol", "222", "No Vencido")
    medicamento["salbutamol"] = Farmacia("salbutamol", "444", "No Vencido")
    medicamento["ibuprofeno"] = Farmacia("ibuprofeno", "666", "No Vencido")

    for clave in medicamento:
        print(medicamento[clave])


if __name__ == "__main__":
    main()
