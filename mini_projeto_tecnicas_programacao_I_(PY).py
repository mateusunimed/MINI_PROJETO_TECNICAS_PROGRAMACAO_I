#%%

## Importa a biblioteca NUMPY

import numpy as np

#%%

## Simula a jogada de dois dados e retorna a soma dos valores

def simulador_dados():

    primeiro_dado = np.random.randint (1,7)

    segundo_dado = np.random.randint (1,7)

    return primeiro_dado + segundo_dado

simulador_dados()

#%%

## Simula 1.000 jogadas e armazena a os resultados e a soma

rodadas = np.array ([simulador_dados() for _ in range (1000)])

print (f'\n\nArray: {rodadas}')

print (f'\n\nSoma: {rodadas.sum()}')

#%%

## Calculo da média, maior e menor lançamento e frequencia de cada lançamento

media = rodadas.mean()

lancamento_maximo = rodadas.max()

lancamento_minimo = rodadas.min()

unicos,contagens = np.unique(rodadas, return_counts=True)

frequencia = dict(zip(unicos,contagens))

#%%

print (f'Média: {media}\n\n'
       f'Lançamento máximo: {lancamento_maximo}\n\n'
       f'Lançamento mínimo: {lancamento_minimo}\n\n'
       f'Frequência de lançamentos: {frequencia}\n\n')

# %%
