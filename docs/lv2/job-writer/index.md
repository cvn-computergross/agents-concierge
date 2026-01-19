
# Job Writer · v2 (Copilot Studio)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**
## Panoramica

Il processo di creazione degli annunci di lavoro è stato semplificato con **Job Writer (v1)**, che permette di generare annunci e salvarli in Word. Tuttavia, la versione precedente presenta limiti: il documento non è perfettamente identico alla versione in chat e richiede interventi manuali per correggere formattazione e struttura.

**Job Writer (v2)** supera questi limiti introducendo:

- Creazione guidata tramite **topic dedicato**, che accelera la raccolta dati.
- Utilizzo di **Prompt Action** per applicare il template aziendale in modo immediato e  un annuncio più accurato e professionale.
- Generazione automatica di un documento Word **perfettamente identico alla versione in chat**
- Salvataggio diretto del file in **OneDrive dell’utente** tramite integrazione MCP Server

Queste evoluzioni trasformano l’agente da semplice generatore di testo a **strumento completo per la gestione degli annunci**, riducendo ulteriormente il carico operativo del team HR.

## Continuità con il livello 1

Job Writer v2 **non sostituisce** il livello 1, ma lo completa.

- Il **LV1** si occupa di:

  - Generazione rapida di annunci rispettando un template.
  - Salvataggio in Word **con formattazione non sempre fedele**.
  - Output in chat pronto per copia/incolla.

- Il **LV2** interviene quando:

  - Serve una creazione guidata per annunci di lavoro di qualità superiore.
  - È richiesta **fedeltà totale tra l'annuncio in chat e il documento Word**
  - Serve una **riduzione del tempo di revisione**.
  - È richiesta una **Standardizzazione degli annunci** per garantire uniformità tra reparti e sedi.

L’obiettivo è **automatizzare l’intero flusso**, dalla richiesta alla pubblicazione, senza correzioni manuali.

## Problema

Anche con Job Writer v1, persistono criticità:

- **Documento Word non identico alla chat** (richiede correzioni manuali)
- **Rischio di perdita di formattazione** tra generazione e salvataggio
- **Processo non ottimizzato** per velocità e qualità dell'output.

Queste lacune rallentano il processo e aumentano il rischio di errori.

## Soluzione

**Job Writer (v2)** risolve queste criticità con un percorso guidato e automatizzato:

- Avvio tramite **topic guidato** che raccoglie gli input
- Generazione dell’annuncio con **Prompt Action** e template ufficiale
- Creazione di un documento Word **perfettamente identico alla versione in chat**
- Salvataggio diretto in **OneDrive dell’utente** tramite MCP Server

Il risultato è un flusso:
> Conversazione → Raccolta dati → Generazione → Documento pronto e salvato

## Come funziona

### 1. Avvio del topic guidato

L’agente:

- Verifica se gli input richiesti sono già presenti
- Richiede solo le informazioni mancanti

### 2. Generazione dell’annuncio

- Utilizza **Prompt Action** con il template aziendale
- Mantiene coerenza e conformità 

### 3. Creazione del documento Word

- Replica **esattamente** il contenuto generato in chat
- Applica la formattazione ufficiale senza interventi manuali

### 4. Salvataggio in OneDrive

- Tramite MCP Server, il documento viene salvato automaticamente
- Garantisce tracciabilità e accesso immediato per l’utente

## Esempio di utilizzo

### Creazione guidata con salvataggio automatico

**Richiesta utente**

`Vorrei creare un annuncio di lavoro completo e salvarlo in Word`

**Comportamento dell’agente**

1. Avvia il topic guidato
2. Raccoglie le informazioni necessarie
3. Genera l’annuncio con il template ufficiale
4. Crea il documento Word identico alla chat
5. Salva il file in OneDrive dell’utente

## Benefici principali

- **Fedeltà totale** tra chat e documento Word
- **Velocità operativa**: riduzione drastica dei passaggi manuali
- **Integrazione nativa con OneDrive** per accesso immediato
- **Flusso HR completamente automatizzato**

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**