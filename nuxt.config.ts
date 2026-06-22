export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
  runtimeConfig: {
    scoreServiceUrl: 'http://localhost:8080',
  },
})
