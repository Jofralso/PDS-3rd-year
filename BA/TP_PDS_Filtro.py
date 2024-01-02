import sys
import pyaudio
import threading
import time
import wave
import numpy as np
from scipy.signal import butter, lfilter

# Flag for stopping record and playback
stop_flag = threading.Event()

#---------------Variables-----------------
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

LOWCUTTOFF = 400
HIGHCUTTOFF = 800
filter_type = 'lowpass'

frames = []
filtered_data = []
#-----------------------------------------

#input and output indexes change according to device used, typicaly range between 0 and 3
input_device_index = 0
output_device_index = 3

# Filter
def butterworth_filter(data, lowcut, highcut, RATE, order, filter_type):
    global LOWCUTTOFF, HIGHCUTTOFF
    nyquist = 0.5 * RATE
    
    if filter_type == 'lowpass' or filter_type == 'highpass':
        normal_cutoff = lowcut / nyquist
        b, a = butter(order, normal_cutoff, btype=filter_type, analog=False)
    else:
        if lowcut > highcut:
            l = lowcut
            lowcut = highcut
            highcut = l
            LOWCUTTOFF = lowcut
            HIGHCUTTOFF = highcut
            
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(order, [low, high], btype=filter_type, analog=False)
    
    # Convert data to np.int16 and apply the filter
    np_data = np.frombuffer(data, dtype=np.int16)
    filtered_np_data = lfilter(b, a, np_data)

    # Convert filtered data back to bytes and append to filtered_data list
    filtered_data.append(filtered_np_data.astype(np.int16).tobytes())

#----------------------------------------------------------------------------------------
# method for saving pre-filter audio to .wav
def save_audio_before_filter(frames, filename='audio_before_filter.wav'):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"\nFicheiro antes do filtro {filename}")

# method for saving post-filter audio to .wav
def save_audio_after_filter(filtered_frames, filename='audio_after_filter.wav'):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(filtered_frames))
    wf.close()
    print(f"\nFicheiro depois do filtro {filename}")
#--------------------------------------------------------------------------------------------
# audio record method wich also calls the filter method while passing each instance of data
def record_audio(stream, frames):
    while not stop_flag.is_set():
        if stream.is_active():  
            data = stream.read(CHUNK)
            frames.append(data)
            butterworth_filter(data, LOWCUTTOFF, HIGHCUTTOFF, RATE, 4, filter_type)
        else:
            break

# audio playback method
def play_audio(stream, filtered_data):
    while not stop_flag.is_set():
        if stream.is_active():
            for data in filtered_data:
                stream.write(data)
        else:
            time.sleep(0.1)
#--------------------------------------------------------------------------------------------
# open audio input and output streams
p = pyaudio.PyAudio()

stream_in = p.open(format=pyaudio.paInt16,
               channels=2,
               rate=44100,
               input=True,
               input_device_index=input_device_index,
               frames_per_buffer=CHUNK)

stream_out = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=44100,
                output=True,
                output_device_index=output_device_index,
                frames_per_buffer=CHUNK)

#-------------------------------------------------------------------------------------------
# create and start record and playback threads

record_thread = threading.Thread(target=record_audio, args=(stream_in, frames))
play_thread = threading.Thread(target=play_audio, args=(stream_out, filtered_data))

record_thread.start()
play_thread.start()


#-------------------------------------------------------------------------------------------
def text_menu():
    print("\nFiltro atual:", filter_type)
    if filter_type == 'lowpass' or filter_type == 'highpass':
        print("Frequencia de corte:", LOWCUTTOFF)
    else:
        print("Frequencia de corte inferior:", LOWCUTTOFF)
        print("Frequencia de corte superior:", HIGHCUTTOFF)
        
    print("\n1. Alterar frequencia de corte")
    print("2. Alterar tipo de filtro")
    print("3. Dispositivos de entrada e saida de audio")
    print("4. Exit")


def option1():
    if filter_type == 'lowpass':
        corte1()
    elif filter_type == 'highpass':
        corte1()
    elif filter_type == 'bandpass':
        corte2()
    elif filter_type == 'bandstop':
        corte2()
    else: print("Invalid")
        
def option2():
    global filter_type
    a = int(input("\nEscolha o novo tipo de filtro:\n1-Lowpass\n2-Highpass\n3-Bandpass\n4-Bandstop\n"))
    if a == 1:
        filter_type = 'lowpass'
    elif a == 2:
        filter_type = 'highpass'
    elif a == 3:
        filter_type = 'bandpass'
    elif a == 4:
        filter_type = 'bandstop'
    else: print("Invalid")    

def option3(): 
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')

    print("\nLista de Dispositivos de Saída:")

    for i in range(num_devices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        device_name = device_info.get('name')
        print(f"{i}. {device_name}")
    
    print("\nDispositivos atuais\n")
    print("Input:  ", input_device_index)
    print("output: ", output_device_index)
    input()
    
def option4():
    print("\nParando a gravação e reprodução...\n")
    stop_flag.set()  

    # wait for thread end with 5 sec time limit
    record_thread.join(timeout=5)
    play_thread.join(timeout=5)

    if record_thread.is_alive()  or play_thread.is_alive():
        print("As threads ainda estão em execução. Fechando forçadamente.")
    else:
        print("As threads foram encerradas com sucesso.")
    # method call for saving audio to wav files
    save_audio_before_filter(frames)
    save_audio_after_filter(filtered_data)

    # close stream
    stream_in.stop_stream()
    stream_out.stop_stream()
    stream_in.close()
    stream_out.close()

    # end PyAudio
    p.terminate()
    sys.exit()
#------------------------------------------------------------------------------------------
def corte1():
    global LOWCUTTOFF
    LOWCUTTOFF = int(input("Introduza a nova frequencia de corte: "))
    
def corte2():
    global LOWCUTTOFF, HIGHCUTTOFF
    LOWCUTTOFF = int(input("Introduza a nova frequencia de corte inferior: "))
    HIGHCUTTOFF = int(input("Introduza a nova frequencia de corte superior: "))
#-------------------------------------------------------------------------------------------
# Main program
while True:
    text_menu()       
    choice = input("\nEscolha a opçao (1-4): ")    
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
        break
    else:
        print("Opcao invalida. Introduza um numero de 1 a 4.")



