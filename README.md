# UrnaEletronica

## :memo: Descrição
O projeto simula uma urna eletrônica para governandor, prefeito e presidente. O programa conta com cadastro de usuários e candidatos, além de calcular os vencedores e mostrar os resultados de diversas formas. 

## Funções
* **Cadastro de Candidatos:** Essa função pede que o usuário digite o nome, o cargo e o partido do candidato. Todas as informações são armazenadas em um arquivo chamado lista.txt
* **Cadastro de eleitores:** Nessa função, o eleitor precisa digitar o nome e o cpf que serão armazenados em uma lista
* **Votar:** Essa função realiza os votos individuais de cada eleitor. O voto ocorre em 3 etapas, sendo a primeira para governador, a segunda para prefeito e a terceira para presidente. O programa imprime na tela os nomes, o número e o partido do candidato em formato de tabela (obs: o número do canditato é gerado pelo programa). Dessa forma, o programa pede para que o eleitor primeiro confirme que é um eleitor fazendo uma autenticação simples de nome e cpf e, depois segue para a votação.
* **Resultado:** O resultado mostra em formato de tabela os rankings dos candidatos. As tabelas contém o nome, o partido, o total de votos e a porcentagem dos votos válidos dos candidatos e ordena no formato de rankings os colocados de acordo com a quantidade de votos totais.
* **Relatório:** O relatório é uma função que exibe uma lista dos eleitores que votaram ordenados por nome. O programa verifica se a quantidade de eleitores é igual ao total de votos que foram registrados na eleição


## :wrench: Tecnologias utilizadas
* Python

## :dart: Status do projeto
* :heavy_check_mark:  InProgress

## Próximas implementações
Eu quero implementar um GUI para facilitar a interação com o usuário
