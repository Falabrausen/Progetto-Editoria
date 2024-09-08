import os
from bs4 import BeautifulSoup

# Chiede all'utente il nome del file di input
input_file_name = input("Inserisci il nome del file di input (in formato Markdown): ")

# Compone il nome del file di output
output_file_name = input_file_name[:-2]+"xhtml"

# Esegue la conversione del file Markdown in HTML
os.system(f"pandoc -s {input_file_name} --template=custom-template.xhtml --metadata-file=metadata.txt -o {output_file_name}")

# Apre il file XHTML generato
with open(output_file_name) as f:
    soup = BeautifulSoup(f, "html.parser")

# Cerca il tag style e lo rimuove
for tag in soup("style"):
    tag.decompose()

# Salva il file HTML con il nuovo tag link
with open(output_file_name, "w") as f:
    f.write(str(soup))

print(f"Conversione completata. File generato: {output_file_name}")