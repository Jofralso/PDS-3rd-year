# Afinador de Instrumentos Musicais

#### Alunos
Diogo Santos, Nº 24011

Ricardo Almeida, Nº 22746
#### Professor
João Francisco Almeida Soares

## Sumário

__Introdução__

__Requisitos Técnicos__

__Python__

__Bibliotecas utilizadas__

__Referências__

## Introdução
O Processamento Digital de sinais (PDS) consiste em utilizar computadores ou processadores de sinais digitais especializados, para realizar uma ampla variedade de operações de processamento de sinal. Os sinais digitais processados são uma sequência de números que representam amostras de uma variável contínua em um domínio como tempo, espaço ou frequência. Em eletrônica, um sinal digital é representado como um pulso, geralmente gerado pela comutação de um transístor. 

As aplicações de PDS incluem processamento de áudio, processamento de fala, processamento de imagem digital, compressão de dados, codificação de vídeo, codificação de áudio, engenharia biomédica e sismologia, entre outros.

Foi-nos proposto realizar um projeto que englobasse uma área de Processamento Digital de Sinais e assim decidimos criar uma aplicação que tem como função ser um afinador que se adapta ao instrumento musical escolhido pelo utilizador.

## Requisitos Técnicos
Python 3.7 ou superior.

Bibliotecas: tkinter, matplotlib, pyaudio, numpy, scipy e threading.

## Python
Para desenvolver a aplicação utilizamos a ferramenta IDLE do Python.

O Python é uma linguagem de programação de alto nível, interpretada, orientada a objetos e de propósito geral. Foi criada por Guido van Rossum e lançada em 1991. O Python é uma linguagem popular para desenvolvimento web, análise de dados, automação, inteligência artificial e outras aplicações. O Python é conhecido pela sua sintaxe clara e concisa, o que torna o código fácil de ler e escrever. Além disso, o Python tem uma grande comunidade de desenvolvedores que contribuem com bibliotecas e ferramentas para aprimorar a linguagem.

## Bibliotecas utilizadas

Para desenvolver a aplicação, utilizamos diversas bibliotecas que vamos agora descrever.

- __tkinter__: É uma biblioteca gráfica que permite criar interfaces gráficas para o utilizador (GUI's) em Python. É baseada no kit de ferramentas Tcl/Tk GUI e é a interface padrão do Python. Com o tkinter, é possivel criar janelas, botões, caixas de texto, menus, entre outros elementos da interface gráfica.

- __matplotlib.animation.FuncAnimation__: É uma classe da biblioteca matplotlib que permite criar animações em Python. É usada para criar animações de gráficos, como gráficos de linha, de barra, de dispersão, entre outros. A classe FuncAnimation permite criar animações com base em uma função que é chamada repetidamente em intervalos regulares.

- __matplotlib.pyplot__: É uma função da biblioteca matplotlib que fornece uma interface para criar gráficos em Python. É usada para criar gráficos de linha, de barra, de dispersão, entre outros. A biblioteca pyplot é baseada na biblioteca MATLAB e é muito útil para visualizar dados em Python.

- __pyaudio__: É uma biblioteca que fornece uma interface para trabalhar com áudio em Python. É usada para gravar e reproduzir áudio em tempo real. A biblioteca pyaudio é muito útil para criar aplicações que precisam trabalhar com áudio, como aplicações de gravação de voz, de reconhecimento de fala, entre outros.

- __numpy__: É uma biblioteca que fornece suporte para arrays e matrizes multidimensionais em Python. É usada para realizar operações matemáticas em arrays e matrizes, como adição, subtração, multiplicação, divisão, entre outras. A biblioteca numpy é muito útil para trabalhar com dados numéricos em Python.

- __scipy.signal.butter__: É uma função da biblioteca scipy.signal que é usada para projetar filtros digitais. É usada para criar filtros digitais que podem ser usados para filtrar sinais de áudio, sinais de vídeo, entre outros.

- __scipy.signal.lfilter__: É uma função da biblioteca scipy.signal que é usada para filtrar sinais digitais. É usada para aplicar um filtro digital a um sinal digital. A função lfilter é muito útil para filtrar sinais de áudio, sinais de vídeo, entre outros.

- __threading__: É uma biblioteca que fornece suporte para threads em Python. É usada para criar e gerir threads no Python. A biblioteca threading é muito útil para criar aplicações que precisam executar várias tarefas simultaneamente.

## Funcionamento

Vamos agora mostrar e descrever como funciona a aplicação, as respetivas bibliotecas usadas e as funçoes criadas.

O afinador através do som captado pelo microfone do dispositivo, calcula a frequencia e compara com uma lista de notas musicais e depois imprime no terminal a nota correspondente.

## Referências

https://github.com/Jofralso/PDS-3rd-year/blob/DR/DR%20-%20Afinador-Identi-Inst/README.md, consultado em 29/11/2023

https://elearning2324.estgl.ipv.pt/course/view.php?id=155, consultado em 29/11/2023

https://www.python.org/, consultado em 29/11/2023
