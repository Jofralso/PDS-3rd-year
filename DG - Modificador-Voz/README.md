# Modificador de Voz

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um Modificador de Voz, uma aplicação que permitirá alterar características da voz, tais como tom (grave e agudo), velocidade de fala e também adicionar um ambiente sonoro ao áudio. A aplicação é uma ferramenta versátil e intuitiva para manipulação de áudio, proporcionando uma experiência única aos utilizadores.

## Colaboradores

- **Diogo Oliveira:**

- **Guilherme Castro:**

## Funcionalidades Principais

1. **Alteração de Tom (Grave e Agudo):**
   - A aplicação permitirá aos utilizadores modificar o tom da voz, proporcionando a capacidade de ajustar entre um registro grave e agudo. Isso possibilitará a personalização da voz conforme a preferência do utilizador.

2. **Modificação de Velocidade de Voz:**
   - Os utilizadores terão controle total sobre a velocidade da fala, permitindo acelerar ou desacelerar a reprodução do áudio. Essa funcionalidade pode ser útil para diversas finalidades, como reprodução mais rápida para transcrições ou mais lenta para compreensão detalhada.

3. **Implementação de Ambiente Sonoro:**
   - Os utilizadores serão capazes de adicionar um dos ambientes sonoros predefinidos no programa ao áudio selecionado. Esta funcionalidade pode ser útil para ambientar diversos contextos, desde brincadeiras até aplicações mais sérias.

## Instruções de Uso

1. Abra a aplicação e escolha o ficheiro de áudio desejado.
2. Utilize as opções de controlo para ajustar o tom, a velocidade e/ou adicionar ambiente sonoro conforme suas preferências.
3. Pré-Visualize ou salve o áudio modificado.

## Bibliotecas 

O nosso programa recorre a várias bibliotecas para chegar ao seu estado final, foram necessárias para desenvolver a interface gráfica do programa, para a manipulação e reprodução de áudios, importação e exportação de áudios. A seguir poderá observar as bibliotecas utilizadas e uma breve explicação sobre elas.

1. **Tkinter:**
   - Utilizamos esta biblioteca para criar a interface gráfica (GUI) do nosso programa, onde possibilitou-nos criar sliders para alterar o valor dos parâmetros como a velocidade, tom, tamanho da janela e sobreposição entre valores anteriormente definidos, também criamos botões para procurar o ficheiro de áudio, pré-visualizar o áudio modificado e guardar áudio, por fim utilizamos para mostrar as mensagens de erro. 

2. **Pydub:**
   - Esta biblioteca foi utilizada para a manipulação de áudios, incluindo o carregamento, processamento e exportação de ficheiros de áudio.

3. **Numpy:**
   - Utilizamos esta biblioteca para realizar operações numéricas eficientes sobre as amostras de áudio, utilizado nas funções de alteração de áudio como funções de alterar tom e velocidade do áudio e na função stretch.

4. **OS:**
   - Esta biblioteca fornece uma interface para interagir com o sistema operativo, na prática precisamos de implementar esta biblioteca para a opção de pré-visualizar o áudio, onde criamos um ficheiro temporário e depois remover o ficheiro com a função “os.remove()”.

5. **Pydub.playback:**
   - Esta biblioteca basicamente server para reproduzir o áudio escolhido e modificado pelo utilizador ao clicar no botão “Pré-visualizar”, isto com a função “play(audio)”.

## Funções

Este programa é constituído por várias funções, nelas são implementadas as alterações do áudio face as opções que o utilizador selecionar, como funções para alterar a velocidade e o tom, manipulação e reprodução de áudio, importação e exportação de áudio. A seguir é explicado como funciona cada uma das funções do nosso programa.

**alterar_audio:**

Esta função têm como função obter todos os parâmetros introduzidos pelo utilizador, desde caminho de entrada e saida do áudio, o valor de ajuste do tom, da velocidade, o tamanho da janela, a sobreposição e por fim o ambiente sonoro, depois realizar as alterações introduzidas pelo utilizado sobre o áudio original. Por fim cria um novo segmento de áudio modificado e faz a exportação para um caminho de sáida especificado.  

   -   **audio = AudioSegment.from_file(input_path):** Esta linha de código carrega o ficheiro de áudio guardado na variável input_path.
   -   **sound_array = np.array(audio.get_array_of_samples()):** Os dados do áudio são convertidos em um array NumPy com o método "get_array_of_samples()", onde guarda uma matriz de números que representa a onda sonora.
   -   **pitch_and_speed_shifted_array:** é nesta variável onde é armazenado todas as alterações sobre o áudio utilizando a função pitchshift(sound_array, pitch_factor, speed_factor, window_size, overlap), esta função aplica mudança de tom e mudança de velocidade ao conjunto de áudio.
   -   **pitch_and_speed_shifted_audio: = audio._spawn(pitch_and_speed_shifted_array.astype(np.int16)):** esta linha de código criar novo AudioSegment a partir do array NumPy modificado anteriormente, utilizando o método "_spawn()".
   -   **Condição ambiente:** É feita uma verificação com a variável ambiente, no caso de ser verdadeira, quer dizer que o utilizador escolheu um ambiente sonoro, logo é feito o ajusto do tamanho do áudio do ambiente para o áudio modifcado, realiza a sobreposição dos arrays de amostras do áudio modificado e do áudio ambiente e soma os arrays para criar um array combinado (mixed_array). 
   -   **pitch_and_speed_shifted_audio.export(output_path, format="wav"):** O áudio modificado é exportado para o caminho de sáida especificado no formato WAV ao utilizar o método export().


