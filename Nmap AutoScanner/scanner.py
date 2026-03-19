import subprocess

alvo = input("Digite o ip do alvo: ")

tipo_scan = input("Escolha o tipo de scan 1(simples) ou 2(completo): ")

print("Scan em processo...")

if tipo_scan == "1":
    comando = ["nmap", "-sS", alvo]
elif tipo_scan == "2":
    comando = ["nmap", "-A", alvo]
else:
    print("Erro de tipo de scan")
    exit()

subprocess.run(comando)

try:
    print("Scan finalizado com sucesso!")
except Exception as e:
    print("Erro ao executar o scan", e)