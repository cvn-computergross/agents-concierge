# GDPR Compliance Monitor · v1 (Agent Builder)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**

## Panoramica

Il **Regolamento (UE) 2016/679 (GDPR)** impone alle organizzazioni un impegno continuo nella protezione dei dati personali: registro dei trattamenti, informative, basi giuridiche, misure di sicurezza, gestione dei data breach e dei diritti degli interessati.

Mantenere la conformità richiede di:

- Conoscere e interpretare correttamente il testo normativo e le linee guida delle autorità
- Verificare periodicamente che processi e documenti interni siano allineati
- Rispondere rapidamente a dubbi operativi di colleghi non specialisti

## Problema

Abbiamo identificato tre criticità principali:

- **Normativa complessa** : Il GDPR e le linee guida collegate sono testi lunghi e tecnici, difficili da consultare per chi non è un esperto.
- **Verifiche manuali** : Controllare documenti interni (informative, registro dei trattamenti, procedure) rispetto ai requisiti normativi è un'attività lenta e soggetta a dimenticanze.
- **Dipendenza dal DPO** : Ogni dubbio operativo ricade sul DPO o sull'ufficio legale, creando colli di bottiglia.

## Soluzione

**GDPR Compliance Monitor (v1)** è un agente progettato **esclusivamente per il supporto al monitoraggio della conformità GDPR**, basato sul testo del regolamento e sulla documentazione interna dell'organizzazione.

L'agente:

- Risponde a domande sul GDPR **citando l'articolo di riferimento**
- Esegue una **gap analysis** di un documento interno (es. informativa privacy, registro dei trattamenti) rispetto ai requisiti del regolamento
- Produce **checklist di conformità** per ambito (data breach, diritti degli interessati, fornitori/responsabili, sicurezza)
- Classifica i gap rilevati per priorità e suggerisce le azioni correttive

!!! warning "Disclaimer"
	L'agente è uno **strumento di supporto** e non sostituisce il parere del DPO, dell'ufficio legale o di consulenti qualificati. Ogni valutazione deve essere verificata da personale competente.

Questo approccio permette di:

- Rendere la normativa accessibile anche a chi non è specialista
- Accelerare le verifiche periodiche di conformità
- Ridurre il carico di richieste operative verso il DPO

## Esempi di utilizzo

**Richiesta utente**

`Verifica se l'informativa privacy allegata contiene tutti gli elementi richiesti dal GDPR`

**Comportamento dell'agente**

1. Confronta il documento con i requisiti degli artt. 13 e 14 GDPR
2. Produce una tabella Requisito | Presente/Assente/Parziale | Riferimento | Azione suggerita
3. Assegna una priorità (Alta / Media / Bassa) ai gap rilevati
4. Ricorda di sottoporre l'esito al DPO per la validazione

Altri esempi:

- `Entro quanto tempo dobbiamo notificare un data breach al Garante?`
- `Crea una checklist per la gestione delle richieste di accesso degli interessati`
- `Quali clausole deve contenere un accordo con un responsabile del trattamento?`

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**
