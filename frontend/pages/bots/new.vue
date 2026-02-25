<template>
  <div class="px-6 md:px-12 py-24 min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden flex flex-col items-center justify-center">


    <div class="max-w-xl w-full relative z-10">
      <div class="mb-20 text-center">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] text-white">Create New Assistant</h1>
        <p class="mt-4 text-[#A1A1AA] text-[15px] leading-relaxed font-medium">
          Connect your Telegram bot to start automating customer conversations. Enter the bot token from @BotFather to get started.
        </p>
      </div>

      <div class="bg-[#050505]/80 border border-[#222] rounded-3xl p-12 backdrop-blur-xl shadow-2xl relative overflow-hidden group">
        <!-- Subtle hover glow -->
        <div class="absolute -top-32 -right-32 w-64 h-64 bg-white/[0.02] blur-[40px] rounded-full group-hover:bg-[#A855F7]/10 transition-colors duration-1000 -z-10"></div>
        
        <form @submit.prevent="handleConnect" class="space-y-12 relative z-10">
          <div class="space-y-10">
            <div class="space-y-4">
              <label for="name" class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-[0.2em]">Agent Identity</label>
              <input v-model="name" type="text" id="name" required 
                class="w-full bg-[#111] border border-[#222] rounded-2xl px-6 py-4 text-[15px] text-white focus:border-[#444] focus:ring-1 focus:ring-[#A855F7]/50 outline-none transition-all placeholder-[#444] font-medium tracking-tight shadow-inner" 
                placeholder="e.g. Support Prime">
            </div>
            
            <div class="space-y-4">
              <label for="token" class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-[0.2em]">Access Token</label>
              <div class="relative">
                <input v-model="token" type="text" id="token" required 
                  class="w-full bg-[#111] border border-[#222] rounded-2xl px-6 py-4 text-[15px] font-mono text-white focus:border-[#444] focus:ring-1 focus:ring-[#A855F7]/50 outline-none transition-all placeholder-[#444] tracking-tight shadow-inner" 
                  placeholder="123456:ABC-DEF...">
                <div class="absolute right-5 top-1/2 -translate-y-1/2 text-[9px] text-[#A1A1AA] uppercase font-bold tracking-[0.2em] bg-[#222] border border-[#333] px-2.5 py-1 rounded shadow-sm">Telegram</div>
              </div>
              <p class="text-[10px] text-[#888] font-medium text-center uppercase tracking-widest pt-2">Retrieved from @BotFather channel</p>
            </div>
          </div>

          <div class="pt-6 border-t border-[#222]">
            <button type="submit" :disabled="loading" 
              class="w-full bg-white hover:bg-gray-200 text-black py-4 rounded-xl text-[14px] font-semibold transition-all active:scale-95 shadow-xl disabled:opacity-30 disabled:hover:bg-white disabled:scale-100 flex justify-center items-center">
              <span v-if="loading" class="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin mr-2"></span>
              {{ loading ? 'Creating...' : 'Create Agent' }}
            </button>
            
            <NuxtLink to="/bots" class="block text-center mt-10 text-[11px] font-bold text-[#A1A1AA] hover:text-[#E4E4E5] transition-all uppercase tracking-[0.2em] group/link">
              <span class="opacity-40 group-hover/link:opacity-100 transition-opacity group-hover/link:-translate-x-1 inline-block">&lsaquo;</span> Return to Ecosystem
            </NuxtLink>
          </div>

          <div v-if="error" class="mt-6 p-5 border border-red-500/20 bg-red-900/10 rounded-2xl text-red-400 text-[13px] font-semibold text-center animate-pulse">
            {{ error }}
          </div>
        </form>
      </div>

      <div class="mt-20 flex justify-center space-x-6 opacity-20">
        <div class="w-1.5 h-1.5 bg-[#A1A1AA] rounded-full"></div>
        <div class="w-1.5 h-1.5 bg-[#A855F7] rounded-full animate-pulse shadow-[0_0_8px_rgba(168,85,247,0.8)]"></div>
        <div class="w-1.5 h-1.5 bg-[#A1A1AA] rounded-full"></div>
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
    error.value = 'Something went wrong. Please try again.';
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>
