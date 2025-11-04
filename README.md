 **AIR QUALITY DASHBOARD**

Mini-app realizzata da **Alessandra Carnevali** come esercizio tecnico per Guidance Srl (tramite Aulab).

L’applicazione mostra i dati sulla qualità dell’aria provenienti dall’API pubblica **ZeroC Green**, con backend in Flask e frontend in Nuxt 3.

---

Come avviare il progetto in locale

  **Backend (Flask)**

**NB: Dato che servirà un ambiente virtuale, se non lo si è già fatto, crearlo con python3 -m venv venv, ```bash,  ovviamente dentro la cartella backend**


 1) Aprire da terminale la cartella backend con code . o qualsiasi altro strumento si utilizzi per aprire codice.
  
 2) Dopodiché, aprire il terminale dallo strumento e attivare l'ambiente virtuale con **source venv/bin/activate**, **```bash** . Assicurarsi di essere dentro la cartella backend giustamente.

 3) Installare le dipendeze di flask-cors con questo comando: **pip install flask flask-cors requests**

 4) Per avviare infine Flask, farlo con: flask run. Questò farà partire il server.


**Frontend (Nuxt)**

1) Eseguire le procedure fatte per aprire il backend, ma ovviamente eseguite su frontend
2) Avviare il terminale dallo strumeto e fare: **npm install** che installerà le dipendeze
3) Fare poi **npm run dev** che avvierà il frontend.



   **Descrizione funzionalità**

   GET /api/stations → Elenco di tutte le stazioni disponibili

   GET /api/stations/:id → Dati giornalieri e media ponderata delle metriche (ultimi 7 giorni)


  **Interfaccia**

  Interfaccia moderna con Bootstrap 5

  Tabella interattiva con ricerca e navigazione ai dettagli

  Grafica responsive con immagine “hero” e navbar personalizzata


  **Versione utilizzate**

  | Componente  | Versione |
| ----------- | -------- |
| **Python**  | 3.12.7   |
| **Node.js** | 20.x     |
| **npm**     | 10.x     |
| **Flask**   | 3.x      |
| **Nuxt**    | 3.10+    |



  
   
