<template>
  <div>
    <!-- HERO con immagine -->
    <section class="text-white d-flex align-items-center"
             style="min-height: 220px;
                    background: linear-gradient(180deg, rgba(0,0,0,.35), rgba(0,0,0,.55)),
                                url('/hero.jpg') center/cover no-repeat;">
      <div class="container">
        <h1 class="fw-bold mb-2">
          <i class="bi bi-activity me-2"></i>Stazioni disponibili
        </h1>
        <p class="mb-0 opacity-75"> Di seguito tutti i dettagli nello specifico.</p>
      </div> 
    </section>

    <!-- LISTA -->
    <div class="container my-4">
      <div class="card shadow-sm border-0">
        <div class="card-body">
          <div class="d-flex gap-2 flex-wrap justify-content-between align-items-center mb-3">
            <h5 class="mb-0">Elenco stazioni</h5>

            <!-- piccolo filtro client-side -->
            <div class="input-group" style="max-width: 320px;">
              <span class="input-group-text"><i class="bi bi-search"></i></span>
              <input v-model="q" type="text" class="form-control" placeholder="Cerca per nome o ID…" />
            </div>
          </div>

          <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
              <thead class="table-success">
                <tr>
                  <th style="width:40%">Nome</th>
                  <th>ID</th>
                  <th style="width:110px" class="text-end">Dettagli</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="station in filtered" :key="station.id"
                    @click="goTo(station.id)"
                    style="cursor:pointer">
                  <td class="fw-semibold">
                    <i class="bi bi-geo-alt me-2 text-success"></i>
                        {{ renameStation(station.name) }}
                          </td>

                  <td class="text-muted small">{{ station.id }}</td>
                  <td class="text-end">
                    <button class="btn btn-sm btn-outline-success">
                      Apri <i class="bi bi-arrow-right-short"></i>
                    </button>
                  </td>
                </tr>
                <tr v-if="filtered.length === 0">
                  <td colspan="3" class="text-center text-muted py-4">
                    Nessun risultato per “{{ q }}”.
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const stations = ref([])
const q = ref("")

onMounted(async () => {
  const res = await fetch(`${config.public.apiBase}/stations`)
  const data = await res.json()
  stations.value = data.stations || []  
})


const filtered = computed(() => {
  const term = q.value.toLowerCase().trim()
  if (!term) return stations.value

  return stations.value.filter(s => {
    const renamed = renameStation(s.name).toLowerCase()
    return (
      renamed.includes(term) || 
      s.name.toLowerCase().includes(term) ||
      s.id.toLowerCase().includes(term)
    )
  })
})


const renameStation = (name) => {
  if (name === "ZeroC 1") return "Milano"
  if (name === "ZeroC 2") return "Roma"
  if (name === "ZeroC 3") return "Torino"
  if (name === "ZeroC 4") return "Genova"
  if (name === "ZeroC 5") return "Firenze"
  return name
}


const goTo = (id) => navigateTo(`/station/${id}`)
</script>

