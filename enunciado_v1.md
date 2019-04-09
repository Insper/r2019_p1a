# Robótica Computacional

## Avaliação 1

Observações de avaliações nesta disciplina:
* É necessário ter pelo menos $50\%$ de nota nesta prova
* Quem não tiver nota mínima nesta prova pode fazer a *delta* versando sobre o mesmo conteúdo na semana das avaliações finais. A *delta* limita a nota aos $50\%$ mínimos necessários

Orientações gerais:
* Se você ficou no horário atribuído originalmente,  terá  um robô disponível com **somente uma carga de bateria**. Conte com apenas 20 minutos efetivos de funcionamento do robô ou 30-40 minutos de *standby*. Não deixe seu robô ligado sem necessidade
* Todas as questões podem ser feitas com robô real ou simulado
* Você pode consultar a *Internet* livremente, mas não pode se comunicar com outras pessoas da turma ou de fora dela sobre o conteúdo da prova. Tentativas de comunicação serão severamente punidas.
* Ao final da prova, compacte a pasta com todo o seu código e envie pelo Blackboard.
* A responsabilidade por ter o *setup* funcionando é de cada estudante
* Haverá uma planilha compartilhada com fila para dúvidas. Indique nela se seu problema é de **infra** ou **geral**

Existe algumas dicas de referência rápida de setup [instrucoes_setup.md](instrucoes_setup.md)


# Questões

## Questão 1

Trabalhe na pasta `p1_webcam`. Ali estão disponíveis os códigos fornecidos em aula para rodar `Darknet Yolo v.3`  e `MobileNet` . Se usar o Yolo **vai precisar baixar os pesos**

**O que é para fazer**

Escolha como base um dos dois reconhecedores de objetos e implemente um contador de quantas bicicletas foram vistas. A categoria para bicicleta é `bicycle`

É necessário que seu programa imprima o tempo todo a quantidade de bicicletas vistas até então.

**Não é necessário** eliminar redundância *frame* a *frame*, ou seja: se uma bicicleta contar num *frame*, ela **pode** ser contada novamente no frame seguinte.

Escreva aqui (neste markdown) em qual das duas versões trabalhou

### Rubrica questão 1

|Resultado| Conceito| 
|---|---|
| Não executa | 0 |
| Não consegue identificar ocorrências da categoria bicycle | 1.0 |
| Identifica, mas não conta direito nem dá output | 2.0 |
| Identifica e conta todas as ocorrências | 4.0 | 





## Questão 2

Trabalhe na pasta `p1_a_ros` e crie um script válido.

Faça o robô girar na direção do **objeto real mais próximo** detectado pelo laser. A idéia é que ao final o robô termine voltado para o objeto.

O resultado pode ser alcançado de forma *iterativa* - o robô pode fazer isso em loop. Não é preciso ter um controle de posição preciso que permita acertar na primeira tentativa.

Tome cuidado de levar em conta apenas valores válidos de leituras.


### Rubrica questão 2



|Resultado| Conceito| 
|---|---|
| Não executa | 0 |
| Não descobre qual o objeto mais próximo ou não filtra valores inválidos | 1.0 |
| Identifica o objeto mais próximo, mas não se posiciona corretamente | 2.0 |
| É capaz de se orientar na direção do objeto mais próximo | 4.0 | 




## Questão 3

**1.0 ponto**

Por que o projeto 1 é chamado de robótica comportamental?

O que o robô precisaria ter para ir além do nível comportamental?

Lembre-se de que **você pode pesquisar**.

**Responda aqui**

## Questão 4

**1.0 ponto**

Na atividade da `aula 03` você usou um rede neural (Yolo ou SSD para identificar categorias, mas em seguida mudou para tracking).

Qual a diferença entre *tracking* e *deteção*? 

Cite duas vantagens de usar *tracking*?

**Responda aqui**



