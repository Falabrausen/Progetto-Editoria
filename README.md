# Progetto-Editoria
## Introduzione

Questo progetto nasce con l'intento di trascrivere alcune ricette da un vecchio libro per il Bimby, in un formato moderno e accessibile su dispositivi tecnologici.

Questo ricettario è un progetto molto importante che permetterà di condividere, con chiunque ne farà uso, una lista di deliziose ricette.Sarà dunque un grande alleato in cucina per tutti coloro che desiderano sperimentare qualche nuova ricetta e far colpo su parenti e amici con pochi e semplici passaggi.

Questo ricettario sarà da ora accessibile da chiunque in qualsiasi momento della giornata e potrà essere facilmente ricondiviso con amici o chiunque si desideri.


## Estensione e-book

Questo progetto oltre che essere di facile condivisione è anche facilmente estendibile. Vediamo come.

### Fase 1: Creazione

Prima di tutto è necessario trascrivere la ricetta in un file markdown e salvare il file nella cartella `Extra`.

### Fase 2: Trasformazione

In questa fase andremo a trasformare il file nel formato xhtml.

> N.B.: Per poter far funzionare correttamente questa fase è necessario aver installato precedentemente [pandoc](https://pandoc.org/installing.html) e [python](https://www.python.org/downloads/).

1. A questo punto dobbiamo aprire il `cmd`, recarci nella cartella `Extra` e digitare questo codice:
    ```
    python convertitore.py
    ```
2. Verrà avviato uno script python che ci chiederà il nome del file che vogliamo convertire. A questo punto non dovremo fare altro che inserire il nome del file markdown creato. Ad esempio: `pastaPomodoro.md`.
3. Il programma ci avrà creato ora nella cartella `Extra`, un nuovo file, che seguendo l'esempio del punto 2, si chiamerà `pastaPomodoro.xhtml`.

### Fase 3: Inserimento nell'e-book

Una volta ottenuto il file con estensione .xhtml dovremo aggiungerlo al nostro e-book.

> N.B.: Per questo progetto è stato utilizzato il software [Sigil](https://sigil-ebook.com/sigil/download/). Di conseguenza le istruzioni che verranno date saranno specifiche per questa applicazione.

1. Aprire il file con estensione **.epub** in Sigil.
2. Nella sezione '**Navigatore del Libro**' cercare la cartella `Text`.
3. Premere il tasto destro sulla cartella e cliccare '**Aggiungi file esistenti...**' e selezionare il file generato al passo precedente.
4. Modificare il file `nav.xhtml` andando a inserire al posto corretto il link al file appena aggiunto.
5. Infine aggiungere la pagina appena creata all'indice analitico selezionando il titolo della ricetta e cliccando poi il tasto '**Aggiungi il testo selezionato all'Editor dell'indice analitico**'.

