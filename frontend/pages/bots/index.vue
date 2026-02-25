<template>
  <div class="px-6 md:px-12 py-16 min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden">


    <div class="max-w-7xl mx-auto relative z-10">
      <!-- Header Section -->
      <div class="flex flex-col md:flex-row md:items-end md:justify-between mb-20 gap-8">
        <div>
          <h1 class="text-4xl font-semibold tracking-[-0.04em] text-white">AI Assistants</h1>
          <p class="mt-4 text-[#A1A1AA] text-[15px] leading-relaxed max-w-xl font-medium">
            Manage your AI assistants. Each agent handles customer conversations automatically — responding instantly, qualifying leads, and escalating when needed.
          </p>
        </div>
        <div class="shrink-0">
          <NuxtLink to="/bots/new" class="bg-white hover:bg-gray-200 text-black px-8 py-3.5 rounded-full text-[15px] font-semibold transition-all active:scale-95 shadow-xl flex items-center group">
            <svg class="w-4 h-4 mr-2 group-hover:rotate-90 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
            <span>Create Agent</span>
          </NuxtLink>
        </div>
      </div>

      <!-- Ecosystem Content -->
      <div class="mt-6">
        <div v-if="loading" class="flex flex-col items-center justify-center py-32 border border-[#222] bg-[#050505]/50 backdrop-blur-sm rounded-3xl group relative overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full animate-[shimmer_2s_infinite]"></div>
          <div class="w-12 h-12 border-2 border-[#333] border-t-[#A855F7] rounded-full animate-spin mb-6"></div>
          <p class="text-[#A1A1AA] text-[11px] font-bold uppercase tracking-[0.2em]">Loading agents...</p>
        </div>
        
        <div v-else-if="error" class="text-red-400 text-center py-10 bg-red-900/10 border border-red-500/20 rounded-2xl text-[14px] font-medium">{{ error }}</div>
        
        <div v-else-if="bots.length === 0" class="text-center py-32 border border-[#222] bg-[#050505]/50 backdrop-blur-sm rounded-3xl group shadow-inner">
          <div class="w-20 h-20 bg-[#111] border border-[#222] rounded-3xl flex items-center justify-center mx-auto mb-8 group-hover:scale-110 group-hover:bg-[#1A1A1A] group-hover:border-[#333] transition-all duration-500 shadow-xl">
            <svg class="w-8 h-8 text-[#A1A1AA] group-hover:text-[#A855F7] transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 012-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          </div>
          <p class="text-[#A1A1AA] text-[15px] mb-8 font-medium">No agents yet. Create your first one!</p>
          <NuxtLink to="/bots/new" class="text-[#A855F7] font-semibold hover:text-purple-400 text-[13px] uppercase tracking-widest inline-flex items-center group/btn transition-colors">
            Create Your First Agent <svg class="w-4 h-4 ml-1 transform group-hover/btn:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
          </NuxtLink>
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="bot in bots" :key="bot.id" class="bg-[#050505]/90 border border-[#222] hover:border-[#444] rounded-3xl p-10 group hover:-translate-y-1 transition-all relative overflow-hidden shadow-[0_10px_40px_rgba(0,0,0,0.5)] backdrop-blur-xl">
            <!-- Subtle gradient overlay -->
            <div class="absolute top-0 right-0 w-48 h-48 bg-white/[0.01] blur-[60px] group-hover:bg-white/[0.03] transition-all duration-700 pointer-events-none"></div>
            
            <div class="flex items-start justify-between mb-10 relative z-10">
              <div class="w-16 h-16 rounded-[20px] bg-[#111] border border-[#222] flex items-center justify-center text-[#888] shadow-inner">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
              </div>
              <div class="flex items-center space-x-2 bg-[#111] px-3 py-1.5 rounded-full border border-[#222] shadow-sm">
                 <div class="w-2 h-2 rounded-full animate-pulse" :class="bot.is_active ? 'bg-[#A855F7] shadow-[0_0_8px_rgba(168,85,247,0.8)]' : 'bg-[#333]'"></div>
                 <span class="text-[9px] font-bold uppercase tracking-[0.2em]" :class="bot.is_active ? 'text-[#E4E4E5]' : 'text-[#888]'">
                   {{ bot.is_active ? 'Active' : 'Standby' }}
                 </span>
              </div>
            </div>
            
            <div class="relative z-10">
              <h3 class="text-[24px] font-semibold text-white mb-3 truncate tracking-tight">{{ bot.name }}</h3>
              <p class="text-[10px] text-[#A1A1AA] font-bold uppercase tracking-[0.2em] mb-12">Agent Active</p>
              
              <div class="space-y-5 pt-8 border-t border-[#222]">
                <div class="flex items-center justify-between">
                  <span class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-wider">Telegram Bot</span>
                  <span class="text-[14px] font-medium text-[#E4E4E5] tracking-tight">@{{ bot.username || 'Agent' }}</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-wider">Signal Priority</span>
                  <span class="text-[12px] font-bold uppercase tracking-widest" :class="bot.token ? 'text-white' : 'text-[#888]'">{{ bot.token ? 'L-9 Secured' : 'Unsecured' }}</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-wider">Established</span>
                  <span class="text-[14px] font-medium text-[#E4E4E5] tracking-tight">{{ new Date(bot.created_at).toLocaleDateString() }}</span>
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
    error.value = 'Failed to load agents. Please try again.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>
