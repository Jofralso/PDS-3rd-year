# Modificador de Voz

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um Modificador de Voz, uma aplicação que permitirá alterar características da voz, tais como tom (grave e agudo), velocidade de fala, e até mesmo alterar a voz baseado no gênero sexual selecionado. A aplicação será uma ferramenta versátil e intuitiva para manipulação de áudio, proporcionando uma experiência única aos utilizadores.

## Colaboradores

- **Diogo Oliveira:**

- **Guilherme Castro:**

## Funcionalidades Principais

1. **Alteração de Tom (Grave e Agudo):**
   - A aplicação permitirá aos utilizadores modificar o tom da voz, proporcionando a capacidade de ajustar entre um registro grave e agudo. Isso possibilitará a personalização da voz conforme a preferência do utilizador.

2. **Modificação de Velocidade de Voz:**
   - Os utilizadores terão controle total sobre a velocidade da fala, permitindo acelerar ou desacelerar a reprodução do áudio. Essa funcionalidade pode ser útil para diversas finalidades, como reprodução mais rápida para transcrições ou mais lenta para compreensão detalhada.

3. **Alteração da Voz pelo Género:**
   - A aplicação será capaz de alterar a voz do áudio com base no gênero sexual selecionado. Essa funcionalidade pode ser útil para diversos contextos, desde brincadeiras divertidas até aplicações mais sérias.

## Instruções de Uso

1. Abra a aplicação e escolha o ficheiro de áudio desejado.
2. Utilize as opções de controle para ajustar o tom, a velocidade e/ou alterar o gênero conforme suas preferências.
3. Pré-Visualize ou salve o áudio modificado.

## Bibliotecas 

O nosso programa recorre a várias bibliotecas para chegar ao seu estado final, foram necessárias para desenvolver a interface gráfica do programa, para a manipulação e reprodução de áudios, importação e exportação de áudios. A seguir poderá observar as bibliotecas utilizadas e uma breve explicação sobre elas.

1. **Tkinter:**
   - Utilizamos esta biblioteca para criar a interface gráfica (GUI) do nosso programa, onde possibilitou-nos criar sliders para alterar o valor dos parâmetros como a velocidade, tom, tamanho da janela e sobreposição entre valores anteriormente definidos, também criamos botões para procurar o ficheiro de áudio, pré-visualizar o áudio modificado e guardar áudio, por fim utilizamos para mostrar as mensagens de erro. 

2. **Pydub:**
   - Esta biblioteca foi utilizada para a manipulação de áudios, incluindo o carregamento, processamento e exportação de ficheiros de áudio.

3. **Numpy:**
   - Utilizamos esta biblioteca para realizar operações numéricas eficientes sobre as amostras de áudio, utilizado nas funções de alteração de áudio como, funções de alterar tom e velocidade do áudio e na função stretch.

4. **OS:**
   - Esta biblioteca fornece uma interface para interagir com o sistema operativo, na prática precisamos de implementar esta biblioteca para a opção de pré-visualizar o áudio, onde criamos um ficheiro temporário e depois remover o ficheiro com a função “os.remove()”.

5. **Pydub.playback:**
   - Esta biblioteca basicamente server para reproduzir o áudio escolhido e modificado pelo utilizador ao clicar no botão “Pré-visualizar”, isto com a função “play(audio)”.

## Funções

Este programa é constituído por várias funções, nelas estão implementadas as alterações do áudio face as opções que o utilizador selecionar, como funções para alterar a velocidade e o tom, manipulação e reprodução de áudio, importação e exportação de áudio. A seguir é explicado como funciona cada uma das funções do nosso programa.

