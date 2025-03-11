import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.ERROR)

@contextmanager
def suprimir_e_registrar_excecoes():
    try:
        yield  
    except Exception as e:
        logging.error("Ocorreu uma exceção: %s", e)

if __name__ == "__main__":
    with suprimir_e_registrar_excecoes():
        raise ValueError("Erro.")
    
