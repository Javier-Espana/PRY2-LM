"""
SAT Solver usando Fuerza Bruta (Brute Force)
===========================================

Este módulo implementa un solver para el problema de satisfacibilidad booleana (SAT)
utilizando el método de fuerza bruta.

Autor: Sistema SAT Solver
Fecha: 2025
"""

from itertools import product
from typing import List, Set, Dict, Tuple


class SATSolver:
    """
    Clase que implementa un solver SAT usando fuerza bruta.
    
    La fórmula booleana se representa en Forma Normal Conjuntiva (CNF):
    - Una fórmula es una conjunción (AND) de cláusulas
    - Cada cláusula es una disyunción (OR) de literales  
    - Un literal es una variable o su negación
    
    Ejemplo: (p ∨ ¬q) ∧ (q ∨ r) se representa como [{'p', '¬q'}, {'q', 'r'}]
    """
    
    def __init__(self):
        """Inicializa el solver SAT."""
        self.variables: Set[str] = set()
        self.clauses: List[Set[str]] = []
    
    def parse_formula(self, formula: List[List[str]]) -> None:
        """
        Parsea una fórmula booleana en CNF y extrae variables y cláusulas.
        
        Args:
            formula: Lista de listas donde cada sublista representa una cláusula
                    y cada string es un literal (variable o ¬variable)
        
        Ejemplo:
            Entrada: [['p', '¬q'], ['q', 'r']]
            Representa: (p ∨ ¬q) ∧ (q ∨ r)
        """
        self.clauses = []
        self.variables = set()
        
        for clause_list in formula:
            # Convertir cada cláusula a un conjunto
            clause = set(clause_list)
            self.clauses.append(clause)
            
            # Extraer variables de cada literal
            for literal in clause:
                if literal.startswith('¬'):
                    # Literal negativo: ¬p → extraer variable p
                    variable = literal[1:]
                else:
                    # Literal positivo: p → variable es p
                    variable = literal
                self.variables.add(variable)
    
    def generate_all_assignments(self) -> List[Dict[str, bool]]:
        """
        Genera todas las posibles asignaciones de verdad para las variables.
        
        Para n variables, genera 2^n asignaciones posibles.
        
        Returns:
            Lista de diccionarios, cada uno representando una asignación
            donde las claves son variables y los valores son booleanos.
        """
        variables_list = sorted(list(self.variables))
        n_variables = len(variables_list)
        
        # Generar producto cartesiano {False,True}^n
        truth_values = list(product([False, True], repeat=n_variables))
        
        assignments = []
        for values in truth_values:
            assignment = dict(zip(variables_list, values))
            assignments.append(assignment)
        
        return assignments
    
    def evaluate_literal(self, literal: str, assignment: Dict[str, bool]) -> bool:
        """
        Evalúa un literal bajo una asignación de verdad específica.
        
        Args:
            literal: String representando el literal (ej: 'p' o '¬p')
            assignment: Diccionario con asignación de variables a valores booleanos
        
        Returns:
            Valor de verdad del literal
        """
        if literal.startswith('¬'):
            # Literal negativo: ¬p
            variable = literal[1:]
            return not assignment[variable]
        else:
            # Literal positivo: p
            return assignment[literal]
    
    def evaluate_clause(self, clause: Set[str], assignment: Dict[str, bool]) -> bool:
        """
        Evalúa una cláusula bajo una asignación de verdad.
        
        Una cláusula es verdadera si al menos uno de sus literales es verdadero.
        
        Args:
            clause: Conjunto de literales
            assignment: Diccionario con asignación de variables a valores booleanos
        
        Returns:
            True si la cláusula se satisface, False en caso contrario
        """
        for literal in clause:
            if self.evaluate_literal(literal, assignment):
                return True
        return False
    
    def evaluate_formula(self, assignment: Dict[str, bool]) -> bool:
        """
        Evalúa toda la fórmula bajo una asignación de verdad.
        
        Una fórmula es verdadera si todas sus cláusulas son verdaderas.
        
        Args:
            assignment: Diccionario con asignación de variables a valores booleanos
        
        Returns:
            True si la fórmula se satisface, False en caso contrario
        """
        for clause in self.clauses:
            if not self.evaluate_clause(clause, assignment):
                return False
        return True
    
    def solve(self, formula: List[List[str]]) -> Tuple[bool, Dict[str, bool]]:
        """
        Resuelve el problema SAT usando fuerza bruta.
        
        Args:
            formula: Fórmula booleana en CNF como lista de listas
        
        Returns:
            Tupla (es_satisfacible, asignacion_satisfactoria)
            - es_satisfacible: True si existe una asignación que satisface la fórmula
            - asignacion_satisfactoria: Asignación que satisface la fórmula, o {} si no existe
        """
        # Parsear la fórmula para extraer variables y cláusulas
        self.parse_formula(formula)
        
        # Casos base
        if not self.clauses:
            # Fórmula vacía es trivialmente satisfacible
            return True, {}
        
        if not self.variables:
            # Sin variables pero con cláusulas implica insatisfacibilidad
            return False, {}
        
        # Generar todas las asignaciones posibles
        all_assignments = self.generate_all_assignments()
        
        # Probar cada asignación
        for assignment in all_assignments:
            if self.evaluate_formula(assignment):
                # Encontrada asignación satisfactoria
                return True, assignment
        
        # No se encontró ninguna asignación satisfactoria
        return False, {}
