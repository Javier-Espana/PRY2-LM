# SAT Solver - Fuerza Bruta

## Descripción

Este programa implementa un solver para el problema de satisfacibilidad booleana (SAT) utilizando el algoritmo de fuerza bruta.

## Estructura del Proyecto

- `sat_solver.py`: Módulo principal que contiene la clase `SATSolver`
- `main.py`: Archivo principal de ejecución con ejemplos de uso

## Uso

### Ejecución básica
```bash
python3 main.py
```

### Uso programático
```python
from sat_solver import SATSolver

# Crear instancia del solver
solver = SATSolver()

# Definir fórmula en CNF
# Ejemplo: (p ∨ ¬q) ∧ (q ∨ r)
formula = [['p', '¬q'], ['q', 'r']]

# Resolver
satisfacible, asignacion = solver.solve(formula)

# Mostrar resultado
if satisfacible:
    print(f"SATISFACIBLE: {asignacion}")
else:
    print("INSATISFACIBLE")
```

## Formato de Entrada

La fórmula booleana debe estar en Forma Normal Conjuntiva (CNF):
- Lista de listas, donde cada sublista es una cláusula
- Cada cláusula es una lista de literales
- Literales positivos: `'p'`, `'q'`, `'r'`, etc.
- Literales negativos: `'¬p'`, `'¬q'`, `'¬r'`, etc.

### Ejemplos
- `[['p']]` → p
- `[['p'], ['¬p']]` → p ∧ ¬p
- `[['p', 'q'], ['¬p', 'r']]` → (p ∨ q) ∧ (¬p ∨ r)

## Algoritmo

1. **Entrada de datos**: Parsea la fórmula en CNF
2. **Identificar variables**: Extrae todas las variables únicas
3. **Generar asignaciones**: Crea todas las 2^n asignaciones posibles
4. **Evaluar fórmula**: Prueba cada asignación hasta encontrar una satisfactoria
5. **Devolver resultado**: Retorna si es satisfacible y la asignación encontrada

## Complejidad

- **Temporal**: O(2^n × m × k) donde n=variables, m=cláusulas, k=literales/cláusula
- **Espacial**: O(n + m×k)

El algoritmo es exponencial, por lo que es impracticable para fórmulas con más de 20-30 variables.
