<template>
  <div class="container mt-5">
    <h2>{{ station.name }}</h2>
    <p><strong>ID:</strong> {{ station.id }}</p>

    <h4 class="mt-4">Metriche (ultimi 7 giorni)</h4>

    <table class="table table-striped mt-3">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Unità di misura</th>
          <th>Tipo</th>
          <th>Media ponderata</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="metric in station.metrics" :key="metric.name">
          <td>{{ metric.name }}</td>
          <td>{{ metric.unit_of_measurement }}</td>
          <td>{{ metric.type }}</td>
          <td>{{ metric.weighted_average }}</td>
        </tr>
      </tbody>
    </table>

    <NuxtLink to="/" class="btn btn-primary mt-3">← Torna alla lista</NuxtLink>
  </div>
</template>

<script setup>
const route = useRoute()
const config = useRuntimeConfig()
const station = ref({ metrics: [] })

onMounted(async () => {
  try {
    const res = await fetch(`${config.public.apiBase}/stations/${route.params.id}`)
    station.value = await res.json()
  } catch (err) {
    console.error("Errore nel caricamento:", err)
  }
})
</script>

