# Python com Banco de Dados

- Os arquivos estão em https://github.com/abispo/shared-files/tree/main/modulo02. Utilize a biblioteca `requests` para baixá-los.

### Desafio 1

Ler o arquivo `cursos.csv` e salvar os dados na tabela `tb_cursos`. Essa tabela deve ter a seguinte estrutura.

```
id              INT         PRIMARY KEY AUTO_INCREMENT
curso           VARCHAR     NOT NULL
carga_horaria   INT         NOT NULL
preco           FLOAT       NOT NULL
```

Após os dados terem sido salvos, vamos criar uma nova tabela chamada `tb_estatisticas_cursos`, que terá as seguintes colunas:

```
qtd_cursos                  INT
curso_maior_carga_horaria:  VARCHAR
curso_com_maior_valor:      VARCHAR

Após salvar, mostrar esses dados na tela. Exemplo:

Quantidade de cursos: 10
Curso com a maior carga horária: Web Development com Django (50 horas)
Curso com o maior valor: Machine Learning Fundamentals (R$ 1200.00)

```

### Desafio 2

Ler o arquivo `notas.csv` e salvar as informações na tabela `tb_notas`. Essa tabela terá a seguinte estrutura:

```
id          INTEGER     PRIMARY KEY     AUTO_INCREMENT
nome        VARCHAR         NOT NULL
nota1       FLOAT           NOT NULL
nota2       FLOAT           NOT NULL
nota3       FLOAT           NOT NULL
nota4       FLOAT           NOT NULL
nota5       FLOAT           NOT NULL
```

Após os dados terem sido salvos, vamos criar uma tabela com estatísticas, chamada `tb_estatisticas_notas`. A tabela terá a seguinte estrutura:

```
quantidade_de_alunos        INT         NOT NULL
media_geral                 FLOAT       NOT NULL
maior_media                 FLOAT       NOT NULL
aluno_maior_media           VARCHAR     NOT NULL
```

Importante: A média de cada aluno será calculada excluindo a maior e a menor notas. Exemplo:

```
nome;n1;n2;n3;n4;n5
Maria;4;9;10;2;5
```

Nesse caso, a média da aluna Maria será calculada utilizando as 3 notas intermediárias, ou seja, [4, 5, 9]. A menor nota (2) e maior nota (10) são excluídas do cálculo, ou seja, a média de Maria será de 6.
