<template>
  <div class="px-6 md:px-12 py-16 bg-[#080808] min-h-[calc(100vh-56px)] text-white font-sans relative">
    <div class="max-w-2xl mx-auto">
      <div class="mb-20">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] gradient-text">Settings</h1>
        <p class="mt-4 text-[#888888] text-[15px] leading-relaxed">
          Configure your administrative preferences and security tokens.
        </p>
      </div>

      <div class="space-y-16">
        <!-- Account Section -->
        <section class="space-y-8">
          <div class="flex items-center space-x-2 px-1">
            <span class="w-1 h-1 bg-white rounded-full"></span>
            <h2 class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em]">Administrative Account</h2>
          </div>
          
          <div class="wope-card p-1">
            <div class="flex items-center justify-between p-6">
              <div class="flex items-center space-x-4">
                <div class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-[13px] font-semibold text-white">
                  {{ auth.user?.username?.charAt(0).toUpperCase() || 'A' }}
                </div>
                <div>
                  <p class="text-[14px] font-medium text-white">{{ auth.user?.username || 'Administrator' }}</p>
                  <p class="text-[12px] text-[#888888]">{{ auth.user?.email || 'ops@research.lab' }}</p>
                </div>
              </div>
              <button @click="logout" class="wope-button-secondary !py-2 !px-4 text-[12px] border-red-500/10 text-red-400 hover:bg-red-400/5">
                Sign Out
              </button>
            </div>
          </div>
        </section>

        <!-- Security Section -->
        <section class="space-y-8">
          <div class="flex items-center space-x-2 px-1">
            <span class="w-1 h-1 bg-white/20 rounded-full"></span>
            <h2 class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em]">Security Protocol</h2>
          </div>
          
          <div class="wope-card p-8 space-y-8">
             <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-[14px] font-medium text-white mb-1">Two-Factor Authentication</h3>
                  <p class="text-[12px] text-[#888888]">Add an extra layer of security to your node access.</p>
                </div>
                <div class="w-10 h-5 bg-[#1A1A1A] rounded-full relative cursor-not-allowed">
                  <div class="absolute left-1 top-1 w-3 h-3 bg-[#404040] rounded-full"></div>
                </div>
             </div>
             
             <div class="pt-8 border-t border-white/5">
                <h3 class="text-[14px] font-medium text-white mb-4">Neural Access Key</h3>
                <div class="flex items-center space-x-3">
                  <input type="password" value="••••••••••••••••••••••••" readonly 
                    class="flex-1 wope-input !bg-white/[0.02] border-dashed text-[#404040] cursor-default">
                  <button class="wope-button-secondary !py-3">Rotate</button>
                </div>
             </div>
          </div>
        </section>
      </div>
      
      <div class="mt-32 text-center opacity-10">
        <span class="text-[10px] uppercase font-medium tracking-[1em]">Ingite v1.2.0</span>
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
