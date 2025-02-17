import subprocess
import sys

def remove_duplicates_with_awk(file=None):
    if file:
        # Ler a partir de um ficheiro
        with open(file, 'r') as f:
            subprocess.run(['awk', '!a[$0]++'], text=True, stdin=f, stdout=sys.stdout)
    else:
        # Modo interativo
        print("Digite as linhas (pressione Ctrl+D para terminar):")
        try:
            subprocess.run(['awk', '!a[$0]++'], text=True, stdin=sys.stdin, stdout=sys.stdout)
        except KeyboardInterrupt:
            pass 

if __name__ == "__main__":
    # Verifica se um argumento (ficheiro) foi fornecido
    if len(sys.argv) > 1:
        remove_duplicates_with_awk(file=sys.argv[1])
    else:
        remove_duplicates_with_awk()
