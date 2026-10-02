# NIS2 Compliance Monitor · v1 (Agent Builder)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**

## Panoramica

La **Direttiva (UE) 2022/2555 (NIS2)**, recepita in Italia con il **D.Lgs. 138/2024**, amplia in modo significativo il perimetro dei soggetti tenuti a garantire elevati livelli di cybersicurezza. Le organizzazioni coinvolte devono adottare misure di gestione del rischio, notificare gli incidenti significativi entro tempi stringenti e garantire la responsabilità degli organi di amministrazione.

Mantenere la conformità richiede di:

- Capire se e come l'organizzazione rientra nel perimetro (soggetto essenziale o importante)
- Tradurre i requisiti normativi in controlli e procedure concrete
- Monitorare nel tempo l'allineamento di policy e processi interni

## Problema

Abbiamo identificato tre criticità principali:

- **Normativa nuova e articolata** : Direttiva, decreto di recepimento e determinazioni dell'ACN formano un quadro complesso e in evoluzione.
- **Difficoltà di tradurre i requisiti in azioni** : Le misure di gestione del rischio (art. 21) devono essere declinate in controlli operativi verificabili.
- **Tempi stringenti sugli incidenti** : Gli obblighi di notifica (preallarme entro 24 ore, notifica entro 72 ore, relazione finale entro un mese) richiedono procedure chiare e note a tutti.

## Soluzione

**NIS2 Compliance Monitor (v1)** è un agente progettato **esclusivamente per il supporto al monitoraggio della conformità NIS2**, basato sui testi normativi e sulla documentazione interna di sicurezza.

L'agente:

- Risponde a domande su NIS2 e D.Lgs. 138/2024 **citando l'articolo di riferimento**
- Esegue una **gap analysis** di policy e procedure interne rispetto alle misure di gestione del rischio previste
- Produce **checklist di conformità** per ambito (gestione incidenti, supply chain, continuità operativa, controllo accessi, crittografia, formazione)
- Classifica i gap rilevati per priorità e suggerisce le azioni correttive

!!! warning "Disclaimer"
	L'agente è uno **strumento di supporto** e non sostituisce il parere di consulenti legali o di cybersicurezza qualificati. Ogni valutazione deve essere verificata da personale competente.

Questo approccio permette di:

- Rendere la normativa accessibile a IT, management e responsabili di processo
- Accelerare le attività di assessment periodico
- Diffondere in azienda la conoscenza delle procedure di notifica degli incidenti

## Esempi di utilizzo

**Richiesta utente**

`Verifica se la nostra procedura di gestione degli incidenti è allineata ai requisiti NIS2`

**Comportamento dell'agente**

1. Confronta la procedura con gli obblighi di gestione e notifica degli incidenti
2. Produce una tabella Requisito | Presente/Assente/Parziale | Riferimento | Azione suggerita
3. Assegna una priorità (Alta / Media / Bassa) ai gap rilevati
4. Ricorda di sottoporre l'esito ai referenti di sicurezza per la validazione

Altri esempi:

- `Quali sono le tempistiche di notifica di un incidente significativo?`
- `Crea una checklist per la sicurezza della supply chain`
- `Quali responsabilità ha il consiglio di amministrazione secondo la NIS2?`

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**
