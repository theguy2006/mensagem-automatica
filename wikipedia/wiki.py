import requests

HEADERS = {"User-Agent": "MinhaIAWikipedia/1.0 (estudo pessoal)"}

def buscar_pessoa(nome):
    url = "https://pt.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": nome,
        "gsrlimit": 1,
        "prop": "extracts",
        "explaintext": True,   # texto puro, sem HTML
        "exsectionformat": "plain",
    }
    resposta = requests.get(url, params=params, headers=HEADERS, timeout=10)
    dados = resposta.json()

    paginas = dados.get("query", {}).get("pages")
    if not paginas:
        return None

    pagina = next(iter(paginas.values()))
    return pagina["title"], pagina["extract"]

while True:
    nome = input("\nDigite o nome de uma pessoa (ou 'sair'): ").strip()
    if nome.lower() == "sair":
        break

    resultado = buscar_pessoa(nome)
    if resultado is None:
        print("Não encontrei nada sobre essa pessoa.")
        continue

    titulo, texto = resultado
    print(f"\n=== {titulo} ===\n")
    print(texto)