**pitchshift:**

A função pitchshift() é onde é realizado a alteração do tom entre grave e agudo do áudio introduzido pelo utilizador. A seguir poderá observar uma explicação mais detalhada acerca do funcionamento desta função. 

   -   **factor = 2^(1.0 * n / 12.0):** Calcula o fator de mudança de afinação do tom com base no fator de afinação especificado (n) pelo utilizador. A fórmula converte o fator de altura de semitons em um fator multiplicativo usando a fórmula para proporções de frequência na teoria musical.
   -   **stretched = stretch(snd_array, 1.0 / (factor * speed_factor), window_size, overlap):** chama a função stretch para ampliar a matriz de áudio de entrada. Isso envolve a manipulação do algoritmo para modificar a duração do áudio, preservando seu tom.
   -   **return speedx(stretched[window_size:], factor):** ajusta a velocidade do áudio esticado utilizando a função speedx() e o argumento "stretched[window_size:]" é utilizada para descartar as amostras iniciais, que podem ser afetadas durante o alongamento do áudio.

**stretch:**


A função stretch() realiza o alongamento do som introduzido pelo utilizador, onde primeiro divide o som em bits sobrepostos e reorganiza esses bits para que eles se sobreponham ainda mais (se quiser encurtar o som) ou menos (se quiser esticar o som), como nesta figura:

