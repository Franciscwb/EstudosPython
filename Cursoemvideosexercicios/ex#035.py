print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
r1 = float(input('Primeiro número: '))
r2 = float(input('Segundo número: '))
r3 = float(input('Terceiro número: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')
