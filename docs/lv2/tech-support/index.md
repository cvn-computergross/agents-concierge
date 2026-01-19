# Tech Support · v2 (Copilot Studio)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**

## Panoramica

Il supporto IT di primo livello non può risolvere ogni richiesta in autonomia.  
Problemi complessi, casi fuori knowledge base o richieste che richiedono **intervento umano** devono essere gestiti con un’escalation chiara, tracciabile e standardizzata.

**Tech Support (v2)** estende l’agente di primo livello introducendo una **gestione strutturata dell’escalation**, eliminando email informali, messaggi diretti o ticket incompleti.

## Continuità con il livello 1

Tech Support v2 **non sostituisce** il livello 1, ma lo completa.

- Il **LV1** si occupa di:
  - Risposte guidate basate esclusivamente su KB aziendale
  - Troubleshooting di primo livello
  - Riconoscimento delle richieste fuori perimetro

- Il **LV2** interviene quando:
  - Le informazioni in KB non sono sufficienti
  - Il problema richiede un’azione tecnica
  - L’utente chiede esplicitamente supporto umano

L’obiettivo non è “aprire più ticket”, ma **aprire ticket migliori**.

## Problema

Nella maggior parte delle organizzazioni, l’escalation presenta criticità ricorrenti:

- **Ticket incompleti o ambigui**
- **Canali non standard** (email, chat, messaggi diretti)
- **Assenza di contesto** tecnico o funzionale
- **Bassa tracciabilità** e priorità non chiare

Questo genera inefficienza sia per gli utenti sia per il team IT.

## Soluzione

**Tech Support (v2)** introduce un’escalation guidata e controllata:

- L’agente valuta se la richiesta può essere risolta in autonomia
- In caso contrario, **propone l’apertura di un ticket**
- La raccolta dati avviene tramite **Adaptive Card**
- Un **agent flow** registra il ticket in una **SharePoint List**
- Il team IT riceve richieste **complete, standardizzate e subito lavorabili**

Il risultato è un flusso:

> Conversazione → Decisione → Raccolta dati → Ticket strutturato

## Come funziona l’escalation

### 1. Riconoscimento del limite
L’agente identifica che:
- la richiesta non è coperta dalla KB  
- oppure non è risolvibile con le informazioni disponibili

### 2. Conferma dell’utente
L’utente viene guidato e informato, non “scaricato”:
> *Vuoi aprire un ticket per ricevere supporto dal team IT?*

### 3. Raccolta strutturata
Tramite Adaptive Card vengono richiesti:
- Titolo del problema
- Descrizione dettagliata
- Eventuali informazioni aggiuntive

### 4. Creazione del ticket
Un flow dedicato:
- Scrive i dati nella SharePoint List
- Mantiene coerenza e tracciabilità
- Può essere esteso a sistemi ITSM esterni

## Esempi di utilizzo

### Escalation dopo troubleshooting

**Richiesta utente**

`OneDrive mi restituisce errore di accesso, ho già provato a riconnettermi`

**Comportamento dell’agente**

1. Verifica la KB disponibile
2. Riconosce il limite del supporto automatico
3. Propone apertura ticket
4. Raccoglie i dettagli via Adaptive Card
5. Registra il ticket per il team IT

### Apertura ticket diretta

**Richiesta utente**

`Vorrei aprire un ticket per un problema tecnico`

**Comportamento dell’agente**

1. Salta il troubleshooting
2. Attiva direttamente il flusso di ticketing
3. Garantisce una richiesta completa e standard

## Benefici principali

- Riduzione drastica dei ticket incompleti
- Migliore esperienza per l’utente finale
- Minor carico cognitivo per il team IT
- Tracciabilità e governance del processo
- Base solida per integrazioni ITSM avanzate

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**
