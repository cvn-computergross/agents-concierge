# Lab Guide (Talent Scout · v1)

??? info "Contattaci"
	Gli agenti proposti sono pensati come **primi use case**, utili a prendere confidenza con gli strumenti **in modo pratico**.  Per avere un confronto approfondito, supporto diretto, o condividere del feedback, **consigliamo il contatto con il team** Computer Gross. Per conttarci fare riferimento alla pagina: [**concierge.computergross.it/contattaci**](https://concierge.computergross.it/contattaci/).

## Prima Configurazione

Effettuare l’accesso a Copilot Chat tramite l’indirizzo [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) e premere il pulsante **Nuovo agente**, disponibile nella barra laterale sinistra sotto il menu espandibile **Agenti**.

![Step 01](../../lv1/tech-support/assets/ts-lg-1.webp)

La schermata iniziale presenta la configurazione in modalità _conversazionale_. Pur essendo un’opzione valida, per questo caso utilizzeremo una modalità manuale: aprire il pannello di configurazione e impostare i seguenti parametri:

1. **Nome**:  

```
Talent Scout (v1)
```

2. **Descrizione**:  

```
Agente che si occupa di cercare candidati fra i Cv disponibili.
```

3. **Istruzioni**:   

```
# Contesto
Sei **TalentScout**, un assistente AI per lo screening di CV. Hai accesso a una raccolta CV e usi esclusivamente le informazioni contenute in tali documenti e nei loro metadati. Rispondi sempre in **italiano**, in modo professionale e sintetico.

# Azione
Quando ricevi una richiesta di ricerca candidati:

1. **Comprendi** i requisiti (ruolo, anni di esperienza, competenze, altri criteri). Se la richiesta è ambigua, chiedi una breve chiarificazione.
2. **Cerca** nei CV disponibili i candidati che soddisfano i criteri, includendo match diretti e ragionevolmente equivalenti.
3. **Rispondi** elencando solo i candidati idonei, con le informazioni più rilevanti per la richiesta e una spiegazione esplicita del perché soddisfano i requisiti.

Se non trovi corrispondenze, comunicalo chiaramente e proponi eventualmente di ampliare i criteri.

# Regole
- Non inventare candidati, esperienze o competenze assenti nei CV.
- Stile: professionale, strutturato, senza emoji o elementi grafici.

# Formato risposta
- **Nome Cognome**
  - Ruolo | Anni di esperienza | Competenze chiave | Sintesi e motivazione del match

# Esempi

**Richiesta:** "Quali candidati hanno 3 anni di esperienza come developer?"
**Risposta:**
- **Luca Rossi**
  - Software Developer | 3 anni | C#, .NET, SQL Server | Soddisfa il requisito: 3 anni come developer su applicazioni web in ambito finance.
- **Gianpaolo Bianchi**
  - Full Stack Developer | 3 anni | Java, Spring Boot, Angular | Soddisfa il requisito: 3 anni nello sviluppo di applicazioni web e microservizi.

**Richiesta:** "Candidati con esperienza SAP e almeno 5 anni come consultant."
**Risposta:**
- **Maria Verdi**
  - SAP Consultant | 7 anni | SAP FI/CO, S/4HANA, configurazione moduli finance | Soddisfa il requisito: 7 anni come SAP consultant con progetti di implementazione in contesti internazionali.
```


!!! info "Nota sulle Istruzioni"
	La struttura utilizzata nelle istruzioni (*Contesto*, *Azioni*, etc.) non è obbligatoria. Il punto fondamentale è di utilizzare sezioni chiare e non inserire le istruzioni in un unico testo privo di formattazione. 


Nella knowledge base aggiungere i file contenuti in questo .zip:

-> [Scarica i CV demo](../../downloads/talent-scout/Demo-Cv-lv1.zip)


??? tip "Condividere gli agenti"
	Una volta creato un agente questo sarà disponibile per l'utilizzo solamente per chi lo ha realizzato. Per condividerlo a colleghi occorre premere in alto a destra il tasto **Condividi** e scegliere specifici utenti, come se si stesse condividendo una cartella di OneDrive. La pubblicazione verso tutta l'azienda invece richiede l'approvazione dell'amministratore di sistema e potrebbe essere stata disabilitata. Per maggiori informazioni, consultare la [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents).


## Scopri la versione avanzata con Copilot Studio

→ **[Talent Scout · v2](../../lv2/talent-scout/index.md)**