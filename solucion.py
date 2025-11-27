def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return 
 # TODO: implementar la lógica para generar el reloj de arena en ASCII Logica aqui 
    caracter = s[0]
    for i in range(m):
        num_espacios = i
        num_caracteres = 2 * (m - i) - 1
        linea = " " * num_espacios + caracter * num_caracteres
        print(linea)
    if m > 1:
        for k in range(1, m):
            num_espacios = m - 1 - k
            num_caracteres = 2 * k + 1
            linea = " " * num_espacios + caracter * num_caracteres
            print(linea)
        
