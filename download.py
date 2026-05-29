import subprocess
import sys

print("==== INSTALLAZIONE GUIDATA DI PYTHONOS =====")

print("Questa procedura installerà PythonOS sul tuo computer. Assicurati di avere Python e pip installati prima di procedere.")

input("Premi Invio per continuare...")

print("Passo 1: Installazione di Requests")

eseguibile = sys.executable

subprocess.run(f'"{eseguibile}" -m pip install requests', shell=True)

print("Passo 2: Clonazione del repository di PythonOS tramite Requests e installazione")

to_install = input("Dove desideri installare PythonOS? (Inserisci il percorso completo, es. C:\\Users\\TuoNome\\pythonos): ")

import requests
import os

url = "https://api.github.com/repos/pythonos-project/pythonos/tarball"

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open("pythonos.tar.gz", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download completato. Estrazione dei file...")
    import tarfile
    with tarfile.open("pythonos.tar.gz", "r:gz") as tar:
        tar.extractall(path=to_install)
    os.remove("pythonos.tar.gz")
    print(f"PythonOS è stato installato con successo in {to_install}")

input("Premi Invio per uscire...")
