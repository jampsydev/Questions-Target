import json


faturamento_json = '''
{
    "faturamento_diario": [1000, 2000, 0, 3000, 4000, 5000, 0, 6000]
}
'''


dados = json.loads(faturamento_json)
faturamento = [valor for valor in dados['faturamento_diario'] if valor > 0]


menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)


media_mensal = sum(faturamento) / len(faturamento)


dias_acima_da_media = len([dia for dia in faturamento if dia > media_mensal])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias acima da média: {dias_acima_da_media}")
