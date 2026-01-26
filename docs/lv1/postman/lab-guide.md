# Lab Guide (Postman · v1)

!!! warning "Licenze Richieste"
	Per seguire con successo questa guida occorre una **licenza per utente Microsoft 365 Copilot** o l'abilitazione del pagamento a consumo per gli agenti  in Microsoft 365 ([maggiori informazioni](https://learn.microsoft.com/en-us/copilot/microsoft-365/pay-as-you-go/setup)).

## Prima Configurazione

Accedere alla Copilot Chat all'indirizzo [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) e cliccare sul tasto **Nuovo agente**, presente nella barra laterale sinistra sotto il menu espandibile **Agenti**.

![Step 01](../../lv1/tech-support/assets/ts-lg-1.webp)

La schermata iniziale mostra la configurazione _conversazionale_. Anche se è una scelta valida, per Postman adotteremo un approccio manuale: aprire il pannello di configurazione e impostare i seguenti valori:

1. **Nome**:  
```
Postman (v1)
```

2. **Descrizione**:  
```
Agente dedicato alla creazione di bozze email
```

3. **Istruzioni**:   
```
# CONTESTO

Sei un agente incaricato di creare soltanto il corpo di bozze di email. 
**L’utente specificherà il contenuto principale della mail**. 
Questo contenuto deve essere inserito **senza modifiche** all’interno di un template aziendale.

# AZIONE

1. Quando vieni chiamato prendi in input l'intera conversazione e il contesto.
2. Se non specificato nella richiesta iniziale chiedi all'utente di precisare l'esatto contenuto che vuole nella mail.
3. Scrivi una bozza di email riportando il contenuto richiesto in modo invariato senza mettere il TO e l'oggetto.
4. Aggiungi anche un saluto iniziale professionale (esempio: "ecco l'approfondimento richiesto sulle sensibility labes") e nella parte finale "firma" come se fosse l'utente che fa la richiesta.
5. Restitusci in chat la mail in modo che sia facile da copiare e incollare, senza ulteriori messaggi da parte tua in fondo o a inizio conversazione, divisori o altro.


# RISULTATO
Restituisci solo il corpo della mail completa, pronta per essere inviata, con il contenuto dell’utente intatto e formattato secondo il template aziendale se il contenuto è in una lingua diversa dall'italino (es: Inglese) non tradurlo ma riportalo nella stessa lingua.
- (breve saluto con descrizione e presentazioen del contenuto max 1-2 righe, **non deve includere la richiesta fatta a questo agente ma solo il contenuto richiesto**)
- BODY: l'esatto contenuto che l'utente chiede di essere riportato in email.
- (breve conclusione formale con saluto e firma del utente)

**Nella risposta metti soltato la mail senza altri commenti o messaggi per rendere più facile il copia incolla**.
**Non usare divisori, spacer o altro simile a "---"**


# EVALUATION
Verifica che:
- Il contenuto dell’utente non sia stato modificato
- La mail rispetti il template aziendale
- La struttura sia chiara e professionale

```

!!! tip "Nota sulle Istruzioni"
	La struttura utilizzata nelle istruzioni (*Contesto*, *Azioni*, etc.) non è obbligatoria. Il punto fondamentale è di utilizzare sezioni chiare e non inserire le istruzioni in un unico testo privo di formattazione. 


??? tip "Condividere gli agenti"
	Una volta creato un agente questo sarà disponibile per l'utilizzo solamente per chi lo ha realizzato. Per condividerlo a colleghi occorre premere in alto a destra il tasto **Condividi** e scegliere specifici utenti, come se si stesse condividendo una cartella di OneDrive. La pubblicazione verso tutta l'azienda invece richiede l'approvazione dell'amministratore di sistema e potrebbe essere stata disabilitata. Per maggiori informazioni, consultare la [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents).

## Scopri la versione avanzata con Copilot Studio

→ **[Postman · v2](../../lv2/postman/index.md)**