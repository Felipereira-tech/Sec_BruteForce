# ZIP Password Brute-Forcer 🔐

Um script simples e eficiente em Python para recuperar senhas de arquivos `.zip` através de um ataque de força bruta. 

Este projeto foi desenvolvido com foco na simplicidade e na visualização do processo, testando combinações de caracteres em tempo real até encontrar a senha correta. O script **não extrai** o conteúdo do arquivo automaticamente, apenas exibe a senha descoberta no terminal.

> ⚠️ **Aviso Legal:** Este script tem fins puramente educacionais e de recuperação de dados próprios. Utilize-o apenas em arquivos dos quais você é o proprietário ou possui permissão explícita para testar.

---

## 🚀 Funcionalidades

* **Busca Otimizada:** Testa combinações iniciando por números, seguidos por letras minúsculas, maiúsculas e, por fim, símbolos (garantindo que senhas simples como `0000` sejam testadas primeiro).
* **Feedback em Tempo Real:** Exibe no terminal a combinação atual sendo testada e o contador total de tentativas.
* **Segurança (Sem Extração):** Valida a senha diretamente na memória. O arquivo original não é modificado e seu conteúdo não é extraído no disco automaticamente.
* **Interrupção Segura:** Tratamento para `Ctrl+C`, permitindo cancelar o ataque a qualquer momento sem exibir erros poluídos na tela.

---

## 🛠️ Tecnologias e Bibliotecas

O script foi escrito em **Python 3** e utiliza apenas bibliotecas padrão, não sendo necessário instalar dependências externas:

* `zipfile` (Manipulação e validação do ZIP)
* `itertools` (Geração das combinações de força bruta)
* `string` (Dicionário de caracteres)
* `time` & `sys` (Cálculo de tempo e formatação do terminal)

---


**2. Prepare o arquivo:**
Coloque o arquivo ZIP que você deseja testar no mesmo diretório do script e certifique-se de que ele tenha o nome definido no código (por padrão: `arquivos_secretos.zip`).

**3. Execute o script:**
```bash
python nome_do_script.py
```

---

## 🔧 Configuração Customizada

O script está configurado por padrão para buscar senhas de **4 caracteres**. 

Se você deseja testar senhas de tamanhos diferentes, basta alterar a seguinte variável no código:

```python
tamanho_senha = 5 # Altere para o número de dígitos desejado
```
*Atenção: Aumentar o tamanho da senha aumenta exponencialmente o número de combinações e o tempo necessário para o ataque.*

---

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
