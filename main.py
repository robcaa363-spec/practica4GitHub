def calcular_varianza(datos, poblacional=True):
    """
    Calcula la varianza de una lista de números.
    
    Parámetros:
        datos (list): lista de valores numéricos
        poblacional (bool): True para varianza poblacional (÷n),
                             False para varianza muestral (÷n-1)
    
    Retorna:
        float: la varianza
    """
    n = len(datos)
    if n == 0:
        raise ValueError("La lista no puede estar vacía")
    if not poblacional and n == 1:
        raise ValueError("Se necesitan al menos 2 datos para varianza muestral")
    
    media = sum(datos) / n
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    
    divisor = n if poblacional else (n - 1)
    return suma_cuadrados / divisor 

numeros = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
print("Varianza poblacional:", calcular_varianza(numeros))
print("Varianza muestral:", calcular_varianza(numeros, poblacional=False)) 