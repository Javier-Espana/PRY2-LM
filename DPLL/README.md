# SAT Solver - Algoritmo DPLL

## Descripción

Este programa implementa un solver para el problema de satisfacibilidad booleana (SAT) utilizando el algoritmo DPLL (Davis–Putnam–Logemann–Loveland).

## Estructura del Proyecto

- `dpll_solver.py`: Módulo principal con la clase `DPLLSolver`
- `main.py`: Archivo principal con ejemplos e instrucciones de mejora

## Algoritmo DPLL

El algoritmo DPLL es un método de backtracking que mejora la fuerza bruta mediante:

### Pasos del Algoritmo

1. **Entrada de datos**: Fórmula en CNF y asignación vacía
2. **Caso base (éxito)**: Si fórmula vacía → True + asignación
3. **Caso base (fracaso)**: Si cláusula vacía → False
4. **Selección de literal**: Escoge variable no asignada
5. **Propagación True**: Elimina cláusulas satisfechas, reduce otras
6. **Propagación False**: Si falla, intenta con valor opuesto
7. **Backtracking**: Si ambas fallan → False

### Ventajas sobre Fuerza Bruta

- **Poda temprana**: Detecta conflictos antes de asignar todas las variables
- **Propagación**: Elimina cláusulas satisfechas automáticamente
- **Backtracking inteligente**: No explora ramas inválidas

## Uso

```bash
# Ejecutar programa principal
python3 main.py

# Uso programático
from dpll_solver import DPLLSolver
solver = DPLLSolver()
satisfacible, asignacion = solver.solve([['p', '¬q'], ['q', 'r']])
```

## Optimizaciones Futuras

El archivo `main.py` contiene instrucciones detalladas para implementar:

1. **Propagación de literales unitarios**
2. **Eliminación de literales puros**
3. **Heurísticas de selección (VSIDS, Jeroslow-Wang)**
4. **Aprendizaje de cláusulas (CDCL)**

## Complejidad

- **Mejor caso**: O(n) con propagación efectiva
- **Peor caso**: O(2^n) igual que fuerza bruta
- **Promedio**: Significativamente mejor que fuerza bruta debido a la poda
