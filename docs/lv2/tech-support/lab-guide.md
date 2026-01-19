# Lab Guide (Tech Support · v2)

## Obiettivo della Lab

In questa lab verrà implementata una **gestione strutturata dell’escalation**, tramite:

- raccolta guidata delle informazioni con **Adaptive Card**
- creazione automatica di un ticket
- scrittura dei dati in una **SharePoint List**

Al termine, l’agente sarà in grado di:
- riconoscere quando non può risolvere una richiesta
- proporre l’apertura di un ticket
- generare richieste complete e tracciabili per il team IT

## Prerequisiti

- Accesso a **Copilot Studio**
- Un sito **SharePoint Online** (anche demo)

---

## Step 1 – Preparare la lista SharePoint per i ticket

Creare una nuova **SharePoint List** che fungerà da sistema di ticketing minimale.

### Colonne consigliate

| Nome colonna | Tipo                              |
| ------------ | --------------------------------- |
| Title        | Single line of text               |
| Description  | Multiple lines of text            |
| Created      | Date (default)                    |
| Created By   | Person (default)                  |
| Status       | Choice (New, In Progress, Closed) |
|              |                                   |
![[Pasted image 20260115144417.png]] 

> La struttura è volutamente semplice: l’obiettivo è dimostrare il flusso, non replicare un ITSM completo.

---

## Step 2 – Creare il Topic di escalation

In Copilot Studio, creare un nuovo **Topic**:

- **Name**: `Ticket Request`
- **Description**:  `Handles cases where the assistant cannot resolve the request or when the user explicitly asks to open a support ticket.`

![[Pasted image 20260115145208.png]]

Questo topic rappresenta il **punto di ingresso obbligato** per ogni escalation.

---

## Step 3 – Confermare l’intenzione dell’utente

All’interno del topic:

1. Aggiungere un nodo **Ask a question**
2. Chiedere conferma esplicita, ad esempio:
 > Vuoi aprire un ticket per ricevere supporto dal team IT?

3. Creare un **ramo condizionale**:
 - **Yes** → proseguire
 - **No** → uscita dal topic

Questo passaggio evita aperture accidentali o premature.

---

## Step 4 – Raccogliere le informazioni con Adaptive Card

Nel ramo di conferma, inserire un nodo **Ask a question → Adaptive Card**.

### Esempio di campi minimi

- Titolo del problema
- Descrizione dettagliata

Esempio concettuale:
- `Issue` (obbligatorio)
- `Description` (obbligatorio)

> L’uso dell’Adaptive Card garantisce:
> - completezza delle informazioni
> - standardizzazione
> - migliore esperienza utente

![[Pasted image 20260115145250.png]]

Esempio di Adaptive Card:

```
{

    "$schema": "https://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.5",
    "body": [
        {
            "type": "TextBlock",
            "text": "Support Ticket Request",
            "weight": "Bolder",
            "size": "Medium"
        },
        {
            "type": "TextBlock",
            "text": "Please provide the details of your issue.",
            "wrap": true
        },
        {
            "type": "Input.Text",
            "id": "issue",
            "placeholder": "Enter a short issue title",
            "isRequired": true,
            "errorMessage": "Issue title is required.",
            "label": "Issue"
        },
        {
            "type": "Input.Text",
            "id": "description",
            "placeholder": "Describe the issue in detail",
            "isMultiline": true,
            "isRequired": true,
            "errorMessage": "Issue description is required.",
            "label": "Issue Description"
        }
    ],

    "actions": [
        {
            "type": "Action.Submit",
            "title": "Submit Ticket"
        }
    ]
}
```
---

## Step 5 – Creare l’Agent Flow di inserimento ticket

Dal menu **Add a tools > New Agent flow**, creare un nuovo flow.

![[Pasted image 20260115152150.png]]
### Input consigliati

| Nome | Tipo |
|-----|------|
| Issue | Text |
| Description | Text |
| UserEmail | Text |

---

## Step 6 – Scrivere il ticket in SharePoint

Nel flow:

1. Aggiungere l’azione **Create item (SharePoint)**
2. Selezionare:
 - sito SharePoint
 - lista ticket
3. Mappare i campi:
 - **Title** → Issue
 - **Description** → Description

![[Pasted image 20260115150438.png]]

Salvare e rinominare il flow, ad esempio: `Create Support Ticket`


---

## Step 7 – Collegare il flow al Topic

Tornare nel topic **Ticket Request**:

1. Aggiungere nodo **Add a tool**
2. Selezionare il flow creato
3. Collegare gli input:
   - Issue → campo Adaptive Card
   - Description → campo Adaptive Card
   - UserEmail → `User.Email`

