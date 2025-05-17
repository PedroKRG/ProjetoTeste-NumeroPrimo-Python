 Verificador de Números Primos
Este é um simples programa em Python que verifica se um número fornecido pelo usuário é primo.

📋 Descrição
O programa solicita ao usuário que digite um número inteiro e, em seguida, verifica se esse número é primo utilizando uma função personalizada. Um número primo é um número natural maior que 1 que possui apenas dois divisores: 1 e ele mesmo.

⚙️ Como funciona
A função eh_primo(numero) verifica se um número é primo.

A função main() lida com a entrada do usuário e exibe o resultado da verificação.

📌 Exemplo de uso
bash
Copiar
Editar
$ python verificador_primo.py
Coloque um número para verificar se é primo:
7
7 é primo
🧠 Lógica do algoritmo
Números menores que 2 não são primos.

O algoritmo testa divisores de 2 até a raiz quadrada do número.

Se algum divisor for encontrado, o número não é primo.

🖥️ Requisitos
Python 3.x

🚀 Como executar
Salve o código em um arquivo, por exemplo: verificador_primo.py.

Execute no terminal com o comando:

bash
Copiar
Editar
python verificador_primo.py
