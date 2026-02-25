<template>
  <div class="px-6 md:px-12 py-16 min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden flex items-center justify-center">
    <div class="max-w-2xl w-full relative z-10">
      
      <!-- Welcome Header -->
      <div class="text-center mb-16">
        <div class="w-20 h-20 rounded-3xl flex items-center justify-center mx-auto mb-8 overflow-hidden shadow-[0_0_60px_rgba(168,85,247,0.15)]">
          <img src="/logo.png" alt="IngiteAI" class="w-full h-full object-cover" />
        </div>
        <h1 class="text-4xl font-semibold tracking-[-0.04em] text-white mb-4">Welcome to IngiteAI! 👋</h1>
        <p class="text-[#A1A1AA] text-[16px] leading-relaxed font-medium">
          Get started in 3 easy steps
        </p>
      </div>

      <!-- Steps -->
      <div class="space-y-5 mb-12">
        <!-- Step 1 -->
        <NuxtLink to="/bots/new" @click="completeOnboarding" class="block bg-[#050505]/80 border border-[#222] hover:border-[#A855F7]/40 rounded-2xl p-6 group transition-all hover:-translate-y-0.5">
          <div class="flex items-center gap-6">
            <div class="w-12 h-12 bg-[#A855F7]/10 border border-[#A855F7]/20 rounded-xl flex items-center justify-center shrink-0 group-hover:bg-[#A855F7]/20 transition-colors">
              <span class="text-xl font-bold text-[#A855F7]">1</span>
            </div>
            <div class="flex-1">
              <h3 class="text-[16px] font-semibold text-white mb-1">Create your first AI agent</h3>
              <p class="text-[#666] text-[13px]">Give it a name and connect to Telegram</p>
            </div>
            <svg class="w-5 h-5 text-[#444] group-hover:text-[#A855F7] transition-colors shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </div>
        </NuxtLink>

        <!-- Step 2 -->
        <NuxtLink to="/faq" @click="completeOnboarding" class="block bg-[#050505]/80 border border-[#222] hover:border-[#3B82F6]/40 rounded-2xl p-6 group transition-all hover:-translate-y-0.5">
          <div class="flex items-center gap-6">
            <div class="w-12 h-12 bg-[#3B82F6]/10 border border-[#3B82F6]/20 rounded-xl flex items-center justify-center shrink-0 group-hover:bg-[#3B82F6]/20 transition-colors">
              <span class="text-xl font-bold text-[#3B82F6]">2</span>
            </div>
            <div class="flex-1">
              <h3 class="text-[16px] font-semibold text-white mb-1">Add knowledge</h3>
              <p class="text-[#666] text-[13px]">Upload FAQs, docs, or paste your business info</p>
            </div>
            <svg class="w-5 h-5 text-[#444] group-hover:text-[#3B82F6] transition-colors shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </div>
        </NuxtLink>

        <!-- Step 3 -->
        <NuxtLink to="/chats" @click="completeOnboarding" class="block bg-[#050505]/80 border border-[#222] hover:border-[#10B981]/40 rounded-2xl p-6 group transition-all hover:-translate-y-0.5">
          <div class="flex items-center gap-6">
            <div class="w-12 h-12 bg-[#10B981]/10 border border-[#10B981]/20 rounded-xl flex items-center justify-center shrink-0 group-hover:bg-[#10B981]/20 transition-colors">
              <span class="text-xl font-bold text-[#10B981]">3</span>
            </div>
            <div class="flex-1">
              <h3 class="text-[16px] font-semibold text-white mb-1">Start a conversation</h3>
              <p class="text-[#666] text-[13px]">Test your agent live or let customers chat</p>
            </div>
            <svg class="w-5 h-5 text-[#444] group-hover:text-[#10B981] transition-colors shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </div>
        </NuxtLink>
      </div>

      <!-- Skip Button -->
      <div class="text-center">
        <button @click="skipOnboarding" class="text-[#666] hover:text-white text-[13px] font-medium transition-colors">
          Skip for now →
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth';

const auth = useAuthStore();
const config = useRuntimeConfig();
const router = useRouter();

const completeOnboarding = async () => {
  try {
    await $fetch(`${config.public.apiBaseUrl}/api/v1/auth/user/`, {
      method: 'PATCH',
      body: { has_completed_onboarding: true },
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    if (auth.user) auth.user.has_completed_onboarding = true;
  } catch (e) {
    console.error('Failed to complete onboarding', e);
  }
};

const skipOnboarding = async () => {
  await completeOnboarding();
  router.push('/overview');
};
</script>
