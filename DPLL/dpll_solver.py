"""
SAT Solver usando Algoritmo DPLL (Davis–Putnam–Logemann–Loveland)
===============================================================

Este módulo implementa un solver para el problema de satisfacibilidad booleana (SAT)
utilizando el algoritmo DPLL con backtracking.

"""

from typing import List, Set, Dict, Tuple, Optional
import copy


class DPLLSolver:
    """
    Clase que implementa un solver SAT usando el algoritmo DPLL.
    
    El algoritmo DPLL es un método de backtracking que mejora la fuerza bruta
    mediante propagación de literales unitarios y eliminación de cláusulas puras.
    """
    
