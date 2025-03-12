import typer
import time

app = typer.Typer()

@app.command()
def square(valor: int, valor2: int = 0, square: bool = False, addition: bool = False, subtraction: bool = False, multiplication: bool = False):
    start_time = time.time()

    results = []
 
    if square:
        results.append(f"resultado do quadrado: {valor**2}")

    if addition:
        results.append(f"resultado da soma: {valor + valor2}")

    if subtraction:
        results.append(f"resultado da subtração: {valor - valor2}")

    if multiplication:
        results.append(f"resultado da multiplicação: {valor * valor2}")

    for result in results:
        typer.echo(result)

    end_time = time.time()
    final_time = end_time - start_time

    typer.echo(f"Tempo de execução: {final_time:.4f} segundos")


if __name__ == "__main__":
    app()
