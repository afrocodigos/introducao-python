import pandas as pd

frutas = ['Banana', 'Maçã', 'Pera', 'Banana', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera']

df = pd.DataFrame(frutas, columns=['fruta'])

df_frutas = df.groupby('fruta').size().to_frame(name='Contagem')

print(df_frutas)