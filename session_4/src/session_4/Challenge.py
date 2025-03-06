texto = [
    "   tesdsfdsfte 123    ",
    "tesdsfdsfte 2324123",
    "                           ",
    "tesddsdte 132432423",
    "tesfgfggftÈ 13432423",
    "       ",
    "tgbgfeste 145423",
]


def ver_arry(texto):
    for i, linha in enumerate(texto, start=1):

        linha_limpa = linha.strip()

        if linha_limpa:
             yield f"Index {i}. {linha_limpa}"


for index in ver_arry(texto):
    print(index)
