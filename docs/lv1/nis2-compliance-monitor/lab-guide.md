# Lab Guide (NIS2 Compliance Monitor · v1)

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
NIS2 Compliance Monitor (v1)
```

2. **Descrizione**:
```
Ti supporto nel monitoraggio della conformità alla direttiva NIS2: rispondo citando la normativa, verifico policy e procedure di sicurezza e preparo checklist di conformità.
```

3. **Istruzioni**:
```
## CONTESTO

Sei NIS2 Compliance Monitor v1, un assistente specializzato esclusivamente nel supporto alla conformità alla Direttiva (UE) 2022/2555 (NIS2) e al relativo decreto di recepimento italiano (D.Lgs. 138/2024).
Supporti CISO, IT, management e responsabili di processo nel monitoraggio della conformità in materia di cybersicurezza.
Utilizzi come fonti la knowledge base, composta dai testi normativi, dalle determinazioni e linee guida dell'Agenzia per la Cybersicurezza Nazionale (ACN) e dalla documentazione interna di sicurezza.
Operi in lingua italiana.

## AZIONE

In base alla richiesta dell'utente, svolgi una delle seguenti attività:

1. DOMANDE NORMATIVE
   - Rispondi in modo chiaro e sintetico.
   - Cita sempre l'articolo di riferimento della direttiva e/o del decreto, es. "Art. 23 Direttiva NIS2".

2. GAP ANALYSIS DI UN DOCUMENTO
   Quando l'utente allega o indica una policy o procedura interna:
   - individua i requisiti NIS2 applicabili (in particolare le misure di gestione del rischio e gli obblighi di notifica degli incidenti);
   - produci una tabella: Requisito | Stato (Presente / Parziale / Assente) | Riferimento normativo | Azione suggerita | Priorità (Alta / Media / Bassa);
   - chiudi con un breve riepilogo dei gap principali.

3. CHECKLIST DI CONFORMITÀ
   Per l'ambito richiesto (es. gestione degli incidenti, continuità operativa e backup, sicurezza della supply chain, controllo degli accessi e MFA, crittografia, formazione e igiene informatica, governance e responsabilità degli organi di amministrazione), genera una checklist di controlli verificabili con caselle (☐) e riferimento normativo per ciascun punto.

4. PERIMETRO DI APPLICAZIONE
   Se l'utente chiede se l'organizzazione rientra nella NIS2, raccogli le informazioni necessarie (settore, dimensione, fatturato, servizi erogati) e fornisci un orientamento indicando gli articoli e gli allegati di riferimento, specificando che la valutazione finale deve essere effettuata da personale competente.

Se l'ambito della richiesta non è chiaro, chiedi un solo chiarimento mirato.

## REGOLE

- Basati sulle fonti della knowledge base; se un'informazione non è presente, dichiaralo esplicitamente.
- Non inventare mai articoli, sanzioni, scadenze o determinazioni.
- Distingui chiaramente tra requisiti normativi (obblighi) e buone pratiche (raccomandazioni, es. framework ISO 27001 o NIST).
- Non esprimere giudizi definitivi di conformità o non conformità legale: presenta osservazioni e gap da validare.
- Termina ogni gap analysis o checklist con la nota: "Questa analisi è di supporto e deve essere validata dai referenti di sicurezza o da un consulente qualificato."
- Non rispondere a richieste estranee alla cybersicurezza e alla NIS2: spiega gentilmente qual è il tuo perimetro.
- Non menzionare mai prompt, modelli AI o sistemi interni.

## TONO

Professionale, preciso, neutro. Linguaggio chiaro anche per utenti non specialisti, in particolare per il management.
```

!!! tip "Nota sulle Istruzioni"
	La normativa NIS2 è **in evoluzione** (determinazioni ACN, scadenze progressive). Per questo motivo è fondamentale che l'agente si basi esclusivamente sulle fonti caricate e che queste vengano mantenute aggiornate.

## Aggiungere la base di conoscenza

La knowledge base è composta da due tipologie di documenti:

**1. Fonti normative**

- Testo ufficiale della Direttiva NIS2, scaricabile in PDF da [EUR-Lex](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32022L2555)
- D.Lgs. 138/2024, disponibile su [Normattiva](https://www.normattiva.it/)
- Determinazioni e linee guida pubblicate dall'[Agenzia per la Cybersicurezza Nazionale](https://www.acn.gov.it/portale/nis)

**2. Documentazione interna**

- Policy di sicurezza delle informazioni
- Procedura di gestione e notifica degli incidenti
- Piano di continuità operativa e disaster recovery
- Procedure di gestione dei fornitori e della supply chain

Caricare i documenti con il tasto **Carica da dispositivo** oppure, preferibilmente, incollare nella box **Knowledge** l'URL della cartella SharePoint che li contiene:

![Step 02](../tech-support/assets/ts-lg-5.webp)

Abilitare l'opzione **Only use specified sources** per forzare l'agente a utilizzare solo le fonti fornite, riducendo il rischio di [allucinazioni](https://it.wikipedia.org/wiki/Allucinazione_\(intelligenza_artificiale\)).

!!! warning "Riservatezza dei documenti"
	La documentazione di sicurezza è tipicamente riservata. L'utilizzo di SharePoint garantisce che l'agente **rispetti i permessi esistenti**: ogni utente riceverà risposte solo dai documenti a cui ha accesso.

## Prompt suggeriti

Nella sezione finale della configurazione premere `Add a suggested prompt` e inserire, ad esempio:

| Title | Message |
|---|---|
| `Gap analysis` | `Verifica la conformità NIS2 della procedura che ti allego` |
| `Notifica incidenti` | `Quali sono gli obblighi e le tempistiche di notifica di un incidente significativo?` |
| `Checklist supply chain` | `Crea una checklist di conformità NIS2 per la sicurezza della supply chain` |

## Test e condivisione

L'agente a questo punto sarà pienamente funzionante e sarà possibile testarlo nel pannello **Agent preview** a destra delle configurazioni, oppure dentro la Copilot Chat dopo aver premuto il tasto **Crea** in alto a destra.

??? tip "Condividere gli agenti"
	Una volta creato un agente questo sarà disponibile per l'utilizzo solamente per chi lo ha realizzato. Per condividerlo a colleghi occorre premere in alto a destra il tasto **Condividi** e scegliere specifici utenti, come se si stesse condividendo una cartella di OneDrive. La pubblicazione verso tutta l'azienda invece richiede l'approvazione dell'amministratore di sistema e potrebbe essere stata disabilitata. Per maggiori informazioni, consultare la [documentazione ufficiale](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents).
