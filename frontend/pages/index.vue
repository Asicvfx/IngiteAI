<template>
  <div class="min-h-screen bg-[#080808] text-[#EDEDED] font-sans selection:bg-white/20">
    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 wope-glass border-b border-white/5 px-6 py-4">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-8 h-8 rounded-lg flex items-center justify-center overflow-hidden">
            <img src="/logo.png" alt="IngiteAI" class="w-full h-full object-cover" />
          </div>
          <span class="text-lg font-semibold tracking-tighter">IngiteAI</span>
        </div>
        <div class="hidden md:flex items-center space-x-8 text-[13px] font-medium text-[#888888]">
          <a href="#features" class="hover:text-white transition-colors">Features</a>
          <a href="#how-it-works" class="hover:text-white transition-colors">How It Works</a>
          <NuxtLink to="/pricing" class="hover:text-white transition-colors">Pricing</NuxtLink>
        </div>
        <div class="flex items-center space-x-4">
          <NuxtLink to="/login" class="text-[13px] font-medium hover:text-white transition-colors">Sign In</NuxtLink>
          <NuxtLink to="/register" class="wope-button-primary !py-2 !px-4 text-[13px]">Get Started</NuxtLink>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="pt-40 pb-20 px-6 relative overflow-hidden">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[600px] bg-white/[0.02] blur-[120px] rounded-full pointer-events-none"></div>
      
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full border border-white/10 bg-white/5 mb-8 animate-fade-in">
          <span class="w-1.5 h-1.5 rounded-full bg-[#A855F7]"></span>
          <span class="text-[11px] font-medium uppercase tracking-[0.1em] text-[#888888]">AI-Powered Customer Support</span>
        </div>
        
        <h1 class="text-5xl md:text-7xl font-semibold tracking-[-0.04em] leading-[0.95] mb-8 gradient-text">
          Automate your business<br />with AI agents
        </h1>
        
        <p class="text-lg md:text-xl text-[#888888] leading-relaxed mb-12 max-w-2xl mx-auto tracking-normal">
          Create AI assistants that answer customer questions 24/7, learn from your business data, and handle unlimited conversations.
        </p>
        
        <div class="flex flex-col sm:flex-row items-center justify-center space-x-0 sm:space-x-4 space-y-4 sm:space-y-0">
          <NuxtLink to="/register" class="wope-button-primary !px-8 !py-4 text-[15px] w-full sm:w-auto">Get Started Free</NuxtLink>
          <NuxtLink to="/login" class="wope-button-secondary !px-8 !py-4 text-[15px] w-full sm:w-auto">Sign In</NuxtLink>
        </div>
      </div>
    </header>

    <!-- Features Section -->
    <section id="features" class="py-32 px-6">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-20">
          <h2 class="text-4xl font-semibold tracking-tight mb-4">Everything you need</h2>
          <p class="text-[#888888] text-lg max-w-xl mx-auto">Build, train, and deploy AI agents in minutes — no coding required.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
          <!-- Main Feature -->
          <div class="md:col-span-8 wope-card p-10 relative overflow-hidden group">
            <div class="absolute top-0 right-0 w-64 h-64 bg-white/[0.03] blur-[80px] group-hover:bg-white/[0.05] transition-all"></div>
            <div class="relative z-10">
               <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
               </div>
               <h3 class="text-3xl font-semibold mb-4">Smart Knowledge Base</h3>
               <p class="text-[#888888] text-lg max-w-md leading-relaxed">
                 Upload your FAQs, product docs, or business rules — your AI agents learn instantly and answer customers accurately.
               </p>
            </div>
          </div>

          <!-- Feature 2 -->
          <div class="md:col-span-4 wope-card p-10 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4">24/7 Availability</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Your agents never sleep. They handle inquiries and qualify leads around the clock.
              </p>
            </div>
          </div>

          <!-- Feature 3 -->
          <div class="md:col-span-4 wope-card p-10 flex flex-col justify-between">
            <div>
              <div class="w-12 h-12 bg-white/5 border border-white/10 rounded-xl flex items-center justify-center mb-8">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4">Live Conversations</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Monitor all conversations in real-time. Jump in when needed.
              </p>
            </div>
          </div>

          <!-- Feature 4 -->
          <div class="md:col-span-8 wope-card p-10 relative overflow-hidden group">
            <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
              <div class="max-w-sm">
                <h3 class="text-3xl font-semibold mb-4">Multi-Channel</h3>
                <p class="text-[#888888] text-[16px] leading-relaxed">
                  Connect your agents to Telegram, WhatsApp, and more. Reach customers wherever they are.
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

    <!-- How It Works -->
    <section id="how-it-works" class="py-32 px-6">
      <div class="max-w-4xl mx-auto text-center">
        <h2 class="text-4xl font-semibold tracking-tight mb-4">Get started in 3 steps</h2>
        <p class="text-[#888888] text-lg mb-20">Up and running in under a minute.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="w-16 h-16 bg-[#A855F7]/10 border border-[#A855F7]/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <span class="text-2xl font-bold text-[#A855F7]">1</span>
            </div>
            <h3 class="text-lg font-semibold mb-3">Create an Agent</h3>
            <p class="text-[#888888] text-[14px] leading-relaxed">Give your AI agent a name and personality. It takes 10 seconds.</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-[#3B82F6]/10 border border-[#3B82F6]/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <span class="text-2xl font-bold text-[#3B82F6]">2</span>
            </div>
            <h3 class="text-lg font-semibold mb-3">Add Knowledge</h3>
            <p class="text-[#888888] text-[14px] leading-relaxed">Upload your FAQs, docs, or paste text. Your agent learns instantly.</p>
          </div>
          <div class="text-center">
            <div class="w-16 h-16 bg-[#10B981]/10 border border-[#10B981]/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <span class="text-2xl font-bold text-[#10B981]">3</span>
            </div>
            <h3 class="text-lg font-semibold mb-3">Go Live</h3>
            <p class="text-[#888888] text-[14px] leading-relaxed">Connect to Telegram or test directly. Your agent is ready to chat.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-40 px-6 text-center">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-5xl font-semibold mb-8 gradient-text tracking-tighter">Ready to get started?</h2>
        <p class="text-xl text-[#888888] mb-12">Create your first AI agent for free. No credit card required.</p>
        <NuxtLink to="/register" class="wope-button-primary !px-12 !py-5 text-lg">Get Started Free</NuxtLink>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-20 px-6 border-t border-white/5">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center space-y-8 md:space-y-0 text-[#888888] text-[13px]">
        <div class="flex items-center space-x-3">
          <div class="w-6 h-6 rounded overflow-hidden">
            <img src="/logo.png" alt="IngiteAI" class="w-full h-full object-cover" />
          </div>
          <span class="font-semibold text-white">IngiteAI</span>
        </div>
        <div class="flex items-center space-x-12">
          <NuxtLink to="/pricing" class="hover:text-white transition-colors">Pricing</NuxtLink>
          <a href="mailto:support@ingiteai.com" class="hover:text-white transition-colors">Contact</a>
        </div>
        <div>
          © 2025 IngiteAI. All rights reserved.
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
