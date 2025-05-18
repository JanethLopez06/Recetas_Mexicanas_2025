"""Colors"""
from enum import Enum

# E74C3C


class Color(Enum):
    ACCENT = "#e0632b"
    PRIMARY = "#feebc7"
    SECONDARY = "#f5b83a"
    BACKGROUND = "#000000"
    EARTH = "#D6B591"

    # PARA LAS ENTRADAS DEL MENÚ DE RECETAS
    ENTRADA = "#f5d6a5"
    ANTOJITOS="#f0a500"
    P_FUERTES="#4f5d75"
    POSTRES="#d9b8b1"


class TextColor(Enum):
    ACCENT = "#882d26"
    PRIMARY = "#363826"  # Para la fuente textos
    SECONDARY = "#2C3E50"
    TERCIARY = "#34495E"
    LINK = "#16A085"  # - Para enlaces.
