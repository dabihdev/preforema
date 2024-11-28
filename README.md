# PREFOREMA - PREtemp FOREcast MAnager (codice sorgente per sviluppatori)

In questa repo è contenuto il codice sorgente del software PREFOREMA. PREFOREMA è un'applicazione volta a semplificare, velocizzare e standardizzare il lavoro di previsione e pubblicazione dei meteorologi di [PRETEMP](https://www.pretemp.it/).

Il contenuto di questa repo è quindi rivolto agli **sviluppatori** del progetto. Se desideri solo scaricare il programma già compilato e funzionante vai alla repo [preforema-release](https://github.com/dabihdev/preforema-release).

## 1. Requisiti
- Windows a 64bit (la libreria `os` funziona solo su Windows)
- Python 3.6.5 o superiore
- [python-docx](https://pypi.org/project/python-docx/#files), libreria Python per lavorare con i file documento .docx
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), libreria Python per scraping e parsing di file XML/HTML
- OPZIONALE: [Git](https://git-scm.com/downloads) per il controllo di versione

## 2. Installazione
Per clonare l'intera repo nel tuo pc, vai alla tua cartella locale dove vuoi scaricare il codice, apri Git Bash (o software simile) e digita 

```
git clone https://github.com/dabihdev/preforema
```

Se non sei interessato alla cronologia delle modifiche, sulla pagina github clicca "Code" e poi "Download ZIP".

**ATTENZIONE:** La cartella `assets/`, contenente i template della mappa e della pagina html, non è inclusa tra i file di progetto. **Affinché PREFOREMA funzioni, la cartella `assets/` deve essere inclusa nella root del progetto.** Potete trovare la cartella `assets/` nel Drive di PRETEMP.
