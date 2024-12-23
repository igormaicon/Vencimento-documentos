Verificador de Vencimento de Documentos PDF
Este repositório contém um script em Python que verifica a data de vencimento de documentos em formato PDF. O script extrai datas de vigência de documentos e alerta o usuário sobre documentos que estão prestes a vencer ou que já estão vencidos.

Funcionalidades
Extração de Datas: O script utiliza expressões regulares para identificar e extrair datas de vigência no formato dd/mm/yyyy à dd/mm/yyyy.
Verificação de Vencimento: Analisa todos os arquivos PDF em uma pasta especificada e verifica se estão vencidos ou prestes a vencer.
Alertas: Gera alertas para documentos que estão prestes a vencer dentro de um número de dias especificado pelo usuário.
Pré-requisitos
Para executar este script, você precisará ter o Python instalado em sua máquina, além da biblioteca pdfplumber. Você pode instalar a biblioteca necessária usando o seguinte comando:

```pip install pdfplumber```

Como Usar
Clone este repositório ou baixe o arquivo do script.

Abra um terminal e navegue até o diretório onde o script está localizado.

Execute o script com o comando:

```python nome_do_script.py```

Quando solicitado, informe o caminho da pasta que contém os arquivos PDF.

Informe quantos dias antes deseja ser alertado sobre o vencimento dos documentos (o padrão é 30 dias).

Exemplo de Uso
```
### Verificador de Vencimento de Documentos PDF ###
Informe o caminho da pasta com os PDFs: /caminho/para/pasta
Quantos dias antes deseja ser alertado? (padrão: 30): 15
```

