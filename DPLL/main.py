'''
SAT Solver DPLL - main
======================

Script principal para probar el solver SAT usando DPLL (Davis–Putnam–Logemann–Loveland).
Aquí se arman ejemplos y se muestra cómo funciona el algoritmo paso a paso

DPLL es un algoritmo de backtracking que mejora la fuerza bruta eliminando cláusulas satisfechas y simplificando la fórmula en cada paso

Cosas clave:
 - Si la fórmula queda vacía, es SATISFACIBLE
 - Si hay una cláusula vacía, es INSATISFACIBLE
 - Se elige el primer literal que se encuentre
 - Se eliminan cláusulas satisfechas y literales opuestos
 - Hace backtracking: prueba True, si no va, prueba False
'''
from dpll_solver import DPLLSolver


def print_formula_readable(formula: list) -> str:
    #convierte la fórmula a una cadena legible tipo (p ∨ ¬q) ∧ (q ∨ r)
    clause_strings = []
    for clause in formula:
        if len(clause) == 1:
            clause_strings.append(clause[0])
        else:
            clause_strings.append(f"({' ∨ '.join(clause)})")
    return ' ∧ '.join(clause_strings)


def demonstrate_dpll_steps(solver: DPLLSolver, formula: list, example_name: str):
    #muestra paso a paso cómo trabaja el DPLL con la fórmula dada
    print(f"\n{example_name}")
    print("=" * len(example_name))
    
    formula_readable = print_formula_readable(formula)
    print(f"Fórmula: {formula_readable}")
    print(f"Representación interna: {formula}")
    
    #parseo para ver variables encontradas
    clauses = solver.parse_formula(formula)
    print(f"Variables encontradas: {sorted(list(solver.variables))}")
    print(f"Cláusulas como conjuntos: {clauses}")
    
    #ejecutar DPLL
    print("\n--- Ejecutando algoritmo DPLL ---")
    is_satisfiable, assignment = solver.solve(formula)
    
    print(f"Resultado: {'SATISFACIBLE' if is_satisfiable else 'INSATISFACIBLE'}")
    
    if is_satisfiable:
        print(f"Asignación encontrada: {assignment}")
        print("Verificación:")
        for var, value in sorted(assignment.items()):
            print(f"  {var} = {'Verdadero' if value else 'Falso'}")
    else:
        print("No existe asignación que satisfaga la fórmula")


def main():
    #pruebas de ej para el SAT Solver DPLL
    print("SAT Solver - Algoritmo DPLL")
    print("(Davis–Putnam–Logemann–Loveland)")
    print("=" * 50)
    
    #Ej 1: Satisfacible simple
    solver1 = DPLLSolver()
    formula1 = [['p', '¬q'], ['q', 'r']]
    demonstrate_dpll_steps(solver1, formula1, "Ejemplo 1: (p ∨ ¬q) ∧ (q ∨ r)")
    
    #Ej 2: Insatisfacible clásico
    solver2 = DPLLSolver()
    formula2 = [['p'], ['¬p']]
    demonstrate_dpll_steps(solver2, formula2, "Ejemplo 2: p ∧ ¬p (contradicción)")
    
    #Ej 3: Más complejo, pero satisfacible
    solver3 = DPLLSolver()
    formula3 = [['a', 'b'], ['¬a', 'c'], ['¬b', '¬c']]
    demonstrate_dpll_steps(solver3, formula3, "Ejemplo 3: (a ∨ b) ∧ (¬a ∨ c) ∧ (¬b ∨ ¬c)")
    
    #Ej 4: Fórmula vacía (siempre SAT)
    solver4 = DPLLSolver()
    formula4 = []
    demonstrate_dpll_steps(solver4, formula4, "Ejemplo 4: Fórmula vacía")
    
    #Ej 5: Cláusula unitaria
    solver5 = DPLLSolver()
    formula5 = [['x'], ['¬x', 'y'], ['¬y', 'z']]
    demonstrate_dpll_steps(solver5, formula5, "Ejemplo 5: x ∧ (¬x ∨ y) ∧ (¬y ∨ z)")
    
    #Ej 6: 3-SAT más complicado
    solver6 = DPLLSolver()
    formula6 = [
        ['a', 'b', 'c'],
        ['¬a', '¬b', 'c'],
        ['a', '¬b', '¬c'],
        ['¬a', 'b', '¬c']
    ]
    demonstrate_dpll_steps(solver6, formula6, 
                          "Ejemplo 6: (a∨b∨c) ∧ (¬a∨¬b∨c) ∧ (a∨¬b∨¬c) ∧ (¬a∨b∨¬c)")
    
if __name__ == "__main__":
    main()


