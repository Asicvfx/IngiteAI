<template>
  <div class="min-h-screen bg-[#000000] text-[#EDEDED] font-sans selection:bg-white/20">
    <!-- WebGL Background -->
    <ClientOnly>
      <WebGLShader />
    </ClientOnly>

    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 border-b border-white/5 px-6 py-4" style="backdrop-filter: blur(16px); background: rgba(0,0,0,0.4);">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-8 h-8 bg-white rounded-lg flex items-center justify-center">
            <div class="w-3 h-3 bg-black"></div>
          </div>
          <span class="text-lg font-semibold tracking-tighter">IngiteAI</span>
        </div>
        <div class="hidden md:flex items-center space-x-8 text-[13px] font-medium text-[#888888]">
          <a href="#features" class="hover:text-white transition-colors">Intelligence</a>
          <a href="#vision" class="hover:text-white transition-colors">Vision</a>
          <a href="#workflow" class="hover:text-white transition-colors">Workflow</a>
        </div>
        <div class="flex items-center space-x-4">
          <NuxtLink to="/login" class="text-[13px] font-medium hover:text-white transition-colors">Sign in</NuxtLink>
          <NuxtLink to="/register" class="bg-white text-black px-4 py-2 rounded-lg text-[13px] font-semibold hover:bg-gray-200 transition-all active:scale-95">Get Started</NuxtLink>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="relative pt-40 pb-20 px-6 overflow-hidden">
      <div class="relative z-10 border border-[#27272a] p-2 max-w-3xl mx-auto">
        <main class="relative border border-[#27272a] py-16 overflow-hidden" style="background: rgba(0,0,0,0.3); backdrop-filter: blur(8px);">
          <h1 class="mb-4 text-white text-center text-5xl md:text-7xl lg:text-[clamp(2rem,8vw,7rem)] font-extrabold tracking-tighter leading-[0.95]">
            Direct your business<br />with AI precision
          </h1>
          <p class="text-white/50 px-6 text-center text-sm md:text-base lg:text-lg max-w-2xl mx-auto leading-relaxed">
            An automated intelligence layer that connects your business to a self-learning AI agent. Minimize noise, maximize signal.
          </p>
          
          <div class="my-8 flex items-center justify-center gap-1.5">
            <span class="relative flex h-3 w-3 items-center justify-center">
              <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-500 opacity-75"></span>
              <span class="relative inline-flex h-2 w-2 rounded-full bg-green-500"></span>
            </span>
            <p class="text-xs text-green-500 font-medium">AI-Powered • 24/7 Active</p>
          </div>

          <div class="flex flex-col sm:flex-row justify-center items-center gap-4 px-6">
            <NuxtLink to="/register">
              <LiquidButton size="xl" class="text-white border border-white/20 rounded-full">
                Get Started
              </LiquidButton>
            </NuxtLink>
            <NuxtLink to="/login">
              <LiquidButton size="xl" class="text-white/70 border border-white/10 rounded-full">
                Sign In
              </LiquidButton>
            </NuxtLink>
          </div>
        </main>
      </div>
    </header>

    <!-- Features Bento Grid -->
    <section id="features" class="relative z-10 py-32 px-6">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
          <!-- Main Bento -->
          <div class="md:col-span-8 border border-white/10 rounded-3xl p-10 relative overflow-hidden group" style="background: rgba(10,10,10,0.7); backdrop-filter: blur(12px);">
            <div class="absolute top-0 right-0 w-64 h-64 bg-white/[0.03] blur-[80px] group-hover:bg-white/[0.06] transition-all"></div>
            <div class="relative z-10">
              <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              </div>
              <h3 class="text-3xl font-semibold mb-4">Smart Knowledge Base</h3>
              <p class="text-[#888888] text-lg max-w-md leading-relaxed">
                Simply drop your business assets—PDFs, catalogs, or raw text—and watch your agents learn your domain expertise instantly.
              </p>
            </div>
            <div class="mt-12 p-6 bg-black/40 border border-white/5 rounded-2xl">
              <div class="flex items-center space-x-4 mb-4">
                <div class="w-3 h-3 rounded-full bg-white/20"></div>
                <div class="w-20 h-2 bg-white/10 rounded-full"></div>
              </div>
              <div class="space-y-2 opacity-50">
                <div class="w-full h-1 bg-white/5 rounded-full"></div>
                <div class="w-2/3 h-1 bg-white/5 rounded-full"></div>
              </div>
            </div>
          </div>

          <!-- Small Bento 1 -->
          <div class="md:col-span-4 border border-white/10 rounded-3xl p-10 flex flex-col justify-between" style="background: rgba(10,10,10,0.7); backdrop-filter: blur(12px);">
            <div>
              <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4">24/7 Agent Autonomy</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Your agents never sleep. They handle inquiries, qualify leads, and process data around the clock.
              </p>
            </div>
          </div>

          <!-- Small Bento 2 -->
          <div class="md:col-span-4 border border-white/10 rounded-3xl p-10 flex flex-col justify-between" style="background: rgba(10,10,10,0.7); backdrop-filter: blur(12px);">
            <div>
              <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4">Signal Analytics</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Transform conversations into data. Monitor sentiment, classification, and growth in real-time.
              </p>
            </div>
          </div>

          <!-- Medium Bento -->
          <div class="md:col-span-8 border border-white/10 rounded-3xl p-10 relative overflow-hidden group" style="background: rgba(10,10,10,0.7); backdrop-filter: blur(12px);">
            <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
              <div class="max-w-sm">
                <h3 class="text-3xl font-semibold mb-4">Global Communication</h3>
                <p class="text-[#888888] text-[16px] leading-relaxed">
                  Bridge the gap between your brand and your audience on any channel. Telegram, WhatsApp, and beyond.
                </p>
              </div>
              <div class="flex -space-x-4">
                <div class="w-16 h-16 rounded-full border-4 border-black bg-[#229ED9]/20 flex items-center justify-center text-xl font-bold text-[#229ED9]">T</div>
                <div class="w-16 h-16 rounded-full border-4 border-black bg-[#25D366]/20 flex items-center justify-center text-xl font-bold text-[#25D366]">W</div>
                <div class="w-16 h-16 rounded-full border-4 border-black bg-white/10 flex items-center justify-center text-xl font-bold text-white/60">+</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="relative z-10 py-40 px-6 text-center">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-5xl font-semibold mb-8 tracking-tighter text-white">Ready to get started?</h2>
        <p class="text-xl text-[#888888] mb-12">Start your journey into high-clarity business intelligence today.</p>
        <NuxtLink to="/register">
          <LiquidButton size="xxl" class="text-white border border-white/20 rounded-full text-lg">
            Get Started
          </LiquidButton>
        </NuxtLink>
      </div>
    </section>

    <!-- Footer -->
    <footer class="relative z-10 py-20 px-6 border-t border-white/5">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center space-y-8 md:space-y-0 text-[#888888] text-[13px]">
        <div class="flex items-center space-x-3">
          <div class="w-6 h-6 bg-white/10 rounded flex items-center justify-center">
            <div class="w-2 h-2 bg-white"></div>
          </div>
          <span class="font-semibold text-white">IngiteAI</span>
        </div>
        <div class="flex items-center space-x-12">
          <a href="#" class="hover:text-white transition-colors">Privacy</a>
          <a href="#" class="hover:text-white transition-colors">Security</a>
          <a href="#" class="hover:text-white transition-colors">GitHub</a>
        </div>
        <div>
          © 2026 IngiteAI. All rights reserved.
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import WebGLShader from '~/components/ui/WebGLShader.vue'
import LiquidButton from '~/components/ui/LiquidButton.vue'

definePageMeta({
  layout: false
});
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 1s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>

