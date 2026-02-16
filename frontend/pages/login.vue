<template>
  <div class="min-h-screen flex items-center justify-center bg-black text-white p-6 font-sans relative selection:bg-white/20">
    <div class="max-w-sm w-full relative z-10">
      <div class="text-center mb-12">
        <div class="w-12 h-12 bg-[#0D0D0D] border border-[#1A1A1A] rounded-xl flex items-center justify-center mx-auto mb-8">
          <div class="w-5 h-5 bg-white rounded-sm"></div>
        </div>
        <h2 class="text-2xl font-semibold tracking-[-0.022em] text-white">IngiteAI</h2>
        <p class="text-[13px] text-[#6B7280] mt-2">Sign in to your dashboard</p>
      </div>

      <div class="p-8 bg-black border border-[#1A1A1A] rounded-2xl">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <div class="space-y-4">
            <div class="space-y-2">
              <label class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em] ml-1">Identity</label>
              <input v-model="username" type="text" required placeholder="Codename or Email" 
                class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all placeholder-[#262626]">
            </div>

            <div class="space-y-2">
              <label class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em] ml-1">Key</label>
              <input v-model="password" type="password" required placeholder="••••••••" 
                class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all placeholder-[#262626]">
            </div>
          </div>

          <button type="submit" :disabled="loading" 
            class="w-full bg-white text-black py-3 rounded-xl font-semibold text-[13px] transition-all hover:bg-gray-200 active:scale-95 disabled:opacity-50">
            {{ loading ? 'Signing in...' : 'Sign in' }}
          </button>

          <div v-if="error" class="text-red-400 text-center text-[12px] font-medium">
            {{ error }}
          </div>

          <div class="relative py-4">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-[#1A1A1A]"></div>
            </div>
            <div class="relative flex justify-center">
              <span class="px-4 bg-black text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.1em]">or login with</span>
            </div>
          </div>

          <div class="flex justify-center">
             <GoogleLogin popup-type="TOKEN" :callback="handleGoogleLogin" />
          </div>

          <p class="text-center text-[13px] text-[#6B7280]">
            No account? <NuxtLink to="/register" class="text-white hover:underline">Create one</NuxtLink>
          </p>
        </form>
      </div>
      
      <div class="mt-12 text-center opacity-5">
        <span class="text-[10px] uppercase font-medium tracking-[1em]">Ingite v1.1</span>
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

const username = ref('');
const password = ref('');
const loading = ref(false);
const error = ref('');

const handleLogin = async () => {
  loading.value = true;
  error.value = '';
  try {
    await auth.login({ username: username.value, password: password.value });
    router.push('/');
  } catch (err: any) {
    error.value = 'Identity mismatch. Please try again.';
  } finally {
    loading.value = false;
  }
};

const handleGoogleLogin = async (response: any) => {
  if (response.access_token) {
    try {
      loading.value = true;
      await auth.googleLogin(response.access_token);
      router.push('/');
    } catch (err: any) {
      error.value = 'External synchronization failed.';
    } finally {
      loading.value = false;
    }
  } else {
    error.value = 'Security token missing.';
  }
};
</script>
