import os
from docx2pdf import convert
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def converter_com_env():
    # Busca o caminho da variável de ambiente
    caminho = os.getenv("CAMINHO_DOCUMENTOS")

    if not caminho:
        print("Erro: A variável CAMINHO_DOCUMENTOS não foi definida no arquivo .env")
        return

    if not os.path.exists(caminho):
        print(f"Erro: O diretório configurado não existe: {caminho}")
        return

    try:
        print(f"Acessando pasta: {caminho}")
        print("Convertendo arquivos... por favor, aguarde.")
        convert(caminho)
        print("Finalizado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    converter_com_env()