from flask import Flask, jsonify
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



# URL dell'API pubblica che ci fornisce i dati
BASE_URL =  "https://api.zeroc.green/v1/"


# Primo endpoint: elenco delle stazioni
@app.route("/api/stations")
def get_stations():
    import urllib3

    # disattiva i warning SSL (solo per sviluppo)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        # URL corretto con /v1/stations
        full_url = f"{BASE_URL}stations/"
        print("Chiamata diretta a:", full_url)

        headers = {"Accept": "application/json"}
        response = requests.get(full_url, headers=headers, verify=False, timeout=10)
        print("Status code:", response.status_code)
        print("Response text:", response.text[:200])

        response.raise_for_status()
        return jsonify(response.json())

    except requests.exceptions.RequestException as e:
        print("Errore nella richiesta:", e)
        return jsonify({
            "error": "Impossibile recuperare le stazioni",
            "details": str(e)
        }), 500



# Secondo endpoint: dettagli di una singola stazione
@app.route("/api/stations/<station_id>")
def get_station(station_id):
    try:
        response = requests.get(f"{BASE_URL}stations/{station_id}")
        response.raise_for_status()
        data = response.json()

        # Ogni metrica è un dizionario dentro una lista
        for metric in data.get("metrics", []):
            data_points = metric.get("data_points", [])
            valid_days = [d for d in data_points[-7:] if d.get("sample_size", 0) > 0]

            if not valid_days:
                metric["weighted_average"] = None
                continue
            
            # Calcolo della media ponderata
            total_weighted = sum(d["average"] * d["sample_size"] for d in valid_days)
            total_samples = sum(d["sample_size"] for d in valid_days)
            weighted_avg = total_weighted / total_samples if total_samples > 0 else None

            metric["weighted_average"] = round(weighted_avg, 2) if weighted_avg else None

        return jsonify(data)

    except Exception as e:
        print("Errore:", e)
        return jsonify({"error": "Errore durante la richiesta", "details": str(e)}), 500




# Avvia il server
if __name__ == "__main__":
    app.run(debug=True)
