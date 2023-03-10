# smiling-foxes_hole-lotta-worms
Exercício em Álgebra Linear e utilização de vetores. O jogo tem como objetivo um alvo (a espaçonave) que deve ser atingido pelo projétil que é lançado pelo jogador. Utilizando uma fórmula física que descreve o processo de atração gravitacional dos corpos, além de operações matemáticas que utilizam contas com vetores (matrizes), foi possível a criação de um jogo onde os projéteis são afetados pelos campos gravitacionais do planeta presente na tela. 

Para jogar, basta clonar o repositório do github e rodar o arquivo Main.py. Se houver algum erro com as bibliotecas, certifique-se que você possui as bibliotecas necessárias (dentro do requirements.txt). Para intalá-las, é necessário rodar o comando: "". A tela de início lhe mostra o título do jogo e dois botões, o botão de jogar inicia o jogo, o de quit interrompe o código e cessa o programa. 

Ao clicar jogar, você será levado a uma nova tela, com um fundo espacial. Para atirar, basta selecionar a força com a qual quer lançar o projétil (clicando na barra no seletor superior, também chamado de HEADER) e clicar na tela principal (o que não é contemplado pelo HEADER). O ponto de lançamento é uma bolinha branca no canto inferior esquerdo da tela. Dentro do HEADER também é possível ver o nível atual, a pontuação do jogador e o número de tentativas restantes (possíveis de serem disparadas). Na verdade, os projéteis disparados são pequenos astronautas, por isso a escolha da nave como alvo (voltando para um local seguro). É possível observar que o astronauta disparada vai em direção ao cursor, então, o utilize na hora de mirar.

Cada projpetil possui dois vetores, um referente à velocidade (que é influenciado pelos campos gravitacionais) e outro à posição (que é influenciado pela velocidade). Com eles, é possível simular essa atração natural dos corpos na tela, mostrando o trajeto do projétil, criando um jogo divertido. Isso é possível graças ao nosso uso da fórmula da atração de corpos: A cada iteração, para cada partícula, recalcule a aceleração devida à gravidade. Lembre-se que a aceleração gravitacional é um vetor com módulo |a| = c/d**2, onde "c" é uma constante e "d" é a distância entre os dois corpos. A aceleração gravitacional aplicada sobre cada partícula sempre aponta para o corpo celeste para onde a partícula está sendo atraída. Uma maneira de pensar sobre essa fórmula é vermos a magnitude de "a" vezes a direção de "a", assim, conseguindo um vetor que é somado ao vetor "v" de cada objeto e influenciando o trajeto deles na tela. 

Sobre os obstáculos. O planeta influencia a trajetória do projétil que foi disparado, e quanto mais próximo dele maior é a força de atração exercida. A(s) lixeira(s) é(são) uma representação humorística de lixo-espacial, assim, quando seu projétil atinge (um)a lixeira, ele é eliminado (jogado no lixo). A nave é o alvo a ser atingido, pense como se você estivesse voltando a nave. 

Nosso jogo é gerado automaticamente cada vez que o jogador completa uma fase. O planeta muda de posição, assim como o objetivo a ser atingido e o(s) obstáculo(s) na tela. Digo isso pois, a cada 5 níveis que são conquistados, um novo obstáculo aparece na tela (+1), dificultando mais ainda o gameplay. Essa geração automática tem certos limites impostos por nós, que basicamente se resumem à qualquer lugar que não esteja dentro de um perímetro do lançador. 

O jogador possui um número de tentativas. O número inicial de tentativas é 10, mas quando o jogador termina uma fase ele ganha mais 2 tentativas. A pontuação, diferente dessa recompensa, é escalar. O número de pontos do jogador é multiplicado pelo nível atingido dividido por 10 (pontuação *= 1+(fase/10)).

O jogo apenas termina quando todas as tentativas disponíveis foram gastas e não há mais nenhum projétil em jogo (presente na tela). 

Quando o jogador utilizar todas as suas tentativas, seré levado à tela de início, onde a sua pontuação será exibida no local do título do jogo, assim como uma dica também aparecerá abaixo do botão de quit. Esse dica pode ser mudada por meio do botão "nova dica", mas elas não são exatamente úteis para o jogo, são mais como conselhos de vida eu diria. 

Isso é tudo, aproveite nosso jogo (especialmente as dicas).

https://user-images.githubusercontent.com/80931256/221445118-c054cd79-da78-48ff-81ca-51d5b9fab483.mov

