<template>
  <div class="px-6 md:px-12 py-16 bg-[#0A0A0B] min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden">
    <!-- Huge background glow -->
    <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-gradient-to-br from-[#A855F7]/10 via-[#A855F7]/5 to-transparent rounded-full blur-[150px] pointer-events-none -z-10"></div>
    <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-gradient-to-tr from-[#3B82F6]/10 to-transparent rounded-full blur-[120px] pointer-events-none -z-10"></div>

    <div class="max-w-2xl mx-auto relative z-10 w-full">
      <div class="mb-20">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] text-white">Settings</h1>
        <p class="mt-4 text-[#A1A1AA] text-[15px] leading-relaxed font-medium">
          Configure your administrative preferences and security tokens.
        </p>
      </div>

      <div class="space-y-16">
        <!-- Account Section -->
        <section class="space-y-8">
          <div class="flex items-center space-x-3 px-2 border-l-2 border-[#A855F7]">
            <h2 class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-[0.2em]">Administrative Account</h2>
          </div>
          
          <div class="bg-[#050505]/80 border border-[#222] rounded-3xl overflow-hidden relative shadow-2xl backdrop-blur-xl group hover:border-[#444] transition-colors">
            <!-- Subtle hover glow -->
            <div class="absolute -top-32 -right-32 w-64 h-64 bg-white/[0.02] blur-[40px] rounded-full group-hover:bg-[#A855F7]/5 transition-colors duration-1000 -z-10 pointer-events-none"></div>

            <div class="flex flex-col md:flex-row md:items-center justify-between p-8 md:p-10 gap-6 relative z-10">
              <div class="flex items-center space-x-6">
                <!-- Avatar -->
                <div class="w-16 h-16 rounded-[20px] bg-[#111] border border-[#222] flex items-center justify-center text-[18px] font-bold text-white shadow-inner relative overflow-hidden group-hover:border-[#333] transition-colors group-hover:shadow-[0_0_20px_rgba(168,85,247,0.1)]">
                  <div class="absolute inset-0 bg-gradient-to-br from-[#A855F7]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                  <span class="relative z-10">{{ auth.user?.username?.charAt(0).toUpperCase() || 'A' }}</span>
                </div>
                <!-- Info -->
                <div>
                  <div class="flex items-center space-x-3 mb-1">
                    <p class="text-[18px] font-semibold text-white tracking-tight">{{ auth.user?.username || 'Administrator' }}</p>
                    <span class="bg-[#111] border border-[#222] text-[#A855F7] text-[9px] font-bold uppercase tracking-wider px-2 py-0.5 rounded shadow-sm">L-9 Access</span>
                  </div>
                  <p class="text-[14px] text-[#A1A1AA] font-medium">{{ auth.user?.email || 'ops@research.lab' }}</p>
                </div>
              </div>
              
              <!-- Action -->
              <button @click="logout" class="bg-[#111] hover:bg-red-500/10 text-[#A1A1AA] hover:text-red-400 py-3.5 px-8 rounded-full text-[13px] font-semibold border border-[#222] hover:border-red-500/20 transition-all shadow-sm active:scale-95 whitespace-nowrap">
                Terminate Session
              </button>
            </div>
          </div>
        </section>

      </div>
      
      <div class="mt-32 flex items-center justify-center space-x-4 opacity-30">
        <div class="h-px w-16 bg-gradient-to-r from-transparent to-[#A1A1AA]"></div>
        <span class="text-[10px] uppercase font-bold tracking-[0.4em] text-[#A1A1AA]">Ingite v1.2.0</span>
        <div class="h-px w-16 bg-gradient-to-l from-transparent to-[#A1A1AA]"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

const logout = () => {
  auth.logout();
  router.push('/login');
};
</script>
