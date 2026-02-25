<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#0A0A0B] text-white">
    <div class="w-16 h-16 border-2 border-white/5 border-t-white rounded-full animate-spin mb-6"></div>
    <h2 class="text-xl font-semibold mb-2">Authenticating...</h2>
    <p class="text-[#888888] text-sm">{{ status }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '~/stores/auth';
import { useRouter, useRoute } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();
const route = useRoute();
const status = ref('Processing login...');

onMounted(async () => {
  setTimeout(async () => {
    // Authorization Code flow: code is in query params (e.g., ?code=4/...)
    const code = route.query.code as string;
    
    // Fallback: legacy implicit flow (access_token in hash)
    const hash = window.location.hash || route.hash;
    const hashParams = hash ? new URLSearchParams(hash.substring(1)) : null;
    const accessToken = hashParams?.get('access_token');

    if (code) {
      // Authorization Code flow
      status.value = 'Exchanging authorization code...';
      try {
        await auth.googleLoginWithCode(code, `${window.location.origin}/auth/callback`);
        status.value = 'Success! Redirecting...';
        router.push('/home');
      } catch (error: any) {
        let errorMsg = 'Backend validation error.';
        if (error.response && error.response._data) {
          errorMsg = JSON.stringify(error.response._data);
        } else if (error.response && error.response.data) {
          errorMsg = JSON.stringify(error.response.data);
        } else if (error.message) {
          errorMsg = error.message;
        }
        status.value = `Authentication failed: ${errorMsg}`;
        setTimeout(() => router.push('/login'), 6000);
      }
    } else if (accessToken) {
      // Legacy implicit flow fallback
      status.value = 'Validating token...';
      try {
        await auth.googleLogin(accessToken, 'access_token');
        status.value = 'Success! Redirecting...';
        router.push('/home');
      } catch (error: any) {
        let errorMsg = 'Backend validation error.';
        if (error.response && error.response.data) {
          errorMsg = JSON.stringify(error.response.data);
        } else if (error.message) {
          errorMsg = error.message;
        }
        status.value = `Authentication failed: ${errorMsg}`;
        setTimeout(() => router.push('/login'), 6000);
      }
    } else {
      status.value = 'Authentication failed: No code or token received.';
      setTimeout(() => router.push('/login'), 3000);
    }
  }, 200);
});
</script>
