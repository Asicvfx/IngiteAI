<template>
  <div class="px-10 py-12 bg-black min-h-[calc(100vh-56px)] text-white font-sans">
    <div class="max-w-6xl mx-auto">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-16">
        <div>
          <h1 class="text-3xl font-semibold tracking-[-0.022em]">Agent Ecosystem</h1>
          <p class="mt-2 text-[#6B7280] text-[14px]">Orchestrate and monitor your active synchronizations.</p>
        </div>
        <div class="mt-8 md:mt-0">
          <NuxtLink to="/bots/new" class="px-6 py-3 bg-white text-black text-[13px] font-semibold rounded-xl hover:bg-gray-200 transition active:scale-95 flex items-center">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
            Initialize Agent
          </NuxtLink>
        </div>
      </div>

      <div class="mt-6">
        <div v-if="loading" class="flex flex-col items-center justify-center py-20 border border-dashed border-[#1A1A1A] rounded-2xl">
          <div class="w-10 h-10 border-2 border-white/10 border-t-white rounded-full animate-spin mb-4"></div>
          <p class="text-[#4B5563] text-[11px] font-medium uppercase tracking-[0.2em]">Scanning Neural Web...</p>
        </div>
        <div v-else-if="error" class="text-red-400 text-center py-10 bg-red-400/5 border border-red-500/10 rounded-xl text-[13px] font-medium">{{ error }}</div>
        <div v-else-if="bots.length === 0" class="text-center py-20 border border-dashed border-[#1A1A1A] rounded-2xl">
          <div class="w-12 h-12 bg-[#0D0D0D] rounded-lg flex items-center justify-center mx-auto mb-6">
            <svg class="w-6 h-6 text-[#262626]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 012-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          </div>
          <p class="text-[#6B7280] text-[13px] mb-4">No active agents detected.</p>
          <NuxtLink to="/bots/new" class="text-white font-medium hover:underline text-[13px]">Initialize your first agent &rarr;</NuxtLink>
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="bot in bots" :key="bot.id" class="p-8 bg-black border border-[#1A1A1A] rounded-2xl hover:border-white/20 transition-all duration-300">
            <div class="flex items-center justify-between mb-8">
              <div class="w-10 h-10 rounded-lg bg-[#0D0D0D] border border-[#1A1A1A] flex items-center justify-center text-[#6B7280]">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
              </div>
              <span class="px-3 py-1 rounded-md text-[10px] font-medium uppercase tracking-[0.1em]" :class="bot.is_active ? 'bg-white text-black' : 'border border-[#1A1A1A] text-[#6B7280]'">
                {{ bot.is_active ? 'Active' : 'Standby' }}
              </span>
            </div>
            
            <h3 class="text-[17px] font-medium text-white mb-2 truncate">{{ bot.name }}</h3>
            <p class="text-[11px] text-[#4B5563] font-medium uppercase tracking-[0.2em] mb-10">Neural Interface</p>
            
            <div class="space-y-4 pt-8 border-t border-[#1A1A1A]">
              <div class="flex items-center justify-between">
                <span class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.05em]">Handle</span>
                <span class="text-[13px] font-medium text-[#9CA3AF]">@{{ bot.username || 'Agent' }}</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.05em]">Token</span>
                <span class="text-[13px] font-medium text-[#262626] font-mono tracking-tight">{{ bot.token ? '••••' + bot.token.slice(-4) : 'N/A' }}</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.05em]">Established</span>
                <span class="text-[13px] font-medium text-[#9CA3AF]">{{ new Date(bot.created_at).toLocaleDateString() }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '~/stores/auth';

const auth = useAuthStore();
const config = useRuntimeConfig();
const bots = ref<any[]>([]);
const loading = ref(true);
const error = ref('');

onMounted(async () => {
  try {
    const data = await $fetch<any[]>(`${config.public.apiBaseUrl}/api/v1/bots/`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    bots.value = data;
  } catch (err) {
    error.value = 'Failed to synchronize with agent network.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>
