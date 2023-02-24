# smiling-foxes_hole-lotta-worms
Angry Birds inspired game, an exercise in linear algebra

Exercício em Álgebra Linear e utilização de vetores. O jogo tem como objetivo um alvo (o retângulo verde) que deve ser atingido pelo projétil que é lançado pelo jogador. Utilizando uma fórmula física que descreve o processo de atração gravitacional dos corpos, além de operações matemáticas que utilizam contas com vetores (matrizes), foi possível a criação de um jogo onde os projéteis são afetados pelos campos gravitacionais do planeta presente na tela. 

Cada projpetil possui dois vetores, um referente à velocidade (que é influenciado pelos campos gravitacionais) e outro à posição (que é influenciado pela velocidade). Com eles, é possível simular essa atração natural dos corpos na tela, mostrando o trajeto do projétil, criando um jogo divertido.

Para jogar, basta rodar o arquivo Main.py. Se houver algum erro com as bibliotecas, certifique-se que você possui as bibliotecas necessárias (dentro do requirements.txt). A tela de início lhe mostra o título do jogo e dois botões, o botão de jogar inicia o jogo, o de quit interrompe o código e cessa o programa. 

Ao clicar jogar, você será levado a uma nova tela, com um fundo espacial. Para atirar, basta selecionar a força com a qual quer lançar o projétil (clicando na barra no seletor superior, também chamado de HEADER) e clicar na tela principal (o que não é contemplado pelo HEADER). Dentro dele também é possível ver o nível atual, a pontuação do jogador e o número de bolinhas restantes (possíveis de serem disparadas). É possível observar que a bolinha disparada vai em direção ao cursor, então, o utilize na hora de mirar. Você possui 15 bolinhas no início do jogo, e ganha mais 15 a cada 10 níveis que são completos.

Sobre os obstáculos. O planeta influencia a trajetória do projétil que foi disparado. A(s) lixeira(s) é(são) uma representação humorística de lixo-espacial, assim, quando seu projétil atinge (um)a lixeira, ele é eliminado (jogado no lixo). O quadrado verde é o alvo a ser atingido, escolhemos esse formato pela sua praticidade, e sua cor pelo fato de chamativa. 

Nosso jogo é gerado automaticamente cada vez que o jogador completa uma fase. O planeta muda de posição, assim como o objetivo a ser atingido e o(s) obstáculo(s) na tela. Digo isso pois, a cada 5 níveis que são conquistados, um novo obstáculo aparece na tela, dificultando mais ainda o gameplay. Essa geração automática tem certos limites, que basicamente se limitam a qualque lugar que não esteja dentro de um perímetro do lançador. 

O jogador possui um número de bolinhas que ele pode disparar. O número inicial de bolinhas é 10, mas quando o jogador termina uma fase ele ganha mais 2 bolinhas para o seu arsenal. A pontuação, diferente dessa recompensa, é escalar. O número de pontos do jogador é multiplicado pelo nível atingido dividido por 10 (pontuação *= 1+(fase/10)).

O jogo apenas termina quando todas as bolinhas disponíveis foram utilizadas e não há mais nenhuma em jogo (presente na tela). 