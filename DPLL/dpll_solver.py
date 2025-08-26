"""
SAT Solver usando DPLL
"""

from typing import List, Set, Dict, Tuple, Optional
import copy

class DPLLSolver:
    """
    Clase solver SAT
    El DPLL que mejora la fuerza bruta mediante la eliminacioon de clausulas y simplificacin de la fórmula.
    """
    
    def __init__(self):
        self.variables: Set[str] = set()
        self.original_clauses: List[Set[str]] = []
    
    def parse_formula(self, formula: List[List[str]]) -> List[Set[str]]:
        """
        Parsea una formula booleana en CNF y extrae variables y clausulas
        
        Args: formula: Lista de listas donde cada sublista representa una clausula y cada string es un literal (variable o ¬variable)
        Returns: Lista de conjuntos representando las cláusulas
        """
        clauses = []
        self.variables = set()
        
        for clause_list in formula:
            #clausula a un conjunto
            clause = set(clause_list)
            clauses.append(clause)
            
            #extraer vars de cada literal
            for literal in clause:
                if literal.startswith('¬'):
                    #literal neg
                    variable = literal[1:]
                else:
                    #literal positivo
                    variable = literal
                self.variables.add(variable)
        
        self.original_clauses = clauses
        return clauses
    
    def get_complement_literal(self, literal: str) -> str:
        """
        Obtiene el literal complementario de un literal dado.
        
        Args: literal: Literal (variable o ¬variable)
        Returns:literal complementario
        """
        if literal.startswith('¬'):
            #negativo, devolver positivo
            return literal[1:]
        else:
            #positivo, devolver negativo
            return '¬' + literal
    
    def select_literal(self, clauses: List[Set[str]]) -> Optional[str]:
        """
        Selecciona un literal de las clausulas para branching.
        Selecciona el primer literal que encuentre en las clausulas no vacias
        
        Args:clauses: Lista de clausulas (conjuntos de literales
        Returns:Un literal para hacer branching, o None si no hay literales
        """
        for clause in clauses:
            if clause:  #clausula no está vacía
                #toma cualquier literal de la clausula
                literal = next(iter(clause))
                #a forma positiva si es necesario
                if literal.startswith('¬'):
                    return literal[1:]
                else:
                    return literal
        return None
    
    def simplify_formula(self, clauses: List[Set[str]], literal: str, value: bool) -> List[Set[str]]:
        """
        1. si literal=True: eliminar clausula que contienen el literal
        2. eliminar el literal complementario de las clausula restantes
        """
        simplified_clauses = []
        
        if value:
            #Si literal=True, entonces 'literal' satisface y '¬literal' contradice
            satisfying_literal = literal
            contradicting_literal = '¬' + literal
        else:
            #si literal=False, entonces '¬literal' satisface y 'literal' contradice
            satisfying_literal = '¬' + literal
            contradicting_literal = literal
        
        for clause in clauses:
            if satisfying_literal in clause:
                #Si la clausula contiene el literal satisfactorio,
                #toda la clausula es verdadera tons eliminar clausula
                continue
            else:
                #La clausula no se satisface automáticamente
                #crear nueva clausula sin el literal contradictorio
                new_clause = clause - {contradicting_literal}
                simplified_clauses.append(new_clause)
        
        return simplified_clauses
    
    def dpll_recursive(self, clauses: List[Set[str]], assignment: Dict[str, bool]) -> Tuple[bool, Dict[str, bool]]:
        """     
        Algoritmo DPLL según las especificaciones: CASOS
        
        Args:clauses: Lista de cláusulas actuales, assignment: Asignación parcial actual
        Returns:Tupla (es_satisfacible, asignacion_completa)
        """
        
        #CASO BASE 1: Si B es vacia, regresar True e I
        if not clauses:
            return True, assignment.copy()
        
        #CASO BASE 2: Si hay alguna disyunción vacia en B, regresar False
        for clause in clauses:
            if not clause:
                return False, {}
        
        #SELECCIÓN DE LITERAL
        literal = self.select_literal(clauses)
        if literal is None:
            return False, {}
        
        # PRIMERA RAMA: Asignar L = True
        #elim clausulas que contienen L y ocurrencias de ¬L
        simplified_clauses_true = self.simplify_formula(clauses, literal, True)
        
        # I' = I ∪ {L es verdadero}
        assignment_true = assignment.copy()
        assignment_true[literal] = True
        
        # resultado e I1 ← DPLL(B',I')
        result_true, final_assignment_true = self.dpll_recursive(simplified_clauses_true, assignment_true)
        
        #if resultado es verdadera, entonces regresar True e I1
        if result_true:
            return True, final_assignment_true
        
        #SEGUNDA RAMA: Asignar L = False
        #elim clausulas que contienen ¬L y ocurrencias de L
        simplified_clauses_false = self.simplify_formula(clauses, literal, False)
        
        #I'' = I ∪ {L es falso}
        assignment_false = assignment.copy()
        assignment_false[literal] = False
        
        #result e I2 ← DPLL(B'',I'')
        result_false, final_assignment_false = self.dpll_recursive(simplified_clauses_false, assignment_false)
        
        #regresar result e I2
        return result_false, final_assignment_false
    
    def solve(self, formula: List[List[str]]) -> Tuple[bool, Dict[str, bool]]:
        """
        Resuelve el problema SAT usando el algoritmo DPLL.
        """
        #parsear la fórmula para obtener las cláusulas
        clauses = self.parse_formula(formula)
        
        #init con asignación vacía
        initial_assignment = {}
        
        #call al algoritmo DPLL recursivo
        is_satisfiable, satisfying_assignment = self.dpll_recursive(clauses, initial_assignment)
        
        return is_satisfiable, satisfying_assignment
    