**alterar_audio:**
   -   audio = AudioSegment.from_file(input_path): Esta linha usa a classe Pydub AudioSegmentpara carregar um ficheiro de áudio do ficheiro input_path.
   -   sound_array = np.array(audio.get_array_of_samples()): Os dados de áudio são convertidos em um array NumPy usando o get_array_of_samplesmétodo. Esta matriz representa a onda sonora.
   -   pitch_and_speed_shifted_array = pitchshift(sound_array, pitch_factor, speed_factor, window_size, overlap): A pitchshiftfunção é chamada com a matriz de som e parâmetros de afinação, velocidade, tamanho da janela e sobreposição especificados. Esta função aplica mudança de tom e mudança de velocidade ao conjunto de áudio.
   -   pitch_and_speed_shifted_audio = audio._spawn(pitch_and_speed_shifted_array.astype(np.int16)): Um novo AudioSegment é criado a partir do array NumPy modificado. O _spawnmétodo é usado para criar um novo segmento.
   -   pitch_and_speed_shifted_audio.export(output_path, format="wav"): O áudio modificado é exportado para o output_pathformato WAV especificado usando o exportmétodo.
   -   print("Áudio criado com sucesso"): uma mensagem de sucesso é impressa indicando que o áudio foi criado com sucesso.
   Esta função alterar_audio é a principal responsável por carregar um fiheiro de áudio, aplicar mudança de tom e mudança de velocidade, criar um novo segmento de áudio modificado e exportar o resultado para um caminho de saída especificado.


**pitchshift:**
   -   snd_array: A matriz de áudio de entrada (matriz NumPy) que representa a onda sonora.
n: O fator de afinação, indica o número de semitons para mudar a afinação. Os valores positivos aumentam o tom e valores negativos diminuem o tom.
speed_factor: Um fator para ajustar a velocidade do áudio.
window_size: O tamanho da janela de análise usada para processar o áudio.
overlap: A quantidade de sobreposição entre janelas de análise consecutivas.
   -   factor = 2**(1.0 * n / 12.0): Calcula o fator de mudança de afinação com base no fator de afinação especificado ( n). A fórmula converte o fator de altura de semitons em um fator multiplicativo usando a fórmula para proporções de frequência na teoria musical.
   -   stretched = stretch(snd_array, 1.0 / (factor * speed_factor), window_size, overlap): chama a stretchfunção para ampliar a matriz de áudio de entrada. Isso envolve a manipulação do algoritmo do vocoder de fase para modificar a duração do áudio, preservando seu tom.
   -   return speedx(stretched[window_size:], factor): ajusta ainda mais a velocidade do áudio esticado usando a speedxfunção. A stretched[window_size:]peça é utilizada para descartar as amostras iniciais, que podem ser afetadas por artefatos durante o alongamento.
   A função combina operações de mudança de tom e mudança de velocidade para modificar a matriz de áudio de entrada com base no fator de tom, fator de velocidade, tamanho da janela e sobreposição especificados. Ele utiliza a stretchfunção de alongamento do tempo e a speedxfunção de ajuste de velocidade.


**stretch:**
   -   sound_array: A matriz de áudio de entrada (matriz NumPy) que representa a onda sonora.
f: O fator de estiramento, determinando quanto esticar ou comprimir o áudio no tempo.
window_size: O tamanho da janela de análise usada para processar o áudio.
overlap: A quantidade de sobreposição entre janelas de análise consecutivas.
   -   phase = np.zeros(window_size): inicializa um array para armazenar as informações da fase.
