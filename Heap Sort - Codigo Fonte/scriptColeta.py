import subprocess
import re
import statistics

def executar_comando_e_anotar_saida(comando_str):

    try:

        processo = subprocess.run(comando_str, capture_output=True, text=True, check=False, encoding='utf-8', errors='replace', executable="C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe", shell=True)

        stdout_str = processo.stdout

        if stdout_str:

            match = re.search(r"TotalSeconds\s*:\s*([\d,]+)", stdout_str)

            if match:
                total_seconds_str = match.group(1)
                total_seconds_float = round(float(total_seconds_str.replace(',', '.'), ), 3)
                return total_seconds_float
            else:
                print("TotalSeconds não encontrado.")
        else:
            print("(vazia)")

    except FileNotFoundError:
        print(f"Erro: Comando '{comando_str.split()[0] if comando_str else ''}' não encontrado. Verifique se está no PATH.")
        return None, "Comando não encontrado.", -1 # Código de erro arbitrário
    except Exception as e:
        print(f"Ocorreu um erro ao tentar executar o comando: {e}")
        return None, str(e), -1 # Código de erro arbitrário

if __name__ == "__main__":

    comando_digitado1 = "Measure-Command { ./heapsort  }"  # Exemplo de comando para medir o tempo de execução do heapsort.py
    comando_digitado2 = "Measure-Command { py ./heapsort.py  }"  # Exemplo de comando para medir o tempo de execução do heapsort.py

    times = []

    #overhead = 0.194
    #overhead = 0.137
    #overhead = 0.095
    #overhead = 0.092
    #overhead = 0.087
    #overhead = 0.088
    #overhead = 0.084
    #overhead = 0.082
    #overhead = 0.080

    #overhead = 0.013
    #overhead = 0.011
    #overhead = 0.009
    #overhead = 0.009
    #overhead = 0.008
    #overhead = 0.008
    #overhead = 0.008
    #overhead = 0.007
    overhead = 0.008
    
    #overhead = 0

    for _ in range(30):
        times.append(round(executar_comando_e_anotar_saida(comando_digitado1) - overhead,4))

    print("Valores: ", times)
    media = sum(times) / len(times)
    desvioPadrao = statistics.stdev(times)
    print(f"\nMédia dos tempos de execução: {media:.4f} segundos")
    #print("media do Overhead:", round(media, 3))
    print(f"Desvio padrão dos tempos de execução: {desvioPadrao} segundos")
