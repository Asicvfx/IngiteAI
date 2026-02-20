<template>
  <div class="min-h-screen bg-[#080808] text-[#EDEDED] flex flex-col md:flex-row font-sans selection:bg-white/20">
    <!-- Sidebar -->
    <aside class="w-full md:w-64 bg-[#080808] border-r border-white/5 flex flex-col z-50">
      <div class="p-8 flex items-center space-x-3 mb-6">
        <div class="w-7 h-7 bg-white rounded-lg flex items-center justify-center">
           <div class="w-2.5 h-2.5 bg-black"></div>
        </div>
        <span class="text-base font-semibold tracking-tighter text-white">Ingite</span>
      </div>
      
      <nav class="flex-1 px-4 space-y-1">
        <NuxtLink v-for="item in navItems" :key="item.to" :to="item.to" 
          class="flex items-center px-4 py-2.5 rounded-xl transition-all duration-200 group relative"
          :class="[
            isActive(item.to) 
              ? 'bg-white/5 text-white' 
              : 'text-[#888888] hover:text-white hover:bg-white/[0.02]'
          ]"
        >
          <div v-if="isActive(item.to)" class="absolute left-0 w-1 h-4 bg-white rounded-full"></div>
          <div class="mr-4 opacity-60 group-hover:opacity-100 transition-opacity" v-html="item.icon"></div>
          <span class="text-[13px] font-medium tracking-tight">{{ item.label }}</span>
        </NuxtLink>
      </nav>

      <div class="p-6">
        <button @click="handleLogout" class="flex items-center w-full px-4 py-3 rounded-xl text-[#4B5563] hover:text-red-400 hover:bg-red-400/5 transition-all text-[13px] font-medium group">
          <svg class="w-4 h-4 mr-4 opacity-40 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          Sign Out
        </button>
      </div>
    </aside>

    <!-- Main Content Container -->
    <main class="flex-1 flex flex-col h-screen overflow-hidden relative bg-[#080808]">
      <header class="h-20 border-b border-white/5 flex items-center justify-between px-10 z-40 bg-[#080808]/80 backdrop-blur-xl">
        <div class="flex items-center space-x-2">
           <span class="text-[12px] font-semibold text-white/40 tracking-widest uppercase">Secure Node Active</span>
        </div>
        
        <div class="flex items-center space-x-6">
          <div class="flex flex-col items-end">
            <span class="text-[12px] font-semibold text-white tracking-tight">{{ auth.user?.username || 'Administrator' }}</span>
          </div>
          <div class="w-9 h-9 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center overflow-hidden group hover:border-white/20 transition-all cursor-pointer">
             <span class="text-white font-semibold text-[13px] uppercase group-hover:scale-110 transition-transform">{{ auth.user?.username?.[0] || 'A' }}</span>
          </div>
        </div>
      </header>
      
      <div class="flex-1 overflow-y-auto wope-scroll bg-[#080808]">
        <slot />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth';
import { useRoute, useRouter } from 'vue-router';

const auth = useAuthStore();
const route = useRoute();
const router = useRouter();

const navItems = [
  { to: '/', label: 'Overview', icon: '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>' },
  { to: '/chats', label: 'Streams', icon: '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>' },
  { to: '/bots', label: 'Agents', icon: '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 012-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>' },
  { to: '/faq', label: 'Intelligence', icon: '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>' },
  { to: '/settings', label: 'Settings', icon: '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>' }
];

const isActive = (path: string) => {
  if (path === '/') return route.path === '/';
  return route.path.startsWith(path);
};

const handleLogout = () => {
  auth.logout();
  router.push('/login');
};
</script>

<style>
.wope-scroll::-webkit-scrollbar {
  width: 5px;
}
.wope-scroll::-webkit-scrollbar-track {
  background: transparent;
}
.wope-scroll::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 10px;
}
.wope-scroll::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.08);
}
</style>
