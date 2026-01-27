# Postman · v1 (Agent Builder)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**

## Panoramica

Nel lavoro quotidiano, gli utenti si affidano sempre più a Copilot per ottenere informazioni, generare contenuti, riepilogare riunioni o produrre testi. Tuttavia, nella maggior parte dei casi, il risultato di queste interazioni deve poi essere trasferito dentro una email, che rimane lo strumento principale per comunicare in modo formale, condividere decisioni o rispondere a richieste interne ed esterne.

Nella maggior parte dei casi, però, agli utenti non serve una riscrittura o un’interpretazione del contenuto: hanno già il testo corretto e devono solo incapsularlo in una email strutturata, pulita e pronta da inviare.

## Problema

È proprio in questo passaggio, dal risultato di Copilot al corpo di una mail, che emergono le maggiori frizioni: formattazioni che si perdono nel copia‑incolla, rientri da sistemare, liste che si sfaldano, oppure la necessità di reintrodurre manualmente una struttura formale (saluti, firma, etc.).

Nella maggior parte dei casi, però, agli utenti non serve una riscrittura o un’interpretazione del contenuto: hanno già il testo corretto e devono solo incapsularlo in una email strutturata, pulita e pronta da inviare. Abbiamo identificato tre criticità principali nella preparazione delle email:

- **Rielaborazione manuale del contenuto** : Il testo deve essere copiato dalla chat di Copilot e adattato manualmente nel corpo della mail.
- **Rischio di alterazione delle informazioni** : Durante la riscrittura possono essere introdotte modifiche non intenzionali.
- **Struttura non uniforme** : Introduzione e chiusura delle email variano in base all’utente o al momento.

## Soluzione

![Chat](assets/Postmanv1-Chat.png)

**Postman (v1)** è un semplice agente progettato **per creare il corpo delle email**, **riportando in modo invariato il contenuto specificato dall’utente** e aggiungendo una struttura formale standard.

L’agente:

- Non modifica, riassume o rielabora il contenuto principale  
- Inserisce il testo esattamente come trovato dopo la chiamata dall’utente  
- Genera una breve introduzione coerente con il contesto del contenuto  
- Aggiunge una chiusura di email formale e neutra  

Questo approccio permette di:

- Garantire l’integrità delle informazioni  
- Ridurre il tempo necessario per preparare una email  
- Standardizzare introduzione e chiusura delle comunicazioni  


## Esempio di utilizzo

### Creazione del corpo di una email

**Richiesta utente**

`Crea la mail utilizzando l'intera ricerca sugli agenti id qui sopra`

`Prendi dal titolo "che cos'è un Agent ID?" fino alla fine di "In sintesi"`

**Comportamento dell’agente**

![Esempio1](assets/Postmanv1-Esempio1.png)

Se la richiesta è troppo generica l'agente chiede di specificare l'esatto contenuto richiesto.

1. Acquisisce il contenuto fornito dall’utente  
2. Identifica il contesto generale della comunicazione  
3. Inserisce una breve introduzione tipica di una email  
4. Riporta il contenuto in modo invariato  
5. Aggiunge una chiusura formale standard  

![Esempio3](assets/Postmanv1-Esempio3.png)
![Esempio2](assets/Postmanv1-Esempio2.png)

!!! info "Personalizzazioni"
    Lo stile della risposta può essere personalizzato secondo esigenze, ad esempio filtrare i contenuti iniziali eliminando le emoji o prevedendo due versioni italiano e inglese.

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**
