"""
Programa Principal - SAT Solver Fuerza Bruta
==========================================

Punto de entrada principal para el SAT Solver que utiliza el algoritmo de fuerza bruta.

Uso:
    python main.py

Autor: Sistema SAT Solver
Fecha: 2025
"""

from sat_solver import SATSolver


def main():
    """
    Función principal que demuestra el uso del SAT Solver.
    """
    print("SAT Solver - Método de Fuerza Bruta")
    print("=" * 40)
    
    # Crear instancia del solver
    solver = SATSolver()
    
    # Ejemplo 1: Fórmula satisfacible
    print("\nEjemplo 1: (p ∨ ¬q) ∧ (q ∨ r)")
    formula1 = [['p', '¬q'], ['q', 'r']]
    
    satisfacible1, asignacion1 = solver.solve(formula1)
    
    print(f"Fórmula: {formula1}")
    print(f"Resultado: {'SATISFACIBLE' if satisfacible1 else 'INSATISFACIBLE'}")
    if satisfacible1:
        print(f"Asignación encontrada: {asignacion1}")
    
    # Ejemplo 2: Fórmula insatisfacible
    print("\nEjemplo 2: p ∧ ¬p")
    solver2 = SATSolver()
    formula2 = [['p'], ['¬p']]
    
    satisfacible2, asignacion2 = solver2.solve(formula2)
    
    print(f"Fórmula: {formula2}")
    print(f"Resultado: {'SATISFACIBLE' if satisfacible2 else 'INSATISFACIBLE'}")
    if satisfacible2:
        print(f"Asignación encontrada: {asignacion2}")
    
    # Ejemplo 3: Fórmula más compleja
    print("\nEjemplo 3: (a ∨ b) ∧ (¬a ∨ c) ∧ (¬b ∨ ¬c)")
    solver3 = SATSolver()
    formula3 = [['a', 'b'], ['¬a', 'c'], ['¬b', '¬c']]
    
    satisfacible3, asignacion3 = solver3.solve(formula3)
    
    print(f"Fórmula: {formula3}")
    print(f"Resultado: {'SATISFACIBLE' if satisfacible3 else 'INSATISFACIBLE'}")
    if satisfacible3:
        print(f"Asignación encontrada: {asignacion3}")


if __name__ == "__main__":
    main()
