# Lab Guide (Onboarding Buddy · v1)

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
Onboarding Buddy (v1)
```

2. **Descrizione**:
```
Accompagna i neoassunti durante l'onboarding con checklist personalizzate, priorità chiare, contatti utili e risposte alle FAQ basate sulla documentazione aziendale. Adatta la guida a ruolo, sede, data di ingresso e fase del percorso, evidenziando scadenze, blocchi e prossime azioni.
```

3. **Istruzioni**:
```
# Ruolo
Sei **Onboarding Buddy**, la guida operativa per i neoassunti. Aiutali a orientarsi, completare le attività previste e trovare risposte affidabili nella documentazione aziendale.

# Linee guida
- Comunica in modo accogliente, chiaro e concreto.
- Personalizza le risposte in base a ruolo, reparto, sede, data di ingresso e fase di onboarding.
- Usa la documentazione aziendale disponibile come fonte principale per checklist, scadenze, procedure, FAQ e contatti.
- Se le informazioni necessarie mancano, chiedi solo i dettagli indispensabili.
- Se una risposta non è documentata, dichiaralo chiaramente e indica chi o quale team può confermarla, quando disponibile.
- Distingui sempre attività obbligatorie, consigliate e bloccate.
- Non inventare contatti, responsabilità, scadenze o policy.

# Skill disponibili
- Quando il neoassunto chiede una checklist, contatti utili, FAQ o una guida sul proprio percorso, esegui la skill `onboarding-guidance`.

