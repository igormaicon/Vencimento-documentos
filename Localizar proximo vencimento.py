import os
import re
from datetime import datetime, timedelta
import pdfplumber

def extrair_datas_vigencia(texto):
    padrao = r"(\d{2}/\d{2}/\d{4}) à (\d{2}/\d{2}/\d{4})"
    resultado = re.search(padrao, texto)
    if resultado:
        data_inicio = datetime.strptime(resultado.group(1), "%d/%m/%Y")
        data_fim = datetime.strptime(resultado.group(2), "%d/%m/%Y")
        return data_inicio, data_fim
    return None, None

def verificar_vencimento_pdfs(pasta, dias_alerta=30):
    hoje = datetime.today()
    arquivos_vencidos = []

    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith(".pdf"):
            caminho = os.path.join(pasta, arquivo)
            try:
                with pdfplumber.open(caminho) as pdf:
                    texto = ""
                    for pagina in pdf.pages:
                        texto += pagina.extract_text() or ""
                    
                    # Extrai datas de vigência
                    data_inicio, data_fim = extrair_datas_vigencia(texto)
                    if data_fim:
                        dias_restantes = (data_fim - hoje).days
                        if dias_restantes < 0:
                            status = f"⚠️ VENCIDO há {-dias_restantes} dias"
                            arquivos_vencidos.append((arquivo, status, data_fim))
                        elif dias_restantes <= dias_alerta:
                            status = f"⚠️ PRESTES A VENCER em {dias_restantes} dias"
                            arquivos_vencidos.append((arquivo, status, data_fim))
            except Exception as e:
                print(f"Erro ao ler {arquivo}: {e}")

    # Resultado
    if arquivos_vencidos:
        print("\n### Documentos Perto do Vencimento ###")
        for doc, status, data in arquivos_vencidos:
            print(f"{doc} - {status} (Vence em: {data.strftime('%d/%m/%Y')})")
    else:
        print("✅ Nenhum documento está perto de vencer.")

def main():
    print("### Verificador de Vencimento de Documentos PDF ###")
    pasta = input("Informe o caminho da pasta com os PDFs: ").strip()
    dias_alerta = int(input("Quantos dias antes deseja ser alertado? (padrão: 30): ") or 30)
    verificar_vencimento_pdfs(pasta, dias_alerta)

if __name__ == "__main__":
    main()
