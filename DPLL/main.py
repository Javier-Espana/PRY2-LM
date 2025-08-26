"""
Programa Principal - SAT Solver DPLL
===================================

INSTRUCCIONES PARA IMPLEMENTAR EL ALGORITMO DPLL:

El algoritmo DPLL (Davis–Putnam–Logemann–Loveland) es un método de backtracking
para resolver el problema SAT que mejora la fuerza bruta mediante:

1. ENTRADA DE DATOS:
   - Fórmula en forma clausal (igual que fuerza bruta)
   - Asignación vacía al inicio: assignment = {}

2. CASO BASE 1 (ÉXITO):
   - Si la fórmula está vacía (todas las cláusulas fueron satisfechas)
   - → devuelve True y la asignación actual

3. CASO BASE 2 (FRACASO):
   - Si alguna cláusula es vacía (sin literales)
   - → devuelve False y asignación vacía

4. SELECCIÓN DE LITERAL:
   - Escoge un literal no asignado (ej: el primero que aparezca)
   - Esto introduce el carácter no determinista del algoritmo

5. PROPAGACIÓN AL ASIGNAR TRUE:
   - Crea nueva fórmula eliminando cláusulas que contienen ese literal
   - Elimina el literal complementario de las demás cláusulas
   - Añade la asignación (literal=True) a la asignación parcial
   - Llama recursivamente a DPLL
   - Si devuelve satisfacible → propaga True

6. PROPAGACIÓN AL ASIGNAR FALSE:
   - Si la primera llamada falló, repite con el literal complementario
   - Si devuelve satisfacible → propaga True

7. DEVOLVER INSATISFACIBILIDAD:
   - Si ninguna de las dos asignaciones funciona
   - → devuelve False y asignación vacía

PASOS PARA COMPLETAR LA IMPLEMENTACIÓN:

TODO: Implementar las siguientes optimizaciones en dpll_solver.py:

1. PROPAGACIÓN DE LITERALES UNITARIOS:
   - Detectar cláusulas unitarias (con un solo literal)
   - Asignar automáticamente el valor que satisface la cláusula
   - Propagar esta asignación antes del branching

2. ELIMINACIÓN DE LITERALES PUROS:
   - Detectar literales que aparecen solo en forma positiva o negativa
   - Asignar el valor que satisface todas sus ocurrencias
   - Eliminar las cláusulas que los contienen

3. HEURÍSTICAS DE SELECCIÓN:
   - Implementar heurística VSIDS (Variable State Independent Decaying Sum)
   - O heurística Jeroslow-Wang para selección de variables
   - Mejora significativamente el rendimiento

4. APRENDIZAJE DE CLÁUSULAS (CDCL):
   - Analizar conflictos para generar cláusulas aprendidas
   - Implementar non-chronological backtracking
   - Esto convierte DPLL en CDCL (más moderno)

ESTRUCTURA ACTUAL:
- dpll_solver.py: Implementación básica del algoritmo DPLL
- main.py: Este archivo con ejemplos y instrucciones
"""

from dpll_solver import DPLLSolver