![stretchsound](https://github.com/Jofralso/PDS-3rd-year/assets/150937501/203fa7a2-0258-48ee-8b9e-bfd12de8eaad)

Esta função é implementada com os seguintes argumentos:
   -   **sound_array:** A matriz de áudio de entrada que representa a onda sonora.
   -   **f:** O fator de estiramento, determinando quanto esticar ou comprimir o áudio no tempo.
   -   **window_size:** O tamanho da janela de análise usada para processar o áudio.
   -   **overlap:** A quantidade de sobreposição entre janelas de análise consecutivas.

Dentro da função é executado várias operações como o algoritmo de codificador de fase para áudio com alongamento de tempo, envolve a transformada de Fourier, a manipulação de fase e acumulação de segmentos refasados ​​para alcançar o efeito de alongamento de tempo desejado.

   -   **phase = np.zeros(window_size):** inicializa um array para armazenar as informações da fase.
   -   **hanning_window = np.hanning(window_size):** Cria uma janela Hanning do tamanho especificado para análise, onde é usada para atenuar artefatos de borda no processo de estiramento temporal.

Por fim normaliza a matriz de resultados para garantir que o áudio permaneça dentro de um intervalo de amplitude especificado, converte a matriz de resultados em formato inteiro de 16 bits (int16) para compatibilidade com formatos de arquivo de áudio e retorna o áudio estendido no tempo como uma matriz NumPy.

**speedx:**

   A função speedx() é utilizado para alterar a velocidade de reprodução de um array de áudio, isso é conseguido ao selecionar um subconjunto de amostras da matriz original em intervalos determinados pelo fator de velocidade. Tem como principais parametros:
   
   -   **sound_array:** A matriz de áudio de entrada que representa a onda sonora.
   -   **factor:** O fator de velocidade, que determina o quanto acelerar ou desacelerar o áudio.

Depois são executados os passos seguintes: 

   -   **np.arange(0, len(sound_array), factor):** gera uma matriz de índices percorrendo a matriz de áudio original com um tamanho de passo determinado pelo fator de velocidade.
   -   **np.round(...):** arredonda os índices para o número inteiro mais próximo, pois os índices do array devem ser números inteiros.
   -   **sound_array[indices.astype(int)]:** usa os índices calculados para selecionar um subconjunto de amostras da matriz de áudio original. Faz uma nova amostragem do áudio em uma taxa diferente com base no fator de velocidade escolhido pelo utilizador e retorna a matriz de áudio modificado.

**open_file:**

Esta função é executada quando o utilizador clica no botão "procurar", fornece uma maneira de o utilizador escolher um ficheiro de áudio abrindo uma caixa de diálogo e depois que um ficheiro é selecionado, ele atualiza um Entrywidget Tkinter com o caminho do ficheiro selecionado, tornando-o visível para o utilizador na interface gráfica do programa.

   -   **filedialog.askopenfilename():** abre uma caixa de diálogo que permite ao utilizador escolher um ficheiro, esta função retorna o caminho do fiheiro selecionado.
   -   **entry_file_path.delete(0, tk.END):** limpa o conteúdo do entry_file_pathwidget, que normalmente é um Entrywidget Tkinter usado para exibir o caminho do ficheiro selecionado.
   -   **entry_file_path.insert(0, file_path):** insere o caminho do ficheiro selecionado pelo utilizador no entry_file_pathwidget.

**process_audio:**

 A função process_audio() realiza o processamento de áudio coletando parâmetros de entrada da GUI, calculando o tamanho e a sobreposição da janela e, em seguida, invocando a função alterar_audio com esses parâmetros, também lida com possíveis erros relacionados a ficheiros usando a FileNotFoundError.

   -   **filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Arquivos WAV", "*.wav")]):** abre uma caixa de diálogo para salvar o áudio processado.

Após selecionar o caminho para guardar ficheiro a função recupera todos os parâmetros relacionados com a modificação do som introduzidos pelo utilizador.

-   **input_path = entry_file_path.get():** recupera o caminho do fiheiro de entrada.
-   **pitch_factor = float(entry_pitch.get()):** recupera o fator de pitch.
-   **speed_factor = float(entry_speed.get()):** recupera o fator de velocidade.
-   **window_size_exp = int(entry_window_size_scale.get()):** recupera o valor do expoente do tamanho da janela.
-   **overlap_exp = int(entry_overlap_scale.get()):** recupera o expoente do valor de sobreposição.
-   **speed_slider_value = float(entry_speed.get()):** recupera o fator de velocidade.

Depois é feito o calculo do tamanho da janela e a sobreposição do som com base no valor escolhido pelo utilizador.

-   **window_size = 2^window_size_exp:** calcula o tamanho da janela.
-   **overlap = 2^overlap_exp:** calcula a sobreposição.

Por fim é chamado a função alterar_audio() com todos os parâmetros obtidos anteriomente.
   -   **alterar_audio(input_path, output_path, pitch_factor, speed_factor * speed_slider_value, window_size, overlap):** Esta função realiza a modificação do áudio com base nas escolhas do utilizador.
   -   **except FileNotFoundError:** captura a exeção "FileNotFoundError", que pode ocorrer se o ficheiro de entrada especificado não for encontrado, nesse caso, chama a função "errorIO()" para mostrar o erro ao utilizador.
  

**preview_audio:**

A função preview_audio() tal como a função anterior realiza o processamento de áudio coletando parâmetros de entrada da GUI e invoca a função alterar_audio() com esses parâmetros. Esta função é executada quando o utilizador pressiona o botão de pré-visualizar o áudio, logo é criado um ficheiro temporário com as alterações introduzidas pelo utilizador e utiliza-se a função play() para tocar o áudio modificado, após isso o ficheiro criado é removido.

- **output_path = "temp.wav":** especifica um caminho de saída temporário para o áudio modificado.
- **audio = AudioSegment.from_file(output_path):** Carrega o áudio modificado do ficheiro temporário.
- **play(audio):** Usa a função do Pydub play() para reproduzir o áudio modificado.
- **os.remove(output_path):** Remove o ficheiro temporário criado durante a pré-visualização para limpar ficheiros temporários.
- **except FileNotFoundError:** captura a exeção "FileNotFoundError", que pode ocorrer se o ficheiro de entrada especificado não for encontrado, nesse caso, chama a função "errorIO()" para mostrar o erro ao utilizador.


**errorIO:**

Esta função é um mecanismo simples de tratamento de erros para problemas relacionados à introdução de caminho de entrada e saída no programa, onde verifica se o caminho de entrada está vazio ou se existe no computador caso verifique um dos dois, exibe uma caixa de diálogo de mensagem de erro.

-   **input_path = entry_file_path.get():** recupera o caminho do ficheiro de entrada.
-   **if not input_path::** esta condição verifica se o caminho de entrada é uma string vazia ou se existe no computador.
-   **messagebox.showerror("Erro", "Introduza um caminho de ficheiro de áudio existente."):** se o caminho de entrada estiver vazio uma caixa de mensagem será exibida com uma mensagem de erro.
-   **messagebox.showerror("Erro", "Caminho introduzido não existe no seu computador."):** Se o caminho de entrada especificado não for encontrado, outra caixa de mensagem será exibida com uma mensagem de erro.
   
