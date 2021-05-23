**INTELIGÊNCIA ARTIFICIAL BUSCAS**

**Descrição:**

O trabalho consiste em implementar um sistema de navegação automática de um robô utilizando os algoritmos de **busca cega de custo uniforme** e **busca com informação A\***. O robô deve ser capaz de calcular automaticamente a rota para chegar a qualquer ponto de um ambiente representado através de uma matriz *n* x *n*.

O ambiente por onde o robô vai navegar é formado por diversos tipos de terrenos e em cada tipo de terreno o robô tem um grau de dificuldade diferente para andar. A Figura 1 mostra o ambiente a ser explorado pelo robô. Por exemplo, o robô consegue passar facilmente por um terreno sólido e plano, porém terá dificuldades para andar em um terreno montanhoso ou em um pântano.

Os tipos de terrenos que compõem o ambiente são (ver cores na Figura 1):

- Sólido e plano (verde) – Custo: 1
- Montanhoso (marrom) – Custo: 5
- Pântano (azul) – Custo: 10
- Fogo (vermelho) – Custo: 15

![](Aspose.Words.a8f34589-b18f-4cc8-b21c-f2289db7257d.001.png)

Figura 1: Ambiente a ser explorado pelo robô. Cores: verde – terreno sólido e plano; azul

– pântano; marrom – montanhoso; vermelho – fogo.

**Informações Adicionais:**

- O robô pode andar somente na vertical e na horizontal;
- Para o algoritmo A\*, utilize como heurística a distância Manhattan entre a localização atual e a localização destino.
- O ambiente deve ser representado por uma matriz 42 x 42 (igual mostrado na Figura 1);
- O sistema deve permitir que o ambiente seja configurável (por arquivo de entrada);
- A posição inicial do robô e do seu destino devem ser configuráveis (por arquivo de entrada);
- Durante o procedimento de busca, deve ser mostrado no ambiente (ou em um ambiente auxiliar) os nós que já foram visitados e os nós que estão na fronteira de visitação;
- Após calcular a rota (caminho da posição inicial do robô até posição de destino), o programa deve mostrar quantos nós foram **visitados** pelo algoritmo de busca, ou seja, quantos nós foram abertos na árvore de busca;
- O programa deve exibir o custo do caminho percorrido pelo agente ao terminar a execução;
- Após calcular a rota (caminho da posição inicial do robô até posição de destino), o programa deve mostrar a movimentação do robô seguindo a rota calculada (mostrar caminho encontrado origem-destino);
- O programa pode ser desenvolvido em qualquer linguagem de programação;
- O trabalho pode ser realizado em grupos de no máximo 2 pessoas;

**Forma de avaliação:**

Será avaliado se:

- O trabalho atendeu a todos os requisitos especificados anteriormente;
- Os algoritmos foram implementados e aplicados de forma correta;
- O código foi devidamente organizado;
- O sistema apresenta interface gráfica com o mapa.
- O trabalho foi apresentado corretamente em sala de aula. O programa deve ser apresentado durante a aula.

**Cronograma:**

- Cada dupla deve escolher um nome, que seja representativo para a área de Inteligência Artificial até dia 09/04. Esse nome deve ser postado e justificado em uma tarefa disponível no Canvas
- Cada dupla deverá apresentar o projeto para a turma (projeto em execução)
- Cada dupla deverá votar em dois projetos de que tenha gostado mais. Não pode votar em si mesmo (O projeto mais votado valerá 1 ponto a mais no projeto).

**Data de entrega:**

04/05/2021. (Apresentação em sala)

**Importante:**

Trabalhos entregues após a data limite valem um (1.0) ponto a menos para cada dia de atraso, com limite de 3 dias.
