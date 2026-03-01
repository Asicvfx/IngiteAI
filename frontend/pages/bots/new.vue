<template>
  <div class="px-6 md:px-12 py-24 min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden flex flex-col items-center justify-center">

    <div class="max-w-xl w-full relative z-10">
      <div class="mb-20 text-center">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] text-white">Create New Assistant</h1>
        <p class="mt-4 text-[#A1A1AA] text-[15px] leading-relaxed font-medium">
          Connect your messaging channels to automate customer conversations.
        </p>
      </div>

      <div class="bg-[#050505]/80 border border-[#222] rounded-3xl p-12 backdrop-blur-xl shadow-2xl relative overflow-hidden group">
        <!-- Subtle hover glow -->
        <div class="absolute -top-32 -right-32 w-64 h-64 bg-white/[0.02] blur-[40px] rounded-full group-hover:bg-[#A855F7]/10 transition-colors duration-1000 -z-10"></div>
        
        <form @submit.prevent="handleConnect" class="space-y-10 relative z-10">
          <!-- Agent Name -->
          <div class="space-y-4">
            <label for="name" class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-[0.2em]">Agent Identity</label>
            <input v-model="name" type="text" id="name" required 
              class="w-full bg-[#111] border border-[#222] rounded-2xl px-6 py-4 text-[15px] text-white focus:border-[#444] focus:ring-1 focus:ring-[#A855F7]/50 outline-none transition-all placeholder-[#444] font-medium tracking-tight shadow-inner" 
              placeholder="e.g. Support Prime">
          </div>

          <!-- Telegram Section -->
          <div class="space-y-4 p-6 border border-[#222] rounded-2xl bg-[#0a0a0a]/50">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-8 h-8 rounded-lg bg-[#229ED9]/20 flex items-center justify-center">
                <svg class="w-4 h-4 text-[#229ED9]" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.03-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
              </div>
              <span class="text-[12px] font-bold text-[#A1A1AA] uppercase tracking-[0.15em]">Telegram Bot</span>
            </div>
            <div class="relative">
              <input v-model="token" type="text" id="token" required 
                class="w-full bg-[#111] border border-[#222] rounded-xl px-5 py-3.5 text-[14px] font-mono text-white focus:border-[#444] focus:ring-1 focus:ring-[#229ED9]/50 outline-none transition-all placeholder-[#444] tracking-tight shadow-inner" 
                placeholder="123456:ABC-DEF...">
            </div>
            <p class="text-[10px] text-[#555] font-medium uppercase tracking-widest">Token from @BotFather</p>
          </div>

          <!-- WhatsApp Section -->
          <div class="space-y-4 p-6 border border-[#222] rounded-2xl bg-[#0a0a0a]/50">
            <div class="flex items-center justify-between mb-4">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-[#25D366]/20 flex items-center justify-center">
                  <svg class="w-4 h-4 text-[#25D366]" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                </div>
                <span class="text-[12px] font-bold text-[#A1A1AA] uppercase tracking-[0.15em]">WhatsApp</span>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" v-model="whatsappEnabled" class="sr-only peer">
                <div class="w-9 h-5 bg-[#222] peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-[#555] after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-[#25D366]/30 peer-checked:after:bg-[#25D366]"></div>
              </label>
            </div>
            
            <div v-if="whatsappEnabled" class="space-y-4 animate-[fadeIn_0.3s_ease]">
              <div>
                <input v-model="whatsappPhoneId" type="text" 
                  class="w-full bg-[#111] border border-[#222] rounded-xl px-5 py-3.5 text-[14px] font-mono text-white focus:border-[#444] focus:ring-1 focus:ring-[#25D366]/50 outline-none transition-all placeholder-[#444] tracking-tight shadow-inner" 
                  placeholder="Phone Number ID (from Meta Dashboard)">
              </div>
              <div>
                <textarea v-model="whatsappToken" rows="3"
                  class="w-full bg-[#111] border border-[#222] rounded-xl px-5 py-3.5 text-[14px] font-mono text-white focus:border-[#444] focus:ring-1 focus:ring-[#25D366]/50 outline-none transition-all placeholder-[#444] tracking-tight shadow-inner resize-none" 
                  placeholder="Access Token (from Meta Dashboard)"></textarea>
              </div>
              <p class="text-[10px] text-[#555] font-medium uppercase tracking-widest">From Meta Developer Dashboard → WhatsApp → API Setup</p>
            </div>
            <p v-else class="text-[10px] text-[#444] font-medium">Enable to connect WhatsApp Business</p>
          </div>

          <!-- Submit -->
          <div class="pt-4 border-t border-[#222]">
            <button type="submit" :disabled="loading" 
              class="w-full bg-white hover:bg-gray-200 text-black py-4 rounded-xl text-[14px] font-semibold transition-all active:scale-95 shadow-xl disabled:opacity-30 disabled:hover:bg-white disabled:scale-100 flex justify-center items-center">
              <span v-if="loading" class="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin mr-2"></span>
              {{ loading ? 'Creating...' : 'Create Agent' }}
            </button>
            
            <NuxtLink to="/bots" class="block text-center mt-10 text-[11px] font-bold text-[#A1A1AA] hover:text-[#E4E4E5] transition-all uppercase tracking-[0.2em] group/link">
              <span class="opacity-40 group-hover/link:opacity-100 transition-opacity group-hover/link:-translate-x-1 inline-block">&lsaquo;</span> Return to Ecosystem
            </NuxtLink>
          </div>

          <div v-if="error" class="mt-4 p-5 border border-red-500/20 bg-red-900/10 rounded-2xl text-red-400 text-[13px] font-semibold text-center animate-pulse">
            {{ error }}
          </div>
        </form>
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
const whatsappEnabled = ref(false);
const whatsappPhoneId = ref('');
const whatsappToken = ref('');
const loading = ref(false);
const error = ref('');

const handleConnect = async () => {
  loading.value = true;
  error.value = '';
  try {
    const body: any = { name: name.value, token: token.value };
    if (whatsappEnabled.value) {
      body.whatsapp_phone_number_id = whatsappPhoneId.value;
      body.whatsapp_access_token = whatsappToken.value;
      body.whatsapp_enabled = true;
    }
    await $fetch(`${config.public.apiBaseUrl}/api/v1/bots/`, {
      method: 'POST',
      body,
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

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-8px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
