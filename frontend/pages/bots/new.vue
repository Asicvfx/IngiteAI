<template>
  <div class="px-10 py-12 bg-black min-h-[calc(100vh-56px)] text-white font-sans relative">
    <div class="max-w-xl mx-auto">
      <div class="mb-16 text-center">
        <h1 class="text-3xl font-semibold tracking-[-0.022em]">Initialize Agent</h1>
        <p class="mt-2 text-[#6B7280] text-[14px]">Establish a new neural node in your business ecosystem.</p>
      </div>

      <div class="p-10 bg-black border border-[#1A1A1A] rounded-2xl">
        <form @submit.prevent="handleConnect" class="space-y-10">
          <div class="space-y-8">
            <div class="space-y-2">
              <label for="name" class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em]">Agent Identity</label>
              <input v-model="name" type="text" id="name" required 
                class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all placeholder-[#262626]" 
                placeholder="e.g. Support Prime">
            </div>
            
            <div class="space-y-2">
              <label for="token" class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em]">Access Token</label>
              <div class="relative">
                <input v-model="token" type="text" id="token" required 
                  class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] font-mono text-white focus:border-white/30 outline-none transition-all placeholder-[#262626]" 
                  placeholder="123456:ABC-DEF...">
                <div class="absolute right-4 top-1/2 -translate-y-1/2 text-[9px] text-[#4B5563] uppercase font-medium tracking-widest">BotFather</div>
              </div>
            </div>
          </div>

          <div class="pt-4">
            <button type="submit" :disabled="loading" 
              class="w-full py-4 bg-white text-black text-[13px] font-semibold rounded-xl hover:bg-gray-200 transition active:scale-95 disabled:opacity-50">
              {{ loading ? 'Synchronizing Node...' : 'Establish Connection' }}
            </button>
            
            <NuxtLink to="/bots" class="block text-center mt-8 text-[11px] font-medium text-[#4B5563] hover:text-white transition-colors uppercase tracking-[0.1em]">
              &lsaquo; Return to Ecosystem
            </NuxtLink>
          </div>

          <div v-if="error" class="mt-4 p-4 border border-red-500/20 rounded-xl text-red-400 text-[12px] font-medium text-center">
            {{ error }}
          </div>
        </form>
      </div>

      <div class="mt-16 flex justify-center space-x-4 opacity-5">
        <div class="w-1 h-1 bg-white rounded-full"></div>
        <div class="w-1 h-1 bg-white rounded-full"></div>
        <div class="w-1 h-1 bg-white rounded-full"></div>
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