# Gestione della conversazione
- Mantieni il focus sulle prossime azioni concrete.
- Presenta checklist leggibili con stato, priorità e scadenza quando documentati.
- Evidenzia dipendenze e blocchi, suggerendo il percorso di escalation previsto.
- Concludi con le tre azioni più importanti da completare e proponi di aggiornare la checklist in base ai progressi.
```

!!! tip "Le istruzioni sono importanti"
	In questi semplici agenti **tutto il comportamento è dettato dalle istruzioni**. Chiedere all'agente di chiudere ogni risposta con le **tre azioni prioritarie** guida il neoassunto, che spesso non sa ancora cosa fare o cosa chiedere.

## Aggiungere la base di conoscenza

La base di conoscenza di Onboarding Buddy è il **sito SharePoint di Onboarding**, che raccoglie checklist, procedure, FAQ e contatti utili per i neoassunti. Utilizzare SharePoint garantisce che:

- ogni aggiornamento della documentazione sia immediatamente disponibile per l'agente;
- l'agente **rispetti i permessi esistenti** (un utente riceve risposte solo da documenti a cui ha accesso).

Per collegare la documentazione:

1) Navigare nel sito SharePoint **Onboarding** e copiare l'URL del sito o della raccolta documenti.

2) Incollare l'URL nella box **Knowledge** dell'agente, premere *Invio* e verificare che venga riconosciuto il nome del sito o della raccolta:

![Step 02](../tech-support/assets/ts-lg-5.webp)

??? tip "Contenuti consigliati per il sito Onboarding"
	Se non si dispone di documentazione reale, è possibile creare alcuni documenti di esempio (anche con l'aiuto di Copilot):

	- `Checklist Onboarding.docx` – attività suddivise per fase (prima dell'ingresso, primo giorno, prima settimana, primo mese)
	- `Contatti Utili.xlsx` – tabella con ambito, ufficio/referente, e-mail o canale Teams
	- `FAQ Neoassunti.docx` – domande e risposte su accessi, dispositivi, orari, buoni pasto, formazione obbligatoria
	- `Benvenuto in Azienda.pdf` – presentazione dell'azienda, valori e organizzazione

	Documenti con titoli chiari, scadenze e referenti espliciti migliorano sensibilmente la qualità delle checklist generate.

!!! info "Requisiti di licenza"
	Senza licenza `Microsoft 365 Copilot` non è possibile utilizzare SharePoint o file caricati come knowledge: sarà disponibile solo l'inserimento di URL pubblici.

## Skills

Per rendere le risposte ancora più strutturate, è possibile aggiungere all'agente una **skill**: un pacchetto riutilizzabile di istruzioni che l'agente attiva automaticamente quando la richiesta dell'utente corrisponde alla sua descrizione.

La skill **onboarding-guidance** guida il neoassunto in un percorso coerente:

1. Individua fase dell'onboarding, ruolo, sede e obiettivo immediato
2. Cerca nella documentazione checklist, policy, scadenze, sistemi e contatti applicabili
3. Costruisce una checklist per fasi (prima dell'ingresso, primo giorno, prima settimana, primo mese, traguardi successivi)
4. Per ogni attività indica azione, scadenza, responsabile e fonte, segnalando ciò che va confermato
5. Risponde alle FAQ distinguendo i fatti documentati dai suggerimenti pratici
6. Fornisce solo contatti documentati, spiegando perché contattarli e cosa includere nella richiesta
7. Verifica che attività obbligatorie, accessi, dipendenze e formazione siano coperti, evidenziando i blocchi
8. Chiude con le tre azioni prioritarie e propone di aggiornare la checklist

È possibile scaricare la skill premendo il link sottostante:

-> [Scarica la skill (ZIP)](../../downloads/onboarding-buddy/onboarding-guidance.zip)

Per aggiungerla all'agente:

1. Nella scheda **Configura** dell'agente espandere la sezione **Skills** e premere **Aggiungi**.
2. Caricare il file `.zip` **così com'è**, senza estrarlo: il pacchetto deve contenere il file `SKILL.md`.
3. Verificare nome, descrizione e istruzioni della skill mostrati nel riepilogo. Una volta caricata, la skill **onboarding-guidance** compare nella sezione **Skills**.
4. Provare nel pannello di anteprima una domanda che dovrebbe attivare la skill, ad esempio `Prepara la mia checklist di onboarding`.

!!! warning "Funzionalità in anteprima"
	Le skill in Agent Builder sono in **anteprima** e sono disponibili solo per le organizzazioni iscritte al **Microsoft Frontier Program**. Senza questa abilitazione la sezione **Skills** non è visibile: l'agente funziona comunque, basandosi solo sulle istruzioni. Per maggiori informazioni, consultare la [documentazione ufficiale](https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder-add-skills).

??? tip "Istruzioni o skill?"
	Le **istruzioni** definiscono il comportamento generale dell'agente (ruolo, perimetro, tono), mentre la **skill** contiene il procedimento dettagliato per uno specifico compito. Separare le due parti mantiene le istruzioni brevi e rende la skill riutilizzabile anche in altri agenti.

## Prompt suggeriti

Nella sezione finale della configurazione premere `Add a suggested prompt` e inserire i seguenti dati:

| Title | Message |
|---|---|
| `Crea la mia checklist` | `Prepara la mia checklist di onboarding personalizzata per ruolo, sede e data di ingresso.` |
| `Priorità prima settimana` | `Quali attività devo completare nella mia prima settimana e in quale ordine?` |
| `Trova il contatto giusto` | `Indicami chi contattare per accessi, dispositivi, formazione obbligatoria e supporto HR.` |
| `Rispondi a una FAQ` | `Rispondi alle mie domande di onboarding usando la documentazione aziendale disponibile.` |
| `Verifica i miei progressi` | `Aiutami a controllare cosa ho completato, cosa manca e quali blocchi devo risolvere.` |

## Test e condivisione

L'agente a questo punto sarà pienamente funzionante e sarà possibile testarlo nel pannello **Agent preview** a destra delle configurazioni, oppure dentro la Copilot Chat dopo aver premuto il tasto **Crea** in alto a destra.

Verificare in particolare che:

- le checklist distinguano attività obbligatorie, consigliate e bloccate;
- ogni risposta si chiuda con le tre azioni prioritarie;
- una domanda non coperta dalla documentazione produca una risposta di "informazione non documentata" e non un'invenzione.

??? tip "Condividere gli agenti"
	Una volta creato un agente questo sarà disponibile per l'utilizzo solamente per chi lo ha realizzato. Per condividerlo a colleghi occorre premere in alto a destra il tasto **Condividi** e scegliere specifici utenti, come se si stesse condividendo una cartella di OneDrive. La pubblicazione verso tutta l'azienda invece richiede l'approvazione dell'amministratore di sistema e potrebbe essere stata disabilitata. Per maggiori informazioni, consultare la [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents).
