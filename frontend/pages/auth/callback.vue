<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#080808] text-white">
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
const status = ref('Extracting security token...');

onMounted(async () => {
  // Google returns token in the URL hash, e.g., #access_token=...&token_type=Bearer&expires_in=3599
  // Alternatively wait for a few milliseconds to ensure route.hash is populated
  setTimeout(async () => {
    const hash = window.location.hash || route.hash;
    if (!hash) {
      status.value = 'Authentication failed: No token received.';
      setTimeout(() => router.push('/login'), 3000);
      return;
    }

    const params = new URLSearchParams(hash.substring(1)); // Remove the '#'
    const accessToken = params.get('access_token');

    if (accessToken) {
      status.value = 'Validating token with backend...';
      try {
        await auth.googleLogin(accessToken, 'access_token');
        status.value = 'Authentication successful! Redirecting...';
        router.push('/');
      } catch (error: any) {
        // Extract and display the exact backend error message for debugging
        let errorMsg = 'Backend validation error.';
        if (error.response && error.response.data) {
          errorMsg = JSON.stringify(error.response.data);
        } else if (error.message) {
          errorMsg = error.message;
        }
        status.value = `Authentication failed: ${errorMsg}`;
        setTimeout(() => router.push('/login'), 8000); // Wait 8s so user can read it
      }
    } else {
      status.value = 'Authentication failed: Missing access token.';
      setTimeout(() => router.push('/login'), 3000);
    }
  }, 100);
});
</script>
