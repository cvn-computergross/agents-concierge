# Copilot Studio · Livello 2

Questa sezione raccoglie gli agenti di **livello 2** sviluppati tramite **Copilot Studio**, la piattaforma no-code/low-code di Microsoft progettata per creare, estendere e orchestrare agenti conversazionali più avanzati all’interno dell’ecosistema Microsoft 365 Copilot ed oltre.

Copilot Studio consente di superare i limiti degli agenti più semplici, introducendo maggiore controllo sul comportamento dell’agente, sulla gestione delle conversazioni e sull’integrazione con sistemi esterni.
È pensato per scenari in cui è necessario modellare flussi più articolati, combinare capacità diverse o gestire logiche decisionali più complesse.

!!! info "Per maggiori informazioni"
	Per una panoramica completa di Copilot Studio, delle sue funzionalità e degli scenari supportati, fare riferimento alla [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio).

## Agenti disponibili

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
- **[Postman · v2](postman/index.md)**
