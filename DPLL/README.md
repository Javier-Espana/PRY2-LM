# SAT Solver - Algoritmo DPLL

Un solver para el problema de satisfacibilidad booleana (SAT) utilizando el algoritmo DPLL (Davis–Putnam–Logemann–Loveland)

### Pasos del Algoritmo
1. **Entrada de datos**: formula en CNF y asignación vacía
2. **Caso base (éxito)**: si fórmula vacía es True + asignación
3. **Caso base (fracaso)**: si cláusuula vacía es False
4. **Selección de literal**: escoge variable no asignada
5. **Propagación True**: elimina cláusulas satisfechas, reduce otras
6. **Propagación False**: si falla, intenta con valor opuesto
7. **Backtracking**: si ambas fallan es Faalse

### Ventajas sobre Fuerza Bruta
- **Poda temprana**: detecta conflictos antes de asignar todas las variables
- **Propagación**: elimina cláusulas satsfechas automáticamente
- **Backtracking inteligente**: no explora ramas inválidas

## Uso
```bash
# EPrograma principal
python3 main.py

# Uso programático
from dpll_solver import DPLLSolver
solver = DPLLSolver()
satisfacible, asignacion = solver.solve([['p', '¬q'], ['q', 'r']])
```
