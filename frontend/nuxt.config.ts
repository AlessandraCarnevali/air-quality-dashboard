export default defineNuxtConfig({
  devtools: { enabled: true },

  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:5000/api'
    }
  },

  nitro: {
    devProxy: {
      "/api": "http://127.0.0.1:5000/api"
    }
  }
})



