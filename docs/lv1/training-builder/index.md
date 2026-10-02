# Training Builder · v1 (Agent Builder)

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**

## Panoramica

Preparare un corso di formazione, interno o verso clienti, richiede molto lavoro preparatorio: **definire l'agenda, distribuire i tempi, scrivere quiz di verifica e progettare esercitazioni pratiche**. Spesso il materiale di partenza esiste già (documentazione tecnica, manuali, slide), ma va trasformato in un percorso didattico.

Queste attività:

- Richiedono tempo e competenze di progettazione didattica
- Vengono ripetute per ogni nuovo corso o edizione
- Producono materiali con struttura e qualità variabili

## Problema

Abbiamo identificato tre criticità principali:

- **Tempo di preparazione elevato** : Trasformare documentazione tecnica in un corso strutturato richiede ore di lavoro.
- **Materiali disomogenei** : Agende, quiz ed esercitazioni hanno formati diversi a seconda di chi li prepara.
- **Verifica dell'apprendimento trascurata** : Quiz ed esercitazioni vengono spesso preparati all'ultimo o omessi.

## Soluzione

**Training Builder (v1)** è un agente progettato **esclusivamente per la creazione di materiali formativi** a partire da documenti caricati in chat o da un argomento tecnico indicato dall'utente.

L'agente produce tre tipologie di output:

- **Agenda del corso** : moduli, obiettivi didattici e durata di ciascuna sessione
- **Quiz** : domande a risposta multipla con soluzione e spiegazione
- **Esercitazioni** : attività pratiche con obiettivo, prerequisiti, passaggi e risultato atteso

Questo approccio permette di:

- Ridurre drasticamente i tempi di preparazione di un corso
- Standardizzare il formato dei materiali formativi
- Includere sempre momenti di verifica e pratica

## Esempi di utilizzo

**Richiesta utente**

`Crea l'agenda di un corso di 4 ore su Microsoft Intune per tecnici IT junior`

**Comportamento dell'agente**

1. Verifica i parametri essenziali (argomento, durata, destinatari, livello)
2. Chiede eventuali dettagli mancanti prima di procedere
3. Genera l'agenda in formato tabellare
4. Propone di generare quiz ed esercitazioni coerenti con l'agenda

Altri esempi:

- `Crea 10 domande a risposta multipla sul documento allegato`
- `Prepara un'esercitazione pratica di 30 minuti sulla configurazione di una VPN`
- `Partendo da questo manuale, crea un corso completo di una giornata con quiz finale`

## Get started
→ **[Apri la guida tecnica](lab-guide.md)**
