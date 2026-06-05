import zipfile
import itertools
import string
import time
import sys
import zlib

def brute_force_zip(zip_file_path):
    # 1. ORDEM ALTERADA: Começa com números, depois letras, depois símbolos.
    # Isso garante que a primeira tentativa seja '0000'
    caracteres = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    tamanho_senha = 4

    print(f"[*] Iniciando ataque de força bruta no arquivo: {zip_file_path}")
    print(f"[*] Tamanho da senha configurado: {tamanho_senha} dígitos")
    print(f"[*] Total de caracteres possíveis: {len(caracteres)}")
    print("[*] Testando combinações em tempo real...\n")

    tempo_inicio = time.time()
    tentativas = 0

    try:
        for combinacao in itertools.product(caracteres, repeat=tamanho_senha):
            tentativas += 1
            senha_tentativa = "".join(combinacao)

            # Mostra no terminal a senha atual mudando rapidamente
            sys.stdout.write(f"\r[>] Tentando: {senha_tentativa}  |  Total: {tentativas}")
            sys.stdout.flush()

            try:
                with zipfile.ZipFile(zip_file_path, 'r') as arquivo_zip:
                    # Define a senha apenas para verificação na memória
                    arquivo_zip.setpassword(senha_tentativa.encode('utf-8'))
                    
                    # testzip() apenas valida se a senha abre o arquivo sem erros
                    if arquivo_zip.testzip() is None:
                        tempo_fim = time.time()
                        
                        # 2. SEM EXTRAÇÃO: Apenas imprime a senha na tela e encerra
                        print(f"\n\n[+] SUCESSO! A senha é: {senha_tentativa}")
                        print(f"[i] Tempo decorrido: {tempo_fim - tempo_inicio:.2f} segundos")
                        print(f"[i] Total de tentativas: {tentativas}")
                        print("[*] O arquivo NÃO foi descompactado. Você pode abri-lo manualmente com a senha acima.")
                        return senha_tentativa

            except (RuntimeError, zipfile.BadZipFile, zlib.error, ValueError):
                # Se der erro, a senha está errada. Passa para a próxima.
                pass

    except KeyboardInterrupt:
        print("\n\n[!] Ataque interrompido pelo usuário (Ctrl+C).")
        sys.exit()

    print("\n\n[-] Falha. Todas as combinações foram esgotadas.")
    return None

if __name__ == "__main__":
    arquivo_alvo = "arquivos_secretos.zip"
    brute_force_zip(arquivo_alvo) 