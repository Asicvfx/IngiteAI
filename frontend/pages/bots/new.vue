<template>
  <div class="px-6 md:px-12 py-24 bg-[#080808] min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden flex flex-col items-center justify-center">
    <!-- Decorative background element -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-white/[0.01] blur-[120px] rounded-full pointer-events-none"></div>

    <div class="max-w-xl w-full relative z-10">
      <div class="mb-20 text-center">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] gradient-text">Initialize Agent</h1>
        <p class="mt-4 text-[#888888] text-[15px] leading-relaxed">
          Establish a new neural node in your business ecosystem. Sync your Telegram bot token to begin the handshake.
        </p>
      </div>

      <div class="wope-card p-12 bg-[#0C0C0C]/80 backdrop-blur-xl">
        <form @submit.prevent="handleConnect" class="space-y-12">
          <div class="space-y-10">
            <div class="space-y-4">
              <label for="name" class="text-[11px] font-bold text-[#4B5563] uppercase tracking-[0.2em]">Agent Identity</label>
              <input v-model="name" type="text" id="name" required 
                class="w-full bg-[#0E0E0E] border border-white/5 rounded-2xl px-6 py-4 text-[15px] text-white focus:border-white/20 outline-none transition-all placeholder-[#262626] font-medium tracking-tight" 
                placeholder="e.g. Support Prime">
            </div>
            
            <div class="space-y-4">
              <label for="token" class="text-[11px] font-bold text-[#4B5563] uppercase tracking-[0.2em]">Access Token</label>
              <div class="relative">
                <input v-model="token" type="text" id="token" required 
                  class="w-full bg-[#0E0E0E] border border-white/5 rounded-2xl px-6 py-4 text-[15px] font-mono text-white focus:border-white/20 outline-none transition-all placeholder-[#262626] tracking-tight" 
                  placeholder="123456:ABC-DEF...">
                <div class="absolute right-5 top-1/2 -translate-y-1/2 text-[9px] text-[#4B5563] uppercase font-bold tracking-[0.2em] bg-white/5 px-2 py-1 rounded">Uplink</div>
              </div>
              <p class="text-[10px] text-[#4B5563] font-medium text-center uppercase tracking-widest pt-2">Retrieved from @BotFather channel</p>
            </div>
          </div>

          <div class="pt-6">
            <button type="submit" :disabled="loading" 
              class="wope-button-primary w-full !py-5 !text-[14px] shadow-2xl disabled:opacity-20">
              {{ loading ? 'Synchronizing Node...' : 'Establish Secure Connection' }}
            </button>
            
            <NuxtLink to="/bots" class="block text-center mt-10 text-[11px] font-bold text-[#4B5563] hover:text-white transition-all uppercase tracking-[0.2em] group">
              <span class="opacity-40 group-hover:opacity-100 transition-opacity">&lsaquo;</span> Return to Ecosystem
            </NuxtLink>
          </div>

          <div v-if="error" class="mt-6 p-5 border border-red-500/20 bg-red-500/5 rounded-2xl text-red-500 text-[13px] font-semibold text-center animate-pulse">
            {{ error }}
          </div>
        </form>
      </div>

      <div class="mt-20 flex justify-center space-x-6 opacity-10">
        <div class="w-1.5 h-1.5 bg-white rounded-full"></div>
        <div class="w-1.5 h-1.5 bg-white rounded-full animate-pulse"></div>
        <div class="w-1.5 h-1.5 bg-white rounded-full"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '~/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const config = useRuntimeConfig();
const router = useRouter();
const name = ref('');
const token = ref('');
const loading = ref(false);
const error = ref('');

const handleConnect = async () => {
  loading.value = true;
  error.value = '';
  try {
    await $fetch(`${config.public.apiBaseUrl}/api/v1/bots/`, {
      method: 'POST',
      body: { name: name.value, token: token.value },
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    router.push('/bots');
  } catch (err: any) {
    error.value = 'Neural handshake failed. Verify access token.';
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>
