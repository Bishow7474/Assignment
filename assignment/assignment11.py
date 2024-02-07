def generate_fibonacci(n):
    sequence = [0,1]
    for _ in range(2,n):
        next_term = sequence[-1]+sequence[-2]
        sequence.append(next_term)
        return sequence
n_terms =10
fib_sequence = generate_fibonacci(n_terms)
print("Fibonacci sequence:",fib_sequence)
