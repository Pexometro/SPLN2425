import sys

def remove_duplicates(lines):
    seen = set()
    for line in lines:
        line = line.rstrip()  
        if line not in seen:
            sys.stdout.write(line + "\n")  
            seen.add(line)

if __name__ == "__main__":
    if not sys.stdin.isatty():  
        remove_duplicates(sys.stdin)
    else:  # Modo interativo
        print("Digite as linhas (pressione Ctrl+D para terminar):")
        try:
            remove_duplicates(iter(input, ''))  
        except EOFError:
            pass  # (Ctrl+D)
