<template>
  <div class="min-h-screen bg-[#080808] text-[#EDEDED] font-sans selection:bg-white/20">
    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 wope-glass border-b border-white/5 px-6 py-4">
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
          <NuxtLink to="/register" class="wope-button-primary !py-2 !px-4 text-[13px]">Get Started</NuxtLink>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="pt-40 pb-20 px-6 relative overflow-hidden">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[600px] bg-white/[0.02] blur-[120px] rounded-full pointer-events-none"></div>
      
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full border border-white/10 bg-white/5 mb-8 animate-fade-in">
          <span class="w-1.5 h-1.5 rounded-full bg-white"></span>
          <span class="text-[11px] font-medium uppercase tracking-[0.1em] text-[#888888]">Intelligence Synchronized</span>
        </div>
        
        <h1 class="text-6xl md:text-8xl font-semibold tracking-[-0.04em] leading-[0.95] mb-8 gradient-text">
          Direct your business <br /> with neural clarity.
        </h1>
        
        <p class="text-lg md:text-xl text-[#888888] leading-relaxed mb-12 max-w-2xl mx-auto tracking-normal">
          An automated intelligence layer that connects your business assets to a self-learning agent fleet. Minimize noise, maximize signal.
        </p>
        
        <div class="flex flex-col sm:flex-row items-center justify-center space-x-0 sm:space-x-4 space-y-4 sm:space-y-0">
          <NuxtLink to="/register" class="wope-button-primary !px-8 !py-4 text-[15px] w-full sm:w-auto">Initialize Portal</NuxtLink>
          <button class="wope-button-secondary !px-8 !py-4 text-[15px] w-full sm:w-auto">Read Whitepaper</button>
        </div>
      </div>
    </header>

    <!-- Bento Grid Section -->
    <section id="features" class="py-32 px-6">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
          <!-- Main Bento -->
          <div class="md:col-span-8 wope-card p-10 relative overflow-hidden group">
            <div class="absolute top-0 right-0 w-64 h-64 bg-white/[0.03] blur-[80px] group-hover:bg-white/[0.05] transition-all"></div>
            <div class="relative z-10">
               <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
               </div>
               <h3 class="text-3xl font-semibold mb-4">Neural Knowledge Injection</h3>
               <p class="text-[#888888] text-lg max-w-md leading-relaxed">
                 Simply drop your business assets—PDFs, documentation, or raw text—and watch your agents synchronize with your domain expertise instantly.
               </p>
            </div>
            <!-- Visual Element -->
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
          <div class="md:col-span-4 wope-card p-10 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4">24/7 Agent Autonomy</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Your agents never sleep. They handle inquiries, qualify leads, and synchronize data around the clock.
              </p>
            </div>
          </div>

          <!-- Small Bento 2 -->
          <div class="md:col-span-4 wope-card p-10 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4">Signal Analytics</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Transform abstract conversations into concrete data. Monitor sentiment, classification, and growth in real-time.
              </p>
            </div>
          </div>

          <!-- Medium Bento -->
          <div class="md:col-span-8 wope-card p-10 relative overflow-hidden group">
            <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
              <div class="max-w-sm">
                <h3 class="text-3xl font-semibold mb-4">Global Communication</h3>
                <p class="text-[#888888] text-[16px] leading-relaxed">
                  Bridge the gap between your brand and your audience on any channel. Integrated with Telegram and beyond.
                </p>
              </div>
              <div class="flex -space-x-4">
                <div class="w-16 h-16 rounded-full border-4 border-black bg-white/5 flex items-center justify-center text-xl font-bold">T</div>
                <div class="w-16 h-16 rounded-full border-4 border-black bg-white/5 flex items-center justify-center text-xl font-bold">W</div>
                <div class="w-16 h-16 rounded-full border-4 border-black bg-white/5 flex items-center justify-center text-xl font-bold">M</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-40 px-6 text-center">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-5xl font-semibold mb-8 gradient-text tracking-tighter">Ready to synchronize?</h2>
        <p class="text-xl text-[#888888] mb-12">Start your journey into high-clarity business intelligence today.</p>
        <NuxtLink to="/register" class="wope-button-primary !px-12 !py-5 text-lg">Initialize Now</NuxtLink>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-20 px-6 border-t border-white/5">
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
          © 2024 V-Research Laboratory.
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
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
