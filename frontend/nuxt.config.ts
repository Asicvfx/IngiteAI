// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt'],
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    public: {
      googleClientId: process.env.NUXT_PUBLIC_GOOGLE_CLIENT_ID || '508576287981-pd8sg3pleboibd5hu29dlo30gnmgmlh6.apps.googleusercontent.com',
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000'
    }
  }
})
