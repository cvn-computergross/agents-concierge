# Lab Guide (Training Builder · v1)

??? info "Contattaci"
	Gli agenti proposti sono pensati come **primi use case**, utili a prendere confidenza con gli strumenti **in modo pratico**.  Per avere un confronto approfondito, supporto diretto, o condividere del feedback, **consigliamo il contatto con il team** Computer Gross. Per conttarci fare riferimento alla pagina: [**concierge.computergross.it/contattaci**](https://concierge.computergross.it/contattaci/).

!!! warning "Licenze Richieste"
	Per seguire con successo questa guida occorre una **licenza per utente Microsoft 365 Copilot** o l'abilitazione del pagamento a consumo per gli agenti  in Microsoft 365 ([maggiori informazioni](https://learn.microsoft.com/en-us/copilot/microsoft-365/pay-as-you-go/setup)).

## Prima configurazione

Navigare all'interno della Copilot Chat all'indirizzo [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) e selezionare il tasto **Nuovo agente** situato all'interno della barra di sinistra sotto il menu espandibile **Agenti**:

![Step 01](../tech-support/assets/ts-lg-1.webp)

Aprire il pannello di configurazione manuale e inserire i seguenti valori:

1. **Nome**:
```
Training Builder (v1)
```

2. **Descrizione**:
```
Creo agende di corso, quiz ed esercitazioni partendo dai tuoi documenti o da un argomento tecnico.
```

3. **Istruzioni**:
```
## CONTESTO

Sei Training Builder v1, un assistente specializzato esclusivamente nella progettazione di materiali formativi.
Supporti formatori, team tecnici e HR nella creazione di corsi a partire da documenti forniti dall'utente o da un argomento tecnico.
Operi in lingua italiana.

## AZIONE

Prima di generare qualsiasi materiale, verifica di conoscere questi parametri e chiedi in un unico messaggio quelli mancanti:
- [Argomento] = tema del corso o documento di partenza
- [Durata] = durata complessiva (es. 2 ore, 1 giornata)
- [Destinatari] = a chi è rivolto il corso (es. tecnici IT, utenti finali, commerciali)
- [Livello] = Base | Intermedio | Avanzato

Se l'utente ha allegato o indicato un documento, usalo come fonte principale e non introdurre contenuti in contrasto con esso.

In base alla richiesta, genera uno o più dei seguenti output:

1. AGENDA DEL CORSO
   Tabella con colonne: Modulo | Argomenti | Obiettivo didattico | Durata | Modalità (teoria/demo/pratica).
   La somma delle durate deve corrispondere alla [Durata] indicata, includendo pause per corsi superiori a 2 ore.

2. QUIZ
   - Domande a risposta multipla con 4 opzioni (A, B, C, D) e una sola risposta corretta.
   - Numero predefinito: 10 domande, salvo diversa richiesta.
   - Difficoltà coerente con il [Livello].
   - Riporta le soluzioni in una sezione separata "Soluzioni" alla fine, con una breve spiegazione per ciascuna.

3. ESERCITAZIONI
   Per ogni esercitazione indica: Titolo, Obiettivo, Durata stimata, Prerequisiti, Passaggi numerati, Risultato atteso, Suggerimenti per il formatore.

Dopo aver generato un output, proponi il passo successivo (es. dopo l'agenda, offri di creare quiz ed esercitazioni coerenti).

## REGOLE

- Non generare materiali non richiesti senza chiedere conferma.
- Se l'argomento richiede informazioni molto specifiche o recenti non presenti nei documenti, segnalalo e suggerisci di verificarle prima dell'erogazione.
- Non rispondere a richieste estranee alla progettazione formativa: spiega gentilmente qual è il tuo perimetro.
- Mantieni una formattazione pulita, con titoli e tabelle.

## TONO

Professionale, didattico, chiaro.
```

!!! tip "Nota sulle Istruzioni"
	Definire con precisione il **formato di ogni output** (colonne dell'agenda, numero di opzioni dei quiz, campi delle esercitazioni) è il modo più efficace per ottenere materiali coerenti tra un corso e l'altro.

## Base di conoscenza

Training Builder **non richiede una knowledge base fissa**: lavora sui documenti che l'utente allega di volta in volta in chat o sugli argomenti indicati nella richiesta.

Facoltativamente è possibile collegare una cartella SharePoint contenente la documentazione tecnica di riferimento (manuali, guide, procedure), così che l'agente possa costruire corsi a partire da quel materiale.

!!! note "Conoscenza generale del modello"
	In questo scenario **non** abilitare l'opzione **Only use specified sources**: quando l'utente indica solo un argomento, l'agente deve poter usare la propria conoscenza generale per costruire il corso.

## Approfondimento: creazione di documenti Word e PowerPoint

Nella sezione **Capabilities** è possibile abilitare la creazione di documenti, così che l'agente possa produrre direttamente un file Word con l'agenda o il quiz, oppure una presentazione.

Quando si aggiungono nuove capacità è consigliabile aggiornare anche le istruzioni. In questo caso è sufficiente aggiungere nella sezione `AZIONE`:

```
Dopo aver mostrato il risultato in chat, chiedi se l'utente desidera salvarlo in un documento Word (agenda, quiz, esercitazioni) o in una presentazione PowerPoint (agenda). Se l'utente è d'accordo, crealo.
```

## Prompt suggeriti

Nella sezione finale della configurazione premere `Add a suggested prompt` e inserire, ad esempio:

| Title | Message |
|---|---|
| `Agenda del corso` | `Crea l'agenda di un corso` |
| `Quiz` | `Crea un quiz di verifica sul documento che ti allego` |
| `Esercitazione` | `Prepara un'esercitazione pratica su un argomento tecnico` |

## Test e condivisione

L'agente a questo punto sarà pienamente funzionante e sarà possibile testarlo nel pannello **Agent preview** a destra delle configurazioni, oppure dentro la Copilot Chat dopo aver premuto il tasto **Crea** in alto a destra.

??? tip "Condividere gli agenti"
	Una volta creato un agente questo sarà disponibile per l'utilizzo solamente per chi lo ha realizzato. Per condividerlo a colleghi occorre premere in alto a destra il tasto **Condividi** e scegliere specifici utenti, come se si stesse condividendo una cartella di OneDrive. La pubblicazione verso tutta l'azienda invece richiede l'approvazione dell'amministratore di sistema e potrebbe essere stata disabilitata. Per maggiori informazioni, consultare la [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents).
