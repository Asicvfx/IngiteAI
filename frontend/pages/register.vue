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
        <h2 class="text-3xl font-semibold tracking-tighter text-white">Create Account</h2>
        <p class="text-[14px] text-[#888888] mt-3 font-medium">Sign up to get started</p>
      </div>

      <div class="wope-card p-10 bg-[#0C0C0C]/80 backdrop-blur-3xl shadow-2xl">
        <form @submit.prevent="handleRegister" class="space-y-8">
          <div class="space-y-6">
            <div class="space-y-3">
              <label class="text-[10px] font-black text-[#4B5563] uppercase tracking-[0.2em] ml-1">Username</label>
              <input v-model="username" type="text" required placeholder="Choose a username" 
                class="w-full bg-[#0E0E0E] border border-white/5 rounded-2xl px-5 py-4 text-[14px] text-white focus:border-white/20 outline-none transition-all placeholder-[#262626] font-medium tracking-tight">
            </div>

            <div class="space-y-3">
              <label class="text-[10px] font-black text-[#4B5563] uppercase tracking-[0.2em] ml-1">Email</label>
              <input v-model="email" type="email" required placeholder="user@example.com" 
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
            {{ loading ? 'Creating account...' : 'Sign Up' }}
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

          <div class="flex justify-center group/google">
            <button @click="loginWithGoogle" type="button" class="group-hover/google:opacity-100 opacity-60 flex items-center gap-3 bg-white/5 hover:bg-white/10 px-6 py-3 rounded-xl border border-white/5 transition-all">
              <svg class="w-5 h-5" viewBox="0 0 24 24">
                <path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
                <path fill="currentColor" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-1 .67-2.28 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
                <path fill="currentColor" d="M5.84 14.09c-.22-.67-.35-1.39-.35-2.09s.13-1.42.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" />
                <path fill="currentColor" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
              </svg>
              <span class="text-[13px] font-bold">Continue with Google</span>
            </button>
          </div>

          <p class="text-center text-[13px] text-[#4B5563] font-medium pt-4">
            Already have an account? <NuxtLink to="/login" class="text-white hover:underline font-bold">Sign In</NuxtLink>
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

const auth = useAuthStore();
const router = useRouter();
const config = useRuntimeConfig();

const username = ref('');
const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref('');

const handleRegister = async () => {
  loading.value = true;
  error.value = '';
  try {
    await auth.register({ 
      username: username.value, 
      email: email.value, 
      password1: password.value,
      password2: password.value 
    });
    router.push('/login');
  } catch (err: any) {
    error.value = 'Registration failed. This email may already be in use.';
  } finally {
    loading.value = false;
  }
};

const loginWithGoogle = () => {
  error.value = '';
  
  // Load Google GSI script if not already loaded
  if (typeof google === 'undefined' || !google.accounts) {
    const script = document.createElement('script');
    script.src = 'https://accounts.google.com/gsi/client';
    script.async = true;
    script.defer = true;
    script.onload = () => {
      initiateGoogleLogin();
    };
    script.onerror = () => {
      error.value = 'Failed to load Google. Please try again.';
    };
    document.head.appendChild(script);
  } else {
    initiateGoogleLogin();
  }
};

const initiateGoogleLogin = () => {
  try {
    const client = google.accounts.oauth2.initTokenClient({
      client_id: config.public.googleClientId,
      scope: 'email profile openid',
      callback: async (tokenResponse: any) => {
        if (tokenResponse.access_token) {
          try {
            loading.value = true;
            error.value = '';
            await auth.googleLogin(tokenResponse.access_token, 'access_token');
            router.push('/');
          } catch (err: any) {
            error.value = 'Google registration failed. Please try again.';
          } finally {
            loading.value = false;
          }
        } else {
          error.value = 'Google authentication cancelled.';
        }
      },
    });
    client.requestAccessToken();
  } catch (err) {
    console.error('Google login error:', err);
    error.value = 'Google login error. Please try again.';
  }
};

declare const google: any;
</script>
