<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-[#080808] text-[#EDEDED] p-6 font-sans relative selection:bg-white/20 overflow-hidden">
    <!-- Sophisticated background pattern -->
    <div class="absolute inset-0 z-0 opacity-[0.03] pointer-events-none" style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 40px 40px;"></div>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-white/[0.01] blur-[120px] rounded-full pointer-events-none z-0"></div>

    <div class="max-w-sm w-full relative z-10">
      <div class="text-center mb-16">
        <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mx-auto mb-10 shadow-[0_0_50px_rgba(255,255,255,0.1)] group hover:scale-110 transition-transform duration-500 cursor-pointer">
          <div class="w-5 h-5 bg-black rounded-sm"></div>
        </div>
        <h2 class="text-3xl font-semibold tracking-tighter text-white">Welcome Back</h2>
        <p class="text-[14px] text-[#888888] mt-3 font-medium">Sign in to your account</p>
      </div>

      <div class="wope-card p-10 bg-[#0C0C0C]/80 backdrop-blur-3xl shadow-2xl">
        <form @submit.prevent="handleLogin" class="space-y-8">
          <div class="space-y-6">
            <div class="space-y-3">
              <label class="text-[10px] font-black text-[#4B5563] uppercase tracking-[0.2em] ml-1">Email</label>
              <input v-model="username" type="text" required placeholder="Enter your email" 
                class="w-full bg-[#0E0E0E] border border-white/5 rounded-2xl px-5 py-4 text-[14px] text-white focus:border-white/20 outline-none transition-all placeholder-[#262626] font-medium tracking-tight">
            </div>

            <div class="space-y-3">
              <label class="text-[10px] font-black text-[#4B5563] uppercase tracking-[0.2em] ml-1">Password</label>
              <input v-model="password" type="password" required placeholder="••••••••" 
                class="w-full bg-[#0E0E0E] border border-white/5 rounded-2xl px-5 py-4 text-[14px] text-white focus:border-white/20 outline-none transition-all placeholder-[#262626] tracking-tight">
            </div>
          </div>

          <button type="submit" :disabled="loading" 
            class="wope-button-primary w-full !py-4 !text-[13px] shadow-xl disabled:opacity-20">
            {{ loading ? 'Signing in...' : 'Sign In' }}
          </button>

          <div v-if="error" class="text-red-500 text-center text-[12px] font-bold uppercase tracking-wide animate-pulse">
            {{ error }}
          </div>

          <div class="relative py-4">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-white/5"></div>
            </div>
            <div class="relative flex justify-center">
              <span class="px-4 bg-[#0C0C0C] text-[9px] font-black text-[#4B5563] uppercase tracking-[0.34em]">Or continue with</span>
            </div>
          </div>

          <div class="flex justify-center">
            <GoogleLogin :callback="onGoogleSuccess" :error="onGoogleError" />
          </div>

          <p class="text-center text-[13px] text-[#4B5563] font-medium pt-4">
            Don't have an account? <NuxtLink to="/register" class="text-white hover:underline font-bold">Sign Up</NuxtLink>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '~/stores/auth';
import { useRouter } from 'vue-router';
import { GoogleLogin, decodeCredential } from 'vue3-google-login';

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
    error.value = 'Invalid email or password. Please try again.';
  } finally {
    loading.value = false;
  }
};

const onGoogleSuccess = async (response: any) => {
  if (response.credential) {
    try {
      loading.value = true;
      error.value = '';
      await auth.googleLogin(response.credential, 'id_token');
      router.push('/');
    } catch (err: any) {
      error.value = 'Google login failed. Please try again.';
    } finally {
      loading.value = false;
    }
  } else {
    error.value = 'Google login failed. No credential received.';
  }
};

const onGoogleError = () => {
  error.value = 'Google login failed. Please try again.';
};
</script>
