# Tech Support · v2 (Copilot Studio)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**

## Panoramica

Il supporto IT di primo livello non può risolvere ogni richiesta in autonomia.  
Problemi complessi, casi fuori knowledge base o richieste che richiedono **intervento umano** devono essere gestiti con un’escalation chiara, tracciabile e standardizzata.

**Tech Support (v2)** estende l’agente di primo livello introducendo una **gestione strutturata dell’escalation**, eliminando email informali, messaggi diretti o ticket incompleti.

## Problema

Nel supporto IT esiste una criticità strutturale ricorrente: **la maggior parte delle richieste potrebbe essere risolta rapidamente**, ma finisce comunque per congestionare il team IT.

Questo accade perché tutte le richieste seguono lo stesso percorso, indipendentemente dalla loro complessità. Attività semplici e già documentate vengono trattate come problemi critici, generando un effetto di “tappo” che rallenta l’intero servizio.

In particolare:

- molte richieste riguardano **procedure note e ripetitive**, risolvibili con poche istruzioni guidate
- l’assenza di un **filtro iniziale efficace** porta ogni richiesta a diventare un ticket, anche quando non necessario

Quando l’utente non trova subito una risposta, l’escalation avviene spesso in modo **prematuro e non strutturato**:

- apertura di ticket incompleti
- utilizzo di canali informali (email, messaggi diretti)
- mancanza di contesto tecnico utile

Il risultato complessivo è un supporto IT percepito come lento, non perché manchino le soluzioni, ma perché **le richieste non vengono filtrate prima di arrivare al team**.

In questo scenario, migliorare il supporto non significa rispondere più velocemente, ma **distinguere correttamente ciò che può essere risolto subito da ciò che richiede davvero un intervento umano**.

## Soluzione

**Tech Support (v2)** introduce la possibilità di **aprire ticket interagendo direttamente con gli strumenti aziendali**, in modo controllato e prevedibile.

L’agente segue una logica semplice: prova sempre a risolvere la richiesta usando la knowledge base, se la richiesta non è risolvibile, **non improvvisa** ma propone l’apertura di un ticket.
L’apertura del ticket non è manuale e non avviene via testo libero.

Quando l’utente conferma l’escalation:

1. L’agente raccoglie le informazioni tramite **Adaptive Card**, questo consenta di definire a priori i campi che caratterizzano un ticket (oggetto, descrizione, etc.)
2. I dati vengono passati dall'agente ad un tool dedicato chiamato **agent flow**
3. Il flow crea un nuovo elemento nel sistema ticketing interno. In questo esempio per semplicità è stata utilizzata una **SharePoint List**, ma è molto facile connettersi anche a servizi terze parti come *ServiceNow* o *Jira*.

In questo modo l’utente è guidato nella compilazione ed i ticket hanno sempre la struttura coerente che ci aspettiamo.

Questo approccio permette di:

- Agire da filtro, evitando l’apertura di ticket inutili
- Separare chiaramente la parte conversazione dell'agente, più libera, dalla logica di automazione ed integrazione con procedure aziendali che devono rimanere standard.

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
