Criar a model `Comment`. Você deve utilizar o alembic para criar a estrutura da tabela.

1. Criar a model `Comment`, com os seguintes atributos:

```
    nome da tabela: comments

    id int autoincremento chave primaria
    post_id int not null chave estrangeira para postagens.id
    user_id int not null chave estrangeira para users.id
    text varchar(200) not null
```

2. Utilizando os comandos do alembic, gerar a migration
   `alembic revision --autogenerate --message "<mensagem>"`

3. Após isso, aplicar a migration
   `alembic upgrade head`

4. Alterar a model, adicionando o atributo `created_at`. Pode usar como base a model `User`

5. Gere a migration

6. Aplique a migration
