"""
Desafio Implementar um sistema de leitura e de alarme

1. Você deve implementar uma classe que representa um sensor de gás. A cada vez que esse sensor é lido, ele gera um valor. Esse valor é lido a partir do método ler(). Esse valor será um valor randômico entre 0 e 100. O valor inicial do sensor será de 0. Para gerar o valor randômico, utilize a função randint(a, b) do pacote random.

2. Você deve implementar uma classe que irá representar um alarme caso o valor máximo para o leitor de gás tenha sido atingido. A partir dessa classe, você irá criar 2 classes de alarme: AlarmeSonoro e AlarmeVisual. Essas classes devem implementar o método soar(). Gere um texto de alarme de acordo com a classe.

3. Você deve implementar uma classe que irá representar um circuito de leitura desse sensor, que também se comunica com os alarmes. Esse leitor irá consultar a cada segundo o sensor, ou seja, essa classe terá um método chamado checar, que irá fazer a checagem. Para fazer essa checagem a cada segundo, utilize a função sleep do módulo time. Caso o valor lido do sensor seja maior ou igual a 80, esse leitor irá chamar o método soar dos objetos de alarme. Mesmo com o alarme ligado, o leitor irá continuar a ler os dados do sensor. Caso esse valor lido do sensor seja menor que 80, os alarmes não serão mais soados

Lista de Bonus
BONUS: No primeiro item, o valor lido não pode estar fora da faixa entre +5 e menos -5. Exemplo. Se o valor lido anteriormente foi de 60, o novo valor do sensor deve ficar entre 55 e 65. O sensor não deve retornar números negativos, o número mais baixo é 0.
"""