hanning_window = np.hanning(window_size): Cria uma janela Hanning do tamanho especificado para análise.
   -   Itera sobre a matriz de áudio de entrada com um tamanho de passo determinado pelo fator de estiramento e sobreposição. Extrai segmentos sobrepostos ( a1 e a2) da matriz de áudio de entrada. Aplica uma janela Hanning a cada segmento. Calcula a FFT (Fast Fourier Transform) dos segmentos em janela ( s1 e s2). Calcula a diferença de fase entre segmentos consecutivos e atualiza a matriz de fases.
   -   Aplica as informações de fase para alterar a fase do segundo segmento ( a2_rephased). Acumula o segmento reformulado na matriz de resultados, ajustando a janela e a sobreposição.
   -   Normaliza a matriz de resultados para garantir que o áudio permaneça dentro de um intervalo de amplitude especificado.
   -   Converte a matriz de resultados em formato inteiro de 16 bits ( int16) para compatibilidade com formatos de arquivo de áudio.
   -   Retorna o áudio estendido no tempo como uma matriz NumPy em formato inteiro de 16 bits.
   A função implementa o algoritmo de codificador de fase para áudio com alongamento de tempo. Envolve transformada de Fourier, manipulação de fase e acumulação de segmentos refasados ​​para alcançar o efeito de alongamento de tempo desejado.


**speedx:**
   -   sound_array: A matriz de áudio de entrada (matriz NumPy) que representa a onda sonora.
factor: O fator de velocidade, determinando quanto acelerar ou desacelerar o áudio.
   -   np.arange(0, len(sound_array), factor): gera uma matriz de índices percorrendo a matriz de áudio original com um tamanho de passo determinado pelo fator de velocidade.
np.round(...): arredonda os índices para o número inteiro mais próximo, pois os índices do array devem ser números inteiros.
indices[indices < len(sound_array)].astype(int): filtra os índices que excedem o comprimento da matriz original e converte os índices restantes em números inteiros.
   -   sound_array[indices.astype(int)]: usa os índices calculados para selecionar um subconjunto de amostras da matriz de áudio original. Esta operação efetivamente faz uma nova amostragem do áudio em uma taxa diferente com base no fator de velocidade.
   -   Retorna a matriz de áudio reamostrada.
   A função é um método simples, mas eficaz, para alterar a velocidade de reprodução de um array de áudio. Isso é conseguido selecionando um subconjunto de amostras da matriz original em intervalos determinados pelo fator de velocidade.


**open_file:**
   -   filedialog.askopenfilename(): abre uma caixa de diálogo que permite ao utilizador escolher um ficheiro. Esta função retorna o caminho do fiheiro selecionado.
   -   entry_file_path.delete(0, tk.END): limpa o conteúdo do entry_file_pathwidget, que normalmente é um Entrywidget Tkinter usado para exibir o caminho do ficheiro selecionado.
entry_file_path.insert(0, file_path): insere o caminho do ficheiro selecionado no entry_file_pathwidget na posição 0.
   A função fornece uma maneira para o usuário escolher um ficheiro de áudio abrindo uma caixa de diálogo. Depois que um ficheiro é selecionado, ele atualiza um Entrywidget Tkinter com o caminho do ficheiro selecionado, tornando-o visível para o utilizador na GUI.


**process_audio:**
   -   filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Arquivos WAV", "*.wav")]): abre uma caixa de diálogo para salvar o áudio processado. Ele solicita que o utilizador escolha um nome do fiheiro e o local com extensão padrão ".wav".
   -   input_path = entry_file_path.get(): recupera o caminho do fiheiro de entrada do Entrywidget Tkinter chamado entry_file_path, que normalmente exibe o caminho do ficheiro de áudio selecionado.
pitch_factor = float(entry_pitch.get()): recupera o fator de pitch do Scalewidget Tkinter chamado entry_pitch.
speed_factor = float(entry_speed.get()): recupera o fator de velocidade do Scalewidget Tkinter chamado entry_speed.
window_size_exp = int(entry_window_size_scale.get()): recupera o expoente do tamanho da janela do Scalewidget Tkinter chamado entry_window_size_scale.
overlap_exp = int(entry_overlap_scale.get()): recupera o expoente de sobreposição do Scalewidget Tkinter chamado entry_overlap_scale.
speed_slider_value = float(entry_speed.get()): recupera o fator de velocidade do Scalewidget Tkinter chamado entry_speed.
   -   window_size = 2**window_size_exp: calcula o tamanho da janela com base no expoente recuperado da GUI.
