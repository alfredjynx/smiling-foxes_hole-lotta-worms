# smiling-foxes_hole-lotta-worms
Angry Birds inspired game, an exercise in linear algebra

Exercício em Álgebra Linear e utilização de vetores. O jogo tem como objetivo um alvo (o retângulo verde) que deve ser atingido pelo projétil que é lançado pelo jogador. Utilizando uma fórmula física que descreve o processo de atração gravitacional dos corpos, além de operações matemáticas que utilizam contas com vetores (matrizes), foi possível a criação de um jogo onde os projéteis são afetados pelos campos gravitacionais dos planetas presentes na tela. 

Cada projpetil possui dois vetores, um referente à velocidade (que é influenciado pelos campos gravitacionais) e outro à posição (que é influenciado pela velocidade). Com eles, é possível simular essa atração natural dos corpos na tela, mostrando o trajeto do projétil, criando um jogo divertido.

Para jogar, basta selecionar a força com a qual quer lançar o projétil (clicando na barra no seletor superior, também chamado de HEADER) e clicar na tela principal, onde há um fundo com tema espacial e planetas e afins desenhados. É possível observar que a bolinhas disparada vai em direção ao cursor, então, o utilize na hora de mirar. Você possui 15 bolinhas no início do jogo, e ganha mais 15 a cada 10 níveis que são completos.

Sobre os obstáculos. Os planetas tem forças gravitacionais diferentes, um é mais fraco quando comparado ao outro, mas ambos influenciam a trajetória do projétil que foi disparado. A lixeira é uma representação humorística de lixo-espacial, assim, quando seu projétil atinge a lixeira, ele é eliminado (jogado no lixo). O quadrado verde é o alvo a ser atingido, escolhemos esse formato pela sua praticidade, e sua cor pelo fato de chamativa. 

Nosso jogo é gerado automaticamente cada vez que o jogador completa uma fase. Os dois planetas mudam de posição, assim como o objetivo a ser atingido e o(s) obstáculo(s) na tela. Digo isso pois, a cada 5 níveis que são conquistados, um novo obstáculo aparece na tela, dificultando mais ainda o gameplay. 

O jogo apenas termina quando todas as bolinhas disponíveis foram utilizadas e não há mais nenhuma em jogo (presente na tela). 