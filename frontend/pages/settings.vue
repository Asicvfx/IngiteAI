<template>
  <div class="px-10 py-12 bg-black min-h-[calc(100vh-56px)] text-white font-sans relative">
    <div class="max-w-3xl mx-auto">
      <div class="mb-16">
        <h1 class="text-3xl font-semibold tracking-[-0.022em]">Settings</h1>
        <p class="mt-2 text-[#6B7280] text-[14px]">Manage your business synchronization and security protocols.</p>
      </div>

      <div class="space-y-12">
        <!-- Profile Section -->
        <section class="space-y-6">
          <h2 class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em] px-1">Business Profile</h2>
          <div class="p-8 bg-black border border-[#1A1A1A] rounded-2xl space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-2">
                <label class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em]">Brand Name</label>
                <input v-model="business.name" type="text" class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all placeholder-[#262626]">
              </div>
              <div class="space-y-2">
                <label class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em]">Support Channel</label>
                <input v-model="business.email" type="email" class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all placeholder-[#262626]">
              </div>
            </div>
            
            <div class="flex justify-start">
              <button @click="updateBusiness" class="px-8 py-3 bg-white text-black text-[13px] font-semibold rounded-xl hover:bg-gray-200 transition active:scale-95">
                 Update Identity
              </button>
            </div>
          </div>
        </section>

        <!-- Security Section -->
        <section class="space-y-6">
          <h2 class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em] px-1">Security & Sessions</h2>
          <div class="p-8 bg-black border border-[#1A1A1A] rounded-2xl">
            <div class="flex items-center justify-between">
              <div>
                <h3 class="text-[14px] font-medium text-white mb-1">Session Termination</h3>
                <p class="text-[12px] text-[#6B7280]">Sign out of the current administrative session.</p>
              </div>
              <button @click="logout" class="px-6 py-2 border border-red-500/20 text-red-400 text-[12px] font-medium rounded-lg hover:bg-red-400/5 transition">
                Sign Out
              </button>
            </div>
          </div>
        </section>
      </div>
      
      <div class="mt-20 text-center opacity-10">
        <span class="text-[10px] uppercase font-medium tracking-[1em]">Ingite Terminal v1.1</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '~/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

const business = ref({
  name: 'VelorAI Enterprise',
  email: 'ops@velor.ai'
});

const updateBusiness = () => {
  alert('Data synchronized.');
};

const logout = () => {
  auth.logout();
  router.push('/login');
};
</script>
