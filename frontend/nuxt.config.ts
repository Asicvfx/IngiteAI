// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt'],
  css: ['~/assets/css/main.css'],
  app: {
    pageTransition: { name: 'page', mode: 'out-in' }
  },
  runtimeConfig: {
    public: {
      googleClientId: process.env.NUXT_PUBLIC_GOOGLE_CLIENT_ID || '508576287981-pd8sg3pleboibd5hu29dlo30gnmgmlh6.apps.googleusercontent.com',
      // Determine if we are running locally based on NODE_ENV, otherwise default to production backend
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE || (process.env.NODE_ENV === 'development' ? 'http://localhost:8000' : 'https://ingite-backend.onrender.com')
    }
  }
})
