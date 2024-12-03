import json
from datetime import datetime

def salvar_bug_report(erro, contexto, arquivo="bug_report.json"):
    """
    Salva informações de bugs em um arquivo JSON.
    """
    bug = {
        "erro": str(erro),
        "contexto": str(contexto),
        "timestamp": datetime.now().isoformat()
    }

    try:
        with open(arquivo, "a") as file:
            json.dump(bug, file, ensure_ascii=False, indent=4)
            file.write(",\n")
        print(f"Bug report salvo no arquivo: {arquivo}")
    except Exception as e:
        print(f"Erro ao salvar bug report: {e}")
