import json

def analisar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        faturamento = json.load(file)
    
   
    valores_validos = [dia["faturamento"] for dia in faturamento if dia["faturamento"] > 0]
    
    if not valores_validos:
        return "Não há faturamento válido no período."
    
    menor_valor = min(valores_validos)
    maior_valor = max(valores_validos)
    
    media_mensal = sum(valores_validos) / len(valores_validos)
    
    dias_acima_da_media = sum(1 for dia in valores_validos if dia > media_mensal)
    
    return {
        "Menor valor de faturamento": menor_valor,
        "Maior valor de faturamento": maior_valor,
        "Dias acima da média mensal": dias_acima_da_media
    }

arquivo = "faturamento.json"
s
resultado = analisar_faturamento(arquivo)
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
