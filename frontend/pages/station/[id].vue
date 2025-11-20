<template>
  <div class="container mt-5">

    <!-- Titolo -->
    <h2>{{ station.name }}</h2>
    <p><strong>ID:</strong> {{ station.id }}</p>

    <!-- MEDIA PONDERATA - BOX EVIDENZIATO -->
    <div class="mt-4">
      <h4>Media ponderata (ultimi 7 giorni)</h4>

      <div
        v-for="metric in station.metrics"
        :key="metric.name"
        class="alert alert-primary d-flex justify-content-between align-items-center mt-2"
      >
        <strong>{{ metric.name }}</strong>
        <span class="fw-bold">{{ metric.weighted_average }} {{ metric.unit_of_measurement }}</span>
      </div>
    </div>

    <!-- METRICHE - tabella riassuntiva -->
    <h4 class="mt-5">Metriche disponibili</h4>

    <table class="table table-striped mt-3">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Unità di misura</th>
          <th>Tipo</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="metric in station.metrics" :key="metric.name">
          <td>{{ metric.name }}</td>
          <td>{{ metric.unit_of_measurement }}</td>
          <td>{{ metric.type }}</td>
        </tr>
      </tbody>
    </table>

    <!-- GRAFICO ANDAMENTO -->
    <div class="mt-5">
      <h4>Grafico andamento</h4>

      <!-- Selettore metrica -->
      <select v-model="selectedMetric" class="form-select w-25 mb-3">
        <option disabled value="">Seleziona una metrica</option>
        <option v-for="m in station.metrics" :key="m.name" :value="m">
          {{ m.name }}
        </option>
      </select>

      <!-- Canvas del grafico -->
      <canvas id="metricChart" height="120"></canvas>
    </div>

    <!-- DETTAGLI GIORNALIERI -->
    <h4 class="mt-5">Dettagli giornalieri (ultimi 10 giorni)</h4>

    <table class="table table-bordered mt-3" v-if="station.metrics">
      <thead>
        <tr>
          <th>Nome metrica</th>
          <th>Data</th>
          <th>Min</th>
          <th>Average</th>
          <th>Max</th>
          <th>Campioni (sample size)</th>
        </tr>
      </thead>

      <tbody>
        <template v-for="metric in station.metrics" :key="metric.name">
          <tr v-for="dp in metric.data_points" :key="dp.date">
            <td>{{ metric.name }}</td>
            <td>{{ dp.date }}</td>
            <td>{{ dp.min }}</td>
            <td>{{ dp.average }}</td>
            <td>{{ dp.max }}</td>
            <td>{{ dp.sample_size }}</td>
          </tr>
        </template>
      </tbody>
    </table>

    <!-- Pulsante torna indietro -->
    <NuxtLink to="/" class="btn btn-primary mt-3">← Torna alla lista</NuxtLink>

  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue"
import { useRoute, useRuntimeConfig } from "#imports"

// Chart.js
import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  CategoryScale
} from "chart.js"

Chart.register(LineController, LineElement, PointElement, LinearScale, Title, CategoryScale)

const route = useRoute()
const config = useRuntimeConfig()

const station = ref({ metrics: [] })
const selectedMetric = ref(null)
let chart = null

// Fetch dati
onMounted(async () => {
  try {
    const res = await fetch(`${config.public.apiBase}/stations/${route.params.id}`)
    station.value = await res.json()
  } catch (err) {
    console.error("Errore nel caricamento:", err)
  }
})

// Quando cambia la metrica → aggiorna grafico
watch(selectedMetric, (metric) => {
  if (!metric) return

  const labels = metric.data_points.map(dp => dp.date)
  const minData = metric.data_points.map(dp => dp.min)
  const avgData = metric.data_points.map(dp => dp.average)
  const maxData = metric.data_points.map(dp => dp.max)

  const ctx = document.getElementById("metricChart")

  if (chart) chart.destroy()

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Min",
          data: minData,
          borderColor: "blue",
          fill: false
        },
        {
          label: "Average",
          data: avgData,
          borderColor: "green",
          fill: false
        },
        {
          label: "Max",
          data: maxData,
          borderColor: "red",
          fill: false
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: `Andamento di ${metric.name} (ultimi 10 giorni)`
        }
      }
    }
  })
})
</script>
