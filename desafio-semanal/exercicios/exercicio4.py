# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não:
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.


def count_repeat_items(list):
    result = {}
    for item in list:
        result[item] = list.count(item)
    show_result_count_items(result)


def show_result_count_items(result):
    for key, value in sorted(result.items()):
        print(f'A fruta {key} aparece {value} vez(es).')


fruit_list = ['melancia', 'cajá', 'morango', 'uva', 'jaca', 'uva', 'morango', 'uva']
count_repeat_items(fruit_list)
