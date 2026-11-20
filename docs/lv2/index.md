# Copilot Studio · Livello 2

Questa sezione raccoglie gli agenti di **livello 2** sviluppati tramite **Copilot Studio**, la piattaforma no-code/low-code di Microsoft progettata per creare, estendere e orchestrare agenti conversazionali più avanzati all’interno dell’ecosistema Microsoft 365 Copilot ed oltre.

Copilot Studio consente di superare i limiti degli agenti più semplici, introducendo maggiore controllo sul comportamento dell’agente, sulla gestione delle conversazioni e sull’integrazione con sistemi esterni.
È pensato per scenari in cui è necessario modellare flussi più articolati, combinare capacità diverse o gestire logiche decisionali più complesse.

!!! info "Per maggiori informazioni"
	Per una panoramica completa di Copilot Studio, delle sue funzionalità e degli scenari supportati, fare riferimento alla [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio).

## Standard Harness

Gli agenti presentati in questa sezione propongono una **versione evoluta** degli use case introdotti nel livello 1. L’obiettivo è mostrare come uno stesso caso d’uso possa essere ripensato utilizzando strumenti più avanzati, pattern di progettazione più strutturati e un maggiore livello di controllo, al costo di maggiore tempo di implementazione e testing.

!!! note "Nota editoriale"
	Anche in questo caso, gli agenti di livello 2 sono progettati come unità funzionali ben definite, facilmente riutilizzabili e componibili.  Pur rappresentando singoli use case, costituiscono ottimi **punti di partenza per architetture multi-agent**, in cui agenti specializzati collaborano o vengono orchestrati per coprire scenari complessi. Per saperne di più, contattateci.

### **Job Writer · v2**  
**Categorie**: Risorse Umane, Creazione contenuti

**Descrizione**: Redige il contenuto desiderato (annuncio di lavoro) con grande grado di controllo utilizzando i *Topics* per raccogliere gli input richiesti ed elaborandoli in maniera precisa grazie ad una *Prompt Action*. In grado di produrre i contenuti con Microsoft Word grazie all'omonimo *MCP Server*.

➡️[Vai alla documentazione](job-writer/index.md)

### **Tech Support · v2**
**Categorie**: Risorse Umane, Creazione contenuti

**Descrizione**: Gestisce in maniera più precisa l'escalation, guidando l'utente all'apertura del ticket tramite Adaptive Card all'interno della chat, seguito dall'utilizzo di un *Agent Flow* per scrivere le informazioni nel portale di supporto interno.
	
➡️[Vai alla documentazione](tech-support/index.md)

### **Postman · v2**
**Categorie**: Universale, E-mail, Multi Agente

**Descrizione**: Postman (v2) è un "plug-in" per ogni altro agente: introduce un flusso completamente automatizzato per la generazione e l’invio di email di riepilogo dall'alto valore grafico (immagini, collegamenti, etc.) a partire da una conversazione.
	
➡️[Vai alla documentazione](postman/index.md)

### **Talent Scout · v2**
**Categorie**: Autonomo, Interazione Email, Risorse Umane

**Descrizione**: Talent Scout (v2) è un agente per lo screening dei candidati che automatizza ricerca, analisi dei CV e gestione delle nuove candidature, archiviandole in modo strutturato e notificando il team HR in tempo reale.
	
➡️[Vai alla documentazione](talent-scout/index.md)

### **Planner Buddy**
**Categorie**: Pianificazione operativa, Collaborazione, Task Management

**Descrizione**: Un agente AI dedicato a Planner, organizza attività e piani di lavoro in modo intelligente.
Aggiorna automaticamente lo stato dei task e ottimizza la distribuzione delle attività.
Supporta team e utenti nel mantenere ordine, priorità e avanzamento dei progetti.
	
➡️[Vai alla documentazione](planner-buddy/index.md)

### **Agenda Pilot**
**Categorie**: Calendar, Scheduling automatizzato

**Descrizione**: Un agente AI per la gestione dei calendari analizza impegni, priorità e disponibilità.
Propone automaticamente le fasce orarie migliori e risolve eventuali conflitti.
Supporta la produttività adattandosi alle abitudini dell’utente e integrandosi con altri strumenti.

➡️[Vai alla documentazione](agenda-pilot/index.md)
- **[Maps Agent · v2](maps-agent/index.md)**

### **Assistente Trasferte Zava**
**Categorie**: Amministrazione, Note spese, Document Intelligence

**Descrizione**: Un agente per trasferte e note spese dei dipendenti: apre le trasferte tramite Adaptive Card, le elenca leggendo i dati da *Dataverse* e registra le spese partendo dalla foto dello scontrino, analizzata con *Azure AI Document Intelligence* (Microsoft Foundry) tramite *Agent Flow*.

➡️[Vai alla documentazione](trasferte-zava/index.md)

## Microsoft Harness

### **Tech Support CH**
**Categorie**: IT, Ticketing

**Descrizione**: Assistente IT di primo livello che guida la diagnosi e, su richiesta, apre un ticket con la skill *Ticket Intake* e il workflow *Create New Ticket*.

➡️[Vai alla documentazione](harness/tech-support/index.md)

### **Job Writer CH**
**Categorie**: Risorse Umane, Creazione contenuti

**Descrizione**: Prepara bozze di annunci di lavoro con la skill *job-posting-builder* e genera il documento Word con uno script Python in sandbox.

➡️[Vai alla documentazione](harness/job-writer/index.md)

### **Postman CH**
**Categorie**: Universale, E-mail, Multi Agente

**Descrizione**: Invia via email un riepilogo HTML fedele della risposta finale, generato dalla skill *postman-email-recap* e spedito con il tool *Send Email Recap*.

➡️[Vai alla documentazione](harness/postman/index.md)

### **Talent Scout CH**
**Categorie**: Risorse Umane, Screening CV

**Descrizione**: Confronta i CV dell'archivio SharePoint con criteri espliciti tramite la skill *CV Screening* e notifica il canale Teams con il workflow *Notify Teams Applicant channel*.

➡️[Vai alla documentazione](harness/talent-scout/index.md)
