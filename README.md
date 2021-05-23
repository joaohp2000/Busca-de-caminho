**INTELIGÊNCIA ARTIFICIAL BUSCAS**

**Descrição:**

O trabalho consiste em implementar um sistema de navegação automática de um robô utilizando os algoritmos de **busca cega de custo uniforme** e **busca com informação A\***. O robô calcula automaticamente a rota para chegar a qualquer ponto de um ambiente representado através de uma matriz *n* x *n*.

O ambiente por onde o robô vai navegar é formado por diversos tipos de terrenos e em cada tipo de terreno o robô tem um grau de dificuldade diferente para andar. A Figura 1 mostra o ambiente a ser explorado pelo robô. Por exemplo, o robô consegue passar facilmente por um terreno sólido e plano, porém terá dificuldades para andar em um terreno montanhoso ou em um pântano.

Os tipos de terrenos que compõem o ambiente são (ver cores na Figura 1):

- Sólido e plano (verde) – Custo: 1
- Montanhoso (marrom) – Custo: 5
- Pântano (azul) – Custo: 10
- Fogo (vermelho) – Custo: 15

![](Aspose.Words.a8f34589-b18f-4cc8-b21c-f2289db7257d.001.png)

Figura 1: Ambiente a ser explorado pelo robô. Cores: verde – terreno sólido e plano; azul

– pântano; marrom – montanhoso; vermelho – fogo.

**Informações Sobre o Projeto:**

- O robô anda somente na vertical e na horizontal;
- O algoritmo A\*, utiliza como heurística a distância Manhattan entre a localização atual e a localização destino.
- O ambiente é configuravél por arquivo de entrada, tanto o mapa quanto a posição inicial e de destino;




