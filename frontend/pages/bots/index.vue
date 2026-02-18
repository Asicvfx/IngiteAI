<template>
  <div class="px-6 md:px-12 py-16 bg-[#080808] min-h-[calc(100vh-56px)] text-white font-sans">
    <div class="max-w-7xl mx-auto">
      <!-- Header Section -->
      <div class="flex flex-col md:flex-row md:items-end md:justify-between mb-20 gap-8">
        <div>
          <h1 class="text-4xl font-semibold tracking-[-0.04em] gradient-text">Agent Ecosystem</h1>
          <p class="mt-4 text-[#888888] text-[15px] leading-relaxed max-w-xl">
            Orchestrate and monitor your active neural synchronizations. Every agent is a specialized node in your automated intelligence fleet.
          </p>
        </div>
        <div class="shrink-0">
          <NuxtLink to="/bots/new" class="wope-button-primary !px-8 !py-4 shadow-2xl flex items-center space-x-3 group">
            <svg class="w-4 h-4 group-hover:rotate-90 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
            <span>Initialize Agent</span>
          </NuxtLink>
        </div>
      </div>

      <!-- Ecosystem Content -->
      <div class="mt-6">
        <div v-if="loading" class="flex flex-col items-center justify-center py-32 border border-dashed border-white/5 rounded-3xl group">
          <div class="w-12 h-12 border-2 border-white/5 border-t-white rounded-full animate-spin mb-6"></div>
          <p class="text-[#4B5563] text-[11px] font-bold uppercase tracking-[0.2em] group-hover:text-white transition-colors">Scanning Neural Web...</p>
        </div>
        
        <div v-else-if="error" class="text-red-400 text-center py-10 bg-red-400/5 border border-red-500/10 rounded-2xl text-[14px] font-medium">{{ error }}</div>
        
        <div v-else-if="bots.length === 0" class="text-center py-32 border border-dashed border-white/5 rounded-3xl group">
          <div class="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mx-auto mb-8 group-hover:scale-110 group-hover:bg-white transition-all duration-500">
            <svg class="w-6 h-6 text-[#262626] group-hover:text-black transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 012-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          </div>
          <p class="text-[#888888] text-[15px] mb-6 font-medium">No active agents detected in your synchronization network.</p>
          <NuxtLink to="/bots/new" class="text-white font-bold hover:underline text-[13px] uppercase tracking-widest border-b border-white pb-1">Initialize First Node &rarr;</NuxtLink>
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="bot in bots" :key="bot.id" class="wope-card p-10 group hover:translate-y-[-4px] transition-all relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-white/[0.01] blur-2xl group-hover:bg-white/[0.03] transition-all"></div>
            
            <div class="flex items-start justify-between mb-10 relative z-10">
              <div class="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-[#4B5563] group-hover:bg-white group-hover:border-white transition-all duration-500">
                <svg class="w-6 h-6 group-hover:text-black transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
              </div>
              <div class="flex items-center space-x-2 bg-white/5 px-3 py-1.5 rounded-full border border-white/5">
                 <div class="w-1.5 h-1.5 rounded-full animate-pulse" :class="bot.is_active ? 'bg-white shadow-[0_0_8px_rgba(255,255,255,0.5)]' : 'bg-[#1A1A1A]'"></div>
                 <span class="text-[9px] font-black uppercase tracking-[0.2em]" :class="bot.is_active ? 'text-white' : 'text-[#4B5563]'">
                   {{ bot.is_active ? 'Active' : 'Standby' }}
                 </span>
              </div>
            </div>
            
            <div class="relative z-10">
              <h3 class="text-[20px] font-semibold text-white mb-2 truncate tracking-tight">{{ bot.name }}</h3>
              <p class="text-[10px] text-[#4B5563] font-black uppercase tracking-[0.3em] mb-12">Neural Interface Synchronized</p>
              
              <div class="space-y-4 pt-8 border-t border-white/5">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] font-bold text-[#4B5563] uppercase tracking-[0.1em]">Uplink Handle</span>
                  <span class="text-[14px] font-semibold text-[#888888] tracking-tight">@{{ bot.username || 'Agent' }}</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-[10px] font-bold text-[#4B5563] uppercase tracking-[0.1em]">Signal Priority</span>
                  <span class="text-[12px] font-bold text-white uppercase tracking-widest">{{ bot.token ? 'L-9 Secured' : 'Unsecured' }}</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-[10px] font-bold text-[#4B5563] uppercase tracking-[0.1em]">Established</span>
                  <span class="text-[13px] font-semibold text-[#888888] tracking-tight">{{ new Date(bot.created_at).toLocaleDateString() }}</span>
                </div>
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

</script>
