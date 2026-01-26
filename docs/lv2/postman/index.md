# Postman · v2 (Copilot Studio)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**

## Panoramica

Nel lavoro quotidiano, molte conversazioni avvengono in chat e portano a una risposta finale chiara e consolidata, che deve essere condivisa via email in modo formale e tracciabile.

Con **Postman (v1)** l’obiettivo era strutturare correttamente un contenuto già selezionato dall’utente, mantenendolo invariato e inserendolo nel corpo di una email standard.

**Postman (v2)** è progettato per operare in combinazione con altri agenti all’interno di un flusso orchestrato.  
In questo scenario, Postman riceve come input **l’intero storico della conversazione**, fornito da agenti a monte, e agisce **in modo trasparente e non intrusivo per l’utente**, senza richiedere alcuna attivazione esplicita.

L’agente opera quindi **in background**, come componente di un altro agent, individuando in autonomia la risposta finale più rilevante dell’assistente.

Una volta identificata, la risposta viene convertita in una **email HTML professionale** e inviata a un destinatario noto, senza interventi manuali da parte dell’utente.

Postman passa così da strumento di supporto alla formattazione a **meccanismo automatico di recap e inoltro delle risposte finali**, abilitato come agente connesso che lavora in modo silente all’interno di una catena multi-agente, riducendo ulteriormente il carico operativo per l’utente.

## Soluzione

**Postman (v2)** introduce un flusso **completamente automatizzato** per la generazione e l’invio di email di riepilogo a partire da una conversazione.
 
Riceve quindi **l’intera chat come input strutturato**, inclusa la cronologia completa degli scambi, ed esegue le proprie attività **in background**, senza interrompere o modificare l’esperienza conversazionale dell’utente.

Postman utilizza due strumenti distinti, con responsabilità chiaramente separate:

1. **Testo in HTML**  
   - Identifica la risposta più finale e autorevole dell’assistente all’interno dello storico della conversazione  
   - Trasforma quella risposta in un **HTML professionale**  
   - Non modifica né riassume ulteriormente il contenuto prodotto dallo strumento  

2. **Send Email Recap**  
   - Invia l’email di riepilogo al **destinatario**  
   - Compila l’oggetto con un **riassunto molto breve** del contenuto (massimo 8 parole)  
   - Inserisce nel corpo **esattamente l’HTML** generato dallo strumento precedente  

Questo approccio permette di:

- Mantenere l’esperienza utente invariata e priva di interazioni aggiuntive
- Eliminare qualsiasi selezione o copia manuale del contenuto
- Garantire che la risposta finale venga riportata integralmente e senza alterazioni
- Standardizzare il formato dell’email in HTML professionale
- Automatizzare completamente l’invio verso un destinatario predefinito

## Esempio di utilizzo

### Invio automatico del riepilogo finale

L’utente interagisce normalmente con l’assistente all’interno di una conversazione articolata, gestita da uno o più agenti, fino a ottenere una risposta finale completa.

**Richiesta utente**

`Inoltrami l'annuncio via mail`

![Esempio](assets/Postmanv2-Esempio.png)

!!! warning "Nota tecnica"
	Nel presente esempio l’agente è stato integrato con **Job Writer (v2)** al solo fine di dimostrarne il funzionamento. Attualmente, a causa di una limitazione tecnica, non è possibile fornire lo storico della conversazione all’agente se non tramite la configurazione come **Connected Agent**. Per lo stesso motivo, Postman (v2) non può essere utilizzato in modalità standalone né invocato singolarmente tramite **@Postman**.


**Comportamento dell’agente**

1. Riceve lo **storico completo della conversazione** dagli agenti a monte
2. Opera in modo **trasparente e silente** come connected agent
3. Identifica la risposta finale più rilevante dell’assistente
4. Genera il contenuto HTML professionale tramite lo strumento *Testo in HTML*
5. Crea un oggetto email sintetico e coerente con il contenuto
6. Invia automaticamente l’email di riepilogo al destinatario fisso tramite *Send Email Recap*

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**
