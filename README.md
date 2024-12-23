Verificador de Vencimento de Documentos PDF
Este projeto é um script em Python que verifica a data de vencimento de documentos em formato PDF. Ele extrai as datas de vigência dos documentos e informa se estão vencidos ou prestes a vencer, com base em um número de dias de alerta definido pelo usuário.

Funcionalidades
Extração de Datas: O script utiliza expressões regulares para identificar e extrair datas de vigência no formato dd/mm/yyyy à dd/mm/yyyy.
Verificação de Vencimento: Analisa todos os arquivos PDF em uma pasta especificada e verifica se as datas de vencimento estão próximas ou já passaram.
Alertas: Informa ao usuário sobre documentos vencidos e aqueles que estão prestes a vencer, com a quantidade de dias restantes.
Dependências
Para executar este script, você precisará das seguintes bibliotecas Python:

pdfplumber: Para extrair texto de arquivos PDF.
datetime: Para manipulação de datas.
os e re: Para operações de sistema e expressões regulares.
Você pode instalar a biblioteca necessária usando o seguinte comando:

''' bash

Verify

Open In Editor
Run
Copy code
pip install pdfplumber
Como Usar
Clone o repositório ou baixe o arquivo Python.
'''
Execute o script em um terminal ou prompt de comando:

bash

Verify

Open In Editor
Run
Copy code
python nome_do_arquivo.py
Informe o caminho da pasta onde os arquivos PDF estão localizados.

Defina o número de dias antes do vencimento para receber alertas (o padrão é 30 dias).

Exemplo de Uso
plaintext

Verify

Open In Editor
Run
Copy code
### Verificador de Vencimento de Documentos PDF ###
Informe o caminho da pasta com os PDFs: /caminho/para/pasta
Quantos dias antes deseja ser alertado? (padrão: 30): 15
Saída
O script irá listar os documentos que estão vencidos ou prestes a vencer, com a seguinte formatação:

plaintext

Verify

Open In Editor
Run
Copy code
### Documentos Perto do Vencimento ###
documento1.pdf - ⚠️ VENCIDO há 5 dias (Vence em: 01/01/2023)
documento2.pdf - ⚠️ PRESTES A VENCER em 10 dias (Vence em: 15/01/2023)
Se não houver documentos próximos do vencimento, a seguinte mensagem será exibida:

plaintext

Verify

Open In Editor
Run
Copy code
✅ Nenhum documento está perto de vencer.
Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório, crie uma branch para sua feature ou correção e envie um pull request.

Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
