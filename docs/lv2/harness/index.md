# Copilot Studio · Microsoft Harness

Questa sezione raccoglie gli agenti costruiti con il nuovo **harness** di Copilot Studio. Invece di modellare la conversazione con i *Topic*, l'agente è descritto da:

- **Istruzioni** in Markdown, con ruolo, regole e limiti;
- **Skill**: istruzioni strutturate (`SKILL.md`) con file di riferimento ed eventuali script Python eseguiti in sandbox;
- **Tool** e **Workflow**: azioni di connettore e Agent Flow che l'agente invoca;
- **Knowledge**: fonti di conoscenza, ad esempio SharePoint.

Gli use case sono gli stessi della sezione *Standard Harness*, ripensati con questo approccio.

## Agenti disponibili

### **Tech Support CH**
**Categorie**: IT, Ticketing

**Descrizione**: Assistente IT di primo livello che guida la diagnosi e, su richiesta, apre un ticket con la skill *Ticket Intake* e il workflow *Create New Ticket*.

➡️[Vai alla documentazione](tech-support/index.md)

### **Job Writer CH**
**Categorie**: Risorse Umane, Creazione contenuti

**Descrizione**: Prepara bozze di annunci di lavoro con la skill *job-posting-builder* e genera il documento Word con uno script Python in sandbox.

➡️[Vai alla documentazione](job-writer/index.md)

### **Postman CH**
**Categorie**: Universale, E-mail, Multi Agente

**Descrizione**: Invia via email un riepilogo HTML fedele della risposta finale, generato dalla skill *postman-email-recap* e spedito con il tool *Send Email Recap*.

➡️[Vai alla documentazione](postman/index.md)

### **Talent Scout CH**
**Categorie**: Risorse Umane, Screening CV

**Descrizione**: Confronta i CV dell'archivio SharePoint con criteri espliciti tramite la skill *CV Screening* e notifica il canale Teams con il workflow *Notify Teams Applicant channel*.

➡️[Vai alla documentazione](talent-scout/index.md)
