# AfroCodigosFy - Venda de passagens no precinho

Crie um sistema de venda de passagens aéreas, projetado para facilitar a reserva de voos para os clientes. Eles podem comprar passagens aéreas para viagens entre diferentes cidades.

## Descrição Técnica

### Cadastro de Passagens Aéreas:

Os usuários podem comprar passagens aéreas, inserindo informações como _origem_, _destino_ e _preço_ da passagem.
Cada passagem é representada por um objeto da classe _PassagemAerea_, que _armazena_ essas _informações_.

### Gerenciamento de Passagens:

O gerenciamento de passagens é realizado pela classe _PassagensAereasManager_, que mantém uma _lista_ de todas as _passagens compradas_.
Os usuários podem _adicionar passagens_ à lista por meio do método _adicionar_passagem()_.

### Exibição de Passagens:

As passagens compradas podem ser listadas para visualização.
O método _listar_passagens()_ da classe _PassagensAereasManager_ é _responsável_ por _exibir as informações de todas as passagens compradas_.

### Menu de Opções:

O programa oferece um menu com opções para comprar passagens, listar passagens compradas e sair do programa.

### Encerramento do Programa:

Os usuários têm a opção de sair do programa a qualquer momento, encerrando a execução.