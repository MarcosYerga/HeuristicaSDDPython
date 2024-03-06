import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

def obtener_variables(expresion_str):
    # Parsear la expresión para obtener el árbol de sintaxis
    expr = parse_expr(expresion_str)
    # Obtener las variables en el orden en que aparecen
    variables = list(expr.free_symbols)
    # Obtener la posición de cada variable en la expresión original
    posicion_variables = [expresion_str.index(str(variable)) for variable in variables]
    # Unir las variables con sus posiciones
    variables_ordenadas = sorted(zip(variables, posicion_variables), key=lambda x: x[1])
    # Extraer las variables ordenadas
    variables_ordenadas = [variable for variable, _ in variables_ordenadas]
    return variables_ordenadas

def contar_operaciones(expr):
    num_and = expr.count('&')
    num_or = expr.count('|')
    return num_and + num_or

def simplificar_expresion(expresion_str):
    # Obtener las variables en el orden en que aparecen
    variables = obtener_variables(expresion_str)

    # Definir la expresión booleana a partir de la entrada del usuario
    expr = parse_expr(expresion_str)

    # Variables para almacenar el orden de las variables con menos operaciones
    orden_variables = []
    min_operaciones_variable = float('inf')
    min_op_variable = None
    expr_simpl_menor = None
    for variable in variables:
        print(f"\nSustituyendo para la variable {variable}:")
        for valor in [True, False]:
            # Copiar la expresión original para mantenerla sin cambios
            expr_copy = expr.copy()
            # Sustituir la variable por el valor correspondiente en la copia
            nueva_expr = expr_copy.subs(variable, valor)
            # Simplificar la expresión
            expr_simplified = sp.simplify_logic(nueva_expr)
            # Contar el número de operaciones
            operaciones_expr_simplified = contar_operaciones(str(expr_simplified))
            # Actualizar el mínimo de operaciones
            if operaciones_expr_simplified < min_operaciones_variable:
                min_operaciones_variable = operaciones_expr_simplified
                minop=variable
                exp_simpl_menor = expr_simplified
            # Imprimir la expresión resultante y el número de operaciones
            print(f"Expresión con {variable}={valor}: {expr_simplified} ({operaciones_expr_simplified} operaciones)")
        
        # Guardar el mínimo de operaciones para esta variable
        orden_variables.append((variable, min_operaciones_variable))
        
    # Ordenar las variables por el orden en que aparecen en la expresión
    orden_variables.sort(key=lambda x: expresion_str.index(str(x[0])))

    exprString = str(exp_simpl_menor)
    variables_no_presentes = [var for var in variables if var not in exp_simpl_menor.free_symbols]
    OrdenVariables.append(minop)
    # Luego agregar las otras variables que no están en exp_simpl_menor
    for var in variables_no_presentes:
        if var not in OrdenVariables:
            OrdenVariables.append(var)
            
    # Imprimir la variable con menos operacione
    print(f"\nVariable con menos operaciones: {minop} y la función resultante es {exp_simpl_menor} ")
    return exprString
# Solicitar al usuario la función booleana
expresion_str = input("Introduce la expresión booleana (usando 'and', 'or', 'not' y paréntesis si es necesario): ")

# Llamar a la función principal
OrdenVariables = []
while True:
    resultado = simplificar_expresion(expresion_str)
    if resultado == True or resultado == False or len(resultado)==1:
        if len(resultado)==1:
            OrdenVariables.append(resultado)
        break
    expresion_str = resultado


OrdenVariables = [str(elemento) for elemento in OrdenVariables]  
print(OrdenVariables)