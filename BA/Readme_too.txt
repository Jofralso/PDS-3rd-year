O que é um filtro Butterworth?

Um filtro Butterworth é usado para deixar passar certas frequências e bloquear outras. Pode ser útil em situações como limpar ruídos de áudios ou separar diferentes partes de um sinal.

Porque usamos o filtro Butterworth?

O filtro Butterworth é escolhido porque mantém o sinal o mais plano possível na faixa de frequências que desejamos manter, sem causar oscilações ou distorções indesejadas.
Então, usamos o filtro Butterworth para melhorar a qualidade do nosso sinal, removendo interferências e mantendo apenas as partes importantes.

Como funciona?

O filtro Butterworth funciona ajustando o quanto ele deixa passar ou reduz em diferentes frequências. Ele faz isso suavemente, sem causar distorções significativas no sinal.

Ordem do Filtro: A ordem do filtro determina o quão rápido ele começa a reduzir as frequências além daquelas que desejamos manter. Ordens mais altas significam uma redução mais rápida, mas podem introduzir atrasos.

Frequência de Corte: A frequência de corte é o ponto onde o filtro começa a agir. Frequências abaixo desse ponto são menos afetadas, enquanto frequências acima são reduzidas.


Como usar o filtro Butterworth em Python?

Em Python, usamos as bibliotecas como scipy.signal, mais especificamente, butter e lfilter, para aplicar o filtro. Definimos a ordem do filtro e a frequência de corte desejada, e o filtro faz o trabalho de processar o sinal.

b, a = butter(order, [low, high], btype=filter_type, analog=False)

A função butter calcula b e a, que são os coeficientes do numerador e denominador da equação diferencial do filtro. 

O lfilter faz a relação entre o sinal de entrada x(n), o de saída y(n) e os coeficientes.
