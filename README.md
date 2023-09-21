# Gerenciador de Registros com Python e MySQL

Este é um simples gerenciador de registros desenvolvido em Python utilizando a biblioteca MySQL Connector para interagir com um banco de dados MySQL. O programa oferece uma interface gráfica básica criada com a biblioteca Tkinter para realizar operações CRUD (Create, Read, Update, Delete) em registros de uma tabela específica do banco de dados.

## Pré-requisitos

- Python instalado em sua máquina (recomendado Python 3.x).
- Biblioteca MySQL Connector instalada. Caso não tenha a biblioteca instalada, você pode instalá-la usando o gerenciador de pacotes pip:

```python
pip install mysql-connector-python
```

## Configuração

Antes de executar o programa, é necessário configurar as informações de acesso ao banco de dados MySQL. Edite as seguintes linhas no código para refletir as configurações do seu ambiente:

```python
connection = mysql.connector.connect(
    host="localhost",  # Endereço do seu banco de dados
    user="root",       # Usuário do banco de dados
    password="Password", # Senha do banco de dados
    database="bd_client" # Nome da base de dados
)
```

## Funcionalidades do Gerenciador de Registros
O programa oferece as seguintes funcionalidades através de sua interface gráfica:

1. Criar Novo Registro: Preencha os campos de "Nome", "Email" e "Telefone" e clique no botão "Criar" para adicionar um novo registro ao banco de dados.

2. Atualizar Registro: Selecione um registro na lista exibida na interface. Em seguida, atualize os campos de "Nome", "Email" e/ou "Telefone" e clique no botão "Atualizar" para salvar as alterações no registro selecionado.

3. Excluir Registro: Selecione um registro na lista exibida na interface e clique no botão "Excluir" para remover o registro do banco de dados.

4. Listar Registros: A lista exibida na interface mostra os registros presentes na tabela do banco de dados. Ela é atualizada automaticamente após cada operação de criação, atualização ou exclusão.

## Executando o Programa
1. Certifique-se de que o banco de dados MySQL esteja configurado e em execução.
2. Execute o código Python utilizando o terminal ou prompt de comando:
```python
python main.py
```
A interface do programa será aberta e você poderá começar a gerenciar os registros do banco de dados através dela.

## Personalização
Este projeto pode ser personalizado de acordo com suas necessidades. Você pode modificar a interface gráfica, adicionar mais funcionalidades, criar novas tabelas no banco de dados e muito mais.

## Créditos
Este projeto foi desenvolvido com base em conhecimentos adquiridos em cursos e tutoriais da Data Science Academy.

## Licença
Este projeto está licenciado sob a Licença MIT.

Divirta-se gerenciando seus registros com o Gerenciador de Registros em Python e MySQL! Sinta-se à vontade para aprimorá-lo e adequá-lo às suas necessidades. Se tiver alguma dúvida ou sugestão, fique à vontade para entrar em contato! 🗂️📝