overlap = 2**overlap_exp: calcula a sobreposição com base no expoente recuperado da GUI.
   -   alterar_audio(input_path, output_path, pitch_factor, speed_factor * speed_slider_value, window_size, overlap): chama a alterar_audiofunção com os parâmetros de entrada especificados. Ele realiza a modificação do áudio com base nas escolhas do usuário.
   -   except FileNotFoundError:: captura uma FileNotFoundErrorexceção que pode ocorrer se o ficheiro de entrada especificado não for encontrado. Nesse caso, ele chama a errorIOfunção para tratar o erro.
   A função orquestra o processamento de áudio coletando parâmetros de entrada da GUI, calculando o tamanho e a sobreposição da janela e, em seguida, invocando a alterar_audiofunção com esses parâmetros. Ele também lida com possíveis erros relacionados a ficheiros usando a FileNotFoundErrorexceção.


**preview_audio:**
   -   input_path = entry_file_path.get(): recupera o caminho do ficheiro de entrada do Entrywidget Tkinter chamado entry_file_path.
output_path = "temp.wav": especifica um caminho de saída temporário para o áudio modificado.
   -   Semelhante à process_audiofunção, esta parte recupera fator de pitch, fator de velocidade, tamanho da janela, sobreposição e valor do controle deslizante de velocidade da GUI.
   -   window_size = 2**window_size_exp: calcula o tamanho da janela com base no expoente recuperado da GUI.
overlap = 2**overlap_exp: calcula a sobreposição com base no expoente recuperado da GUI.
   -   alterar_audio(input_path, output_path, pitch_factor, speed_factor * speed_slider_value, window_size, overlap): chama a alterar_audiofunção com os parâmetros de entrada especificados. Modifica o áudio e o salva em um arquivo temporário ( temp.wav).
   -   audio = AudioSegment.from_file(output_path): Carrega o áudio modificado do ficheiro temporário usando o Pydub AudioSegment.
play(audio): Usa a função do Pydub playpara reproduzir o áudio modificado.
   -   os.remove(output_path): Remove o ficheiro temporário criado durante a visualização. Esta etapa é necessária para limpar ficheiros temporários.
   -   except FileNotFoundError:: captura uma FileNotFoundErrorexceção que pode ocorrer se o ficheiro de entrada especificado não for encontrado ou se houver problemas com o caminho do ficheiro. Nesse caso, ele chama a errorIOfunção para tratar o erro.
   A função permite aos utilizadores visualizar o áudio modificado reproduzindo-o na GUI. Ele usa um ficheiro temporário para armazenar o áudio modificado e remove o ficheiro temporário após a visualização. Quaisquer erros potenciais são capturados e tratados usando a FileNotFoundErrorexceção.


**errorIO:**
   -   input_path = entry_file_path.get(): recupera o caminho do ficheiro de entrada do Entrywidget Tkinter chamado entry_file_path. Este é o caminho que causou um erro relacionado à  entrada/saída (E/S).
   -   if not input_path:: verifica se o caminho de entrada é uma string vazia. Esta condição é verdadeira quando o utilizador não selecionou nenhum caminho de ficheiro.
   -   messagebox.showerror("Erro", "Introduza um caminho de ficheiro de áudio existente."): se o caminho de entrada estiver vazio, uma caixa de mensagem será exibida com uma mensagem de erro solicitando que o utilizador insira um caminho de ficheiro de áudio válido.
messagebox.showerror("Erro", "Caminho introduzido não existe no seu computador."): Se o caminho de entrada não estiver vazio, mas o ficheiro especificado não for encontrado, outra caixa de mensagem será exibida com uma mensagem de erro indicando que o caminho inserido não existe no computador.
   A função é um mecanismo simples de tratamento de erros para problemas relacionados a E/S na GUI. Ele verifica se o caminho de entrada está vazio e exibe uma caixa de diálogo de mensagem de erro apropriada.
