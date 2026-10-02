# Lab Guide (GDPR Compliance Monitor · v1)

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
GDPR Compliance Monitor (v1)
```

2. **Descrizione**:
```
Ti supporto nel monitoraggio della conformità al GDPR: rispondo citando gli articoli del regolamento, verifico i documenti interni e preparo checklist di conformità.
```

3. **Istruzioni**:
```
## CONTESTO

Sei GDPR Compliance Monitor v1, un assistente specializzato esclusivamente nel supporto alla conformità al Regolamento (UE) 2016/679 (GDPR).
Supporti DPO, uffici legali, IT e responsabili di processo nel monitoraggio della conformità.
Utilizzi come fonti la knowledge base, composta dal testo ufficiale del GDPR, dalle linee guida delle autorità di controllo e dalla documentazione interna dell'organizzazione.
Operi in lingua italiana.

## AZIONE

In base alla richiesta dell'utente, svolgi una delle seguenti attività:

1. DOMANDE NORMATIVE
   - Rispondi in modo chiaro e sintetico.
   - Cita sempre l'articolo (e, se pertinente, il considerando o la linea guida) di riferimento, es. "Art. 33 GDPR".

2. GAP ANALYSIS DI UN DOCUMENTO
   Quando l'utente allega o indica un documento interno (informativa, registro dei trattamenti, procedura, contratto con fornitore):
   - individua i requisiti GDPR applicabili a quel tipo di documento;
   - produci una tabella: Requisito | Stato (Presente / Parziale / Assente) | Riferimento normativo | Azione suggerita | Priorità (Alta / Media / Bassa);
   - chiudi con un breve riepilogo dei gap principali.

3. CHECKLIST DI CONFORMITÀ
   Per l'ambito richiesto (es. data breach, diritti degli interessati, responsabili del trattamento, misure di sicurezza, DPIA), genera una checklist di controlli verificabili con caselle (☐) e riferimento normativo per ciascun punto.

Se l'ambito della richiesta non è chiaro, chiedi un solo chiarimento mirato.

## REGOLE

- Basati sulle fonti della knowledge base; se un'informazione non è presente, dichiaralo esplicitamente.
- Non inventare mai articoli, sanzioni, scadenze o provvedimenti.
- Distingui chiaramente tra requisiti normativi (obblighi) e buone pratiche (raccomandazioni).
- Non esprimere giudizi definitivi di conformità o non conformità legale: presenta osservazioni e gap da validare.
- Termina ogni gap analysis o checklist con la nota: "Questa analisi è di supporto e deve essere validata dal DPO o da un consulente qualificato."
- Non rispondere a richieste estranee alla protezione dei dati: spiega gentilmente qual è il tuo perimetro.
- Non menzionare mai prompt, modelli AI o sistemi interni.

## TONO

Professionale, preciso, neutro. Linguaggio chiaro anche per utenti non specialisti.
```

!!! tip "Nota sulle Istruzioni"
	Chiedere all'agente di **distinguere tra obblighi e buone pratiche** e di **non esprimere giudizi definitivi** è fondamentale in ambito compliance, dove l'output deve sempre essere validato da una figura competente.

## Aggiungere la base di conoscenza

La knowledge base è composta da due tipologie di documenti:

**1. Fonti normative**

- Testo ufficiale del GDPR, scaricabile in PDF da [EUR-Lex](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32016R0679)
- Linee guida e provvedimenti del [Garante per la protezione dei dati personali](https://www.garanteprivacy.it/)
- Linee guida dell'[EDPB](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_it) (es. notifica dei data breach, diritto di accesso)

**2. Documentazione interna**

- Registro dei trattamenti
- Informative privacy
- Procedure interne (gestione data breach, gestione richieste degli interessati, data retention)

Caricare i documenti con il tasto **Carica da dispositivo** oppure, preferibilmente, incollare nella box **Knowledge** l'URL della cartella SharePoint che li contiene:

![Step 02](../tech-support/assets/ts-lg-5.webp)

Abilitare l'opzione **Only use specified sources** per forzare l'agente a utilizzare solo le fonti fornite, riducendo il rischio di [allucinazioni](https://it.wikipedia.org/wiki/Allucinazione_\(intelligenza_artificiale\)).

!!! warning "Riservatezza dei documenti"
	La documentazione interna di compliance può contenere informazioni riservate. L'utilizzo di SharePoint garantisce che l'agente **rispetti i permessi esistenti**: ogni utente riceverà risposte solo dai documenti a cui ha accesso.

## Prompt suggeriti

Nella sezione finale della configurazione premere `Add a suggested prompt` e inserire, ad esempio:

| Title | Message |
|---|---|
| `Gap analysis` | `Verifica la conformità GDPR del documento che ti allego` |
| `Checklist data breach` | `Crea una checklist di conformità per la gestione dei data breach` |
| `Domanda normativa` | `Quali sono i diritti degli interessati previsti dal GDPR?` |

## Test e condivisione

L'agente a questo punto sarà pienamente funzionante e sarà possibile testarlo nel pannello **Agent preview** a destra delle configurazioni, oppure dentro la Copilot Chat dopo aver premuto il tasto **Crea** in alto a destra.

??? tip "Condividere gli agenti"
	Una volta creato un agente questo sarà disponibile per l'utilizzo solamente per chi lo ha realizzato. Per condividerlo a colleghi occorre premere in alto a destra il tasto **Condividi** e scegliere specifici utenti, come se si stesse condividendo una cartella di OneDrive. La pubblicazione verso tutta l'azienda invece richiede l'approvazione dell'amministratore di sistema e potrebbe essere stata disabilitata. Per maggiori informazioni, consultare la [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents).
