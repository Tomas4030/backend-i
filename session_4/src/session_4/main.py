class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers  
        self.iterator = iter(self.numbers) 

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                num = next(self.iterator) 
                if num % 2 == 0:
                    return num
            except StopIteration:
                raise StopIteration 

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibo = fibonacci(10)

even_fibo = EvenIterator(fibo)

for num in even_fibo:
    print("Fibonacci number:", num)
