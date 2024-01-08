Processamento Digital de Sinal

Bruno Alves   19679
António Dias  22828


Filtro de sinal em tempo real 


Este programa após iniciar captura todo o som atraves do microfone do computador, aplica-lhe um filtro e reproduz o resultado com um ligeiro atraso.

Tem 4 tipos de filtro:
Passa-Alto
Passa-Baixo
Passa-Banda
Rejeita-Banda

É apresentado um menu com 4 opções:

1-Alterar frequência de corte, tendo cuidado para verificar se são necessárias duas ou só uma, conforme o tipo de filtro.

2-Alterar o tipo de filtro. (lowpass, highpass, bandpass, bandstop) 

3-Listar os dispositivos de entrada e saída de audio com os respetivos índices e mostrar quais os que estão a ser utilizados nesse momento.

4-Fechar o programa. Ao mesmo tempo grava 2 ficheiros de audio (.wav), um sem filtro e outro com o filtro aplicado.

Tudo isto é feito em tempo real, ou seja estamos constantemente a ouvir o que o microfone está a capturar e qualquer alteração ao filtro, seja frequência de corte ou tipo de filtro é notada imediatamente.


---------------------------------------------------------------------------------------------

###  butterworth_filter(data, lowcut, highcut, RATE, order, filter_type)

	Este método é invocado no thread de captação e gravação de audio.
	De cada vez que é capturado um bloco de dados este é guardado na lista frames, como audio não filtrado, e enviado para este método para ser filtrado e guardado na lista filtered_data.
-----------------------------------------------------------------------------------------

###  save_audio_before_filter(frames, filename='audio_before_filter.wav')
	
	Aqui tudo o que está guardado na lista frames é gravado num ficheiro de audio .wav
	Este audio é sem filtro, conforme capturado pelo microfone
---------------------------------------------------------------------------------------------------
###  save_audio_after_filter(filtered_frames, filename='audio_after_filter.wav')

	Aqui tudo o que está guardado na lista filtered_data é gravado num ficheiro de audio .wav
	Este audio é com o filtro e todas as alterações aplicadas
---------------------------------------------------------------------------------------------
###  record_audio(stream, frames)
	
	Método onde é capturado o audio do microfone, guardado e enviado para butterworth_filter para sel filtrado
------------------------------------------------------------------------------------------------
###  play_audio(stream, filtered_data):
	
	Este método reproduz o audio filtrado guardado na lista filtered_data
-------------------------------------------------------------------------------------------
###  p = pyaudio.PyAudio()
###  stream_in = p.open(format=pyaudio.paInt16,
###  stream_out = p.open(format=pyaudio.paInt16,

	Aqui são abertas as streams para se poder gravar e reproduzir audio
---------------------------------------------------------------------------------------------
###  record_thread = threading.Thread(target=record_audio, args=(stream_in, frames))
###  play_thread = threading.Thread(target=play_audio, args=(stream_out, filtered_data))
###  record_thread.start()
###  play_thread.start()

	Aqui são criados e iniciados os dois threads utilizados, associando os métodos e os argumentos
------------------------------------------------------------------------------------------------
###  text_menu()
	
	Método usado apenas para imprimir o menu principal
--------------------------------------------------------------------------------------------
###  option1()
###  option2()
###  option3()
###  option4()
###  option5()

	Métodos usados no menu, onde são alteradas as frequências, o tipo de filtro, a ordem do filtro, listados os dispositivos de entrada e saida de audio e é feito o fecho do programa.
---------------------------------------------------------------------------------------------
###  corte1()
###  corte2()

	Métodos complementares ao método option1() devido á necessidade de ter uma ou duas frequências de corte, conforme o tipo de filtro.
----------------------------------------------------------------------------------------------



















