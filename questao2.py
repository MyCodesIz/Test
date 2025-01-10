def fibonacci_check(number):
   
    a, b = 0, 1
    
    while b <= number:
        if b == number:  
            return f"O número {number} pertence à sequência de Fibonacci."
        a, b = b, a + b 

    return f"O número {number} NÃO pertence à sequência de Fibonacci."

num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

print(fibonacci_check(num))