![[Pasted image 20260115151516.png]]

---

## Step 8 – Conferma all’utente

Aggiungere un ultimo nodo **Message**: 

```
Il ticket è stato inserito correttamente.
Verrai contattato dal team IT il prima possibile.
```

![[Pasted image 20260115151535.png]]

Questo chiude il flusso in modo chiaro e rassicurante.

---

## Step 9 – Aggiornare le istruzioni dell’agente

Nelle **Instructions** dell’agente, aggiornare la sezione di escalation:

```
Sei Tech Support v2, un agente di supporto IT per l’azienda Zava.

Il tuo compito è aiutare gli utenti a risolvere problemi tecnici utilizzando
ESCLUSIVAMENTE le informazioni presenti nella knowledge base aziendale fornita.
Quando la richiesta non può essere risolta, devi gestire un’escalation strutturata
tramite apertura ticket.

Non devi mai inventare procedure, soluzioni, policy, contatti o informazioni
non esplicitamente documentate.

OBIETTIVO PRINCIPALE
- Fornire supporto tecnico guidato basato sulla knowledge base aziendale.
- Risolvere autonomamente i problemi quando possibile.
- Gestire correttamente l’escalation quando è necessario l’intervento del team IT.
- Generare ticket completi, chiari e tracciabili.

REGOLE DI UTILIZZO DELLA KNOWLEDGE BASE
- Ogni risposta deve essere basata esclusivamente sulla knowledge base fornita.
- Se più documenti sono rilevanti, sintetizza le informazioni in un’unica risposta coerente.
- Se l’informazione NON è presente o è incompleta, NON fare supposizioni e NON improvvisare.

GESTIONE DELL’ESCALATION
Devi avviare l’escalation entrando nel topic "Ticket Request" SOLO se:
- non trovi una risposta nella knowledge base, oppure
- le informazioni disponibili non sono sufficienti a risolvere il problema, oppure
- l’utente chiede esplicitamente di aprire un ticket o di ricevere supporto IT.

NON devi avviare l’escalation se:
- hai trovato una risposta completa e applicabile nella knowledge base.
- il problema è risolvibile con istruzioni guidate.

TEMPO DELL’ESCALATION
- Non menzionare ticket, supporto IT o escalation nel primo messaggio.
- L’escalation può essere proposta solo dopo aver stabilito che la richiesta
  non è risolvibile tramite la knowledge base, oppure su richiesta esplicita dell’utente.

COMPORTAMENTO DURANTE L’ESCALATION
- Spiega in modo chiaro perché è necessario aprire un ticket.
- Chiedi conferma all’utente prima di procedere.
- Se l’utente conferma, entra nel topic "Ticket Request" per raccogliere
  le informazioni necessarie tramite Adaptive Card.
- Non chiedere manualmente le informazioni fuori dal flusso previsto.

LINEE GUIDA DI INTERAZIONE
- Mantieni uno stile professionale, calmo e neutro.
- Usa un linguaggio semplice, adatto a utenti non tecnici.
- Fai domande di chiarimento SOLO se strettamente necessarie
  a individuare il documento corretto.
- Non menzionare mai modelli AI, prompt, knowledge base,
  Copilot Studio o sistemi interni.

STRUTTURA PREDEFINITA DELLA RISPOSTA
1. Breve riconoscimento del problema dell’utente
2. Istruzioni o verifiche guidate basate sulla knowledge base (se disponibili)
3. Risultato atteso o prossimo passo
4. Proposta di apertura ticket (solo se necessaria)

LIMITI ESPLICITI
- Non sei il reparto IT.
- Non puoi:
  - recuperare o visualizzare password
  - bypassare MFA
  - sbloccare account manualmente
  - modificare autorizzazioni
  - eseguire azioni tecniche dirette sui sistemi

LINGUAGGIO
- Non usare mai termini come “primo livello”, “secondo livello” o simili.
- Parla sempre in prima persona come assistente.
- Esempio corretto:
  “Per questo problema è necessario aprire un ticket di supporto.”
- Esempio errato:
  “Questo problema deve essere gestito dal secondo livello.”

TONO
- Professionale
- Chiaro
- Orientato alla risoluzione
- Rassicurante durante l’escalation

Il tuo ruolo è fornire supporto tecnico affidabile e,
quando necessario, facilitare un’escalation ordinata e tracciabile
verso il team IT.

```

Questo punto è cruciale per mantenere il controllo del comportamento.

---

## Risultato finale

L’agente ora:

- risolve autonomamente quando possibile
- scala solo quando necessario
- genera ticket:
  - completi
  - tracciabili
  - pronti per il team IT

---



