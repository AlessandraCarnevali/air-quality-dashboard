<script setup>
import "bootstrap/dist/css/bootstrap.min.css"
</script>

<template>
  <div>
        
<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg navbar-dark"
     style="background: linear-gradient(90deg,#1f8a70,#3bb273);">
  <div class="container d-flex justify-content-between align-items-center">
    
    <!-- TITOLO CENTRALE -->
    <div class="flex-grow-1 d-flex justify-content-center">
      <a class="navbar-brand d-flex align-items-center gap-2 text-center" href="/">
        <i class="bi bi-cloud-sun"></i>
        <span class="fw-bold fs-4">Air Quality Dashboard</span>
      </a>
    </div>

    <!-- PULSANTI A DESTRA -->
    <div class="d-flex gap-2">
      <button class="btn btn-outline-light btn-sm px-3">
        <i class="bi bi-box-arrow-in-right me-1"></i> Accedi
      </button>
      <button class="btn btn-light btn-sm px-3 text-success fw-semibold">
        <i class="bi bi-person-plus me-1"></i> Registrati
      </button>
    </div>
  </div>
</nav>


    <NuxtPage />
  </div>
</template>
