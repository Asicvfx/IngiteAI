<template>
  <div class="min-h-screen bg-[#0A0A0B] text-[#EDEDED] font-sans selection:bg-white/20 overflow-x-hidden">
    
    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 wope-glass border-b border-white/5">
      <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-8 h-8 rounded-lg overflow-hidden shadow-lg shadow-white/5">
            <img src="/logo.png" alt="IngiteAI" class="w-full h-full object-cover" />
          </div>
          <span class="text-lg font-semibold tracking-tighter">IngiteAI</span>
        </div>
        <div class="hidden md:flex items-center space-x-8 text-[13px] font-medium text-[#888888]">
          <a href="#features" class="hover:text-white transition-colors duration-300">Features</a>
          <a href="#how-it-works" class="hover:text-white transition-colors duration-300">How It Works</a>
          <NuxtLink to="/pricing" class="hover:text-white transition-colors duration-300">Pricing</NuxtLink>
        </div>
        <div class="flex items-center space-x-4">
          <NuxtLink to="/login" class="text-[13px] font-medium text-[#888] hover:text-white transition-colors duration-300">Sign In</NuxtLink>
          <NuxtLink to="/register" class="wope-button-primary !py-2.5 !px-5 text-[13px] shadow-lg shadow-white/5">Get Started</NuxtLink>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="pt-44 pb-32 px-6 relative">
      <!-- Ambient glow -->
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[900px] h-[500px] bg-[#A855F7]/[0.04] blur-[150px] rounded-full pointer-events-none animate-pulse-slow"></div>
      <div class="absolute top-40 right-1/4 w-[300px] h-[300px] bg-[#3B82F6]/[0.03] blur-[100px] rounded-full pointer-events-none"></div>
      
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <!-- Badge -->
        <div class="inline-flex items-center space-x-2.5 px-4 py-1.5 rounded-full border border-white/10 bg-white/[0.03] mb-10 animate-fade-in backdrop-blur-sm">
          <span class="w-2 h-2 rounded-full bg-[#A855F7] animate-pulse shadow-[0_0_8px_rgba(168,85,247,0.6)]"></span>
          <span class="text-[11px] font-semibold uppercase tracking-[0.15em] text-[#A1A1AA]">AI-Powered Customer Support</span>
        </div>
        
        <!-- Heading -->
        <h1 class="text-5xl md:text-7xl font-semibold tracking-[-0.04em] leading-[0.92] mb-8 animate-fade-in-up">
          <span class="gradient-text">Automate your business</span><br />
          <span class="text-white/90">with AI agents</span>
        </h1>
        
        <!-- Subtitle -->
        <p class="text-lg md:text-xl text-[#888888] leading-relaxed mb-14 max-w-2xl mx-auto tracking-normal animate-fade-in-up animation-delay-100">
          Create AI assistants that answer customer questions 24/7, learn from your business data, and handle unlimited conversations — in minutes.
        </p>
        
        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4 animate-fade-in-up animation-delay-200">
          <NuxtLink to="/register" class="bg-white text-black px-8 py-4 rounded-xl text-[15px] font-semibold hover:bg-gray-100 transition-all active:scale-95 shadow-xl shadow-white/10 flex items-center group">
            Get Started Free
            <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
          </NuxtLink>
          <NuxtLink to="/login" class="wope-button-secondary !px-8 !py-4 text-[15px]">Sign In</NuxtLink>
        </div>
      </div>
    </header>

    <!-- Features Section -->
    <section id="features" class="py-32 px-6 relative">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-[#A855F7]/[0.01] to-transparent pointer-events-none"></div>
      
      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-20">
          <p class="text-[#A855F7] text-[12px] font-bold uppercase tracking-[0.2em] mb-4">Everything you need</p>
          <h2 class="text-4xl md:text-5xl font-semibold tracking-tight mb-5 gradient-text">Powerful features, simple setup</h2>
          <p class="text-[#888888] text-lg max-w-xl mx-auto">Build, train, and deploy AI agents in minutes — no coding required.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
          <!-- Main Feature -->
          <div class="md:col-span-8 bg-[#050505]/80 border border-[#222] rounded-3xl p-10 md:p-12 relative overflow-hidden group hover:border-[#333] transition-all duration-500">
            <div class="absolute top-0 right-0 w-80 h-80 bg-[#A855F7]/[0.03] blur-[100px] group-hover:bg-[#A855F7]/[0.06] transition-all duration-700 pointer-events-none"></div>
            <div class="relative z-10">
               <div class="w-14 h-14 bg-[#A855F7]/10 border border-[#A855F7]/20 rounded-2xl flex items-center justify-center mb-8 group-hover:scale-110 group-hover:bg-[#A855F7]/15 transition-all duration-500">
                  <svg class="w-7 h-7 text-[#A855F7]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
               </div>
               <h3 class="text-2xl md:text-3xl font-semibold mb-4 tracking-tight">Smart Knowledge Base</h3>
               <p class="text-[#888888] text-[16px] max-w-md leading-relaxed">
                 Upload your FAQs, product docs, or business rules — your AI agents learn instantly and answer customers accurately.
               </p>
            </div>
            <!-- Mock UI -->
            <div class="mt-10 p-5 bg-black/50 border border-white/5 rounded-2xl backdrop-blur-sm group-hover:border-white/10 transition-all">
              <div class="flex items-center space-x-3 mb-4">
                <div class="w-2.5 h-2.5 rounded-full bg-[#A855F7]/40"></div>
                <div class="w-24 h-2 bg-white/10 rounded-full"></div>
                <div class="w-16 h-2 bg-white/5 rounded-full"></div>
              </div>
              <div class="space-y-2.5">
                <div class="w-full h-1.5 bg-white/[0.04] rounded-full"></div>
                <div class="w-4/5 h-1.5 bg-white/[0.04] rounded-full"></div>
                <div class="w-3/5 h-1.5 bg-white/[0.04] rounded-full"></div>
              </div>
            </div>
          </div>

          <!-- Feature 2 -->
          <div class="md:col-span-4 bg-[#050505]/80 border border-[#222] rounded-3xl p-10 flex flex-col justify-between group hover:border-[#333] transition-all duration-500 relative overflow-hidden">
            <div class="absolute bottom-0 left-0 w-40 h-40 bg-[#3B82F6]/[0.03] blur-[60px] group-hover:bg-[#3B82F6]/[0.06] transition-all duration-700 pointer-events-none"></div>
            <div class="relative z-10">
              <div class="w-14 h-14 bg-[#3B82F6]/10 border border-[#3B82F6]/20 rounded-2xl flex items-center justify-center mb-8 group-hover:scale-110 group-hover:bg-[#3B82F6]/15 transition-all duration-500">
                <svg class="w-7 h-7 text-[#3B82F6]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4 tracking-tight">24/7 Availability</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Your agents never sleep. They handle inquiries and qualify leads around the clock.
              </p>
            </div>
          </div>

          <!-- Feature 3 -->
          <div class="md:col-span-4 bg-[#050505]/80 border border-[#222] rounded-3xl p-10 flex flex-col justify-between group hover:border-[#333] transition-all duration-500 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-40 h-40 bg-[#10B981]/[0.03] blur-[60px] group-hover:bg-[#10B981]/[0.06] transition-all duration-700 pointer-events-none"></div>
            <div class="relative z-10">
              <div class="w-14 h-14 bg-[#10B981]/10 border border-[#10B981]/20 rounded-2xl flex items-center justify-center mb-8 group-hover:scale-110 group-hover:bg-[#10B981]/15 transition-all duration-500">
                <svg class="w-7 h-7 text-[#10B981]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
              </div>
              <h3 class="text-2xl font-semibold mb-4 tracking-tight">Live Conversations</h3>
              <p class="text-[#888888] text-[15px] leading-relaxed">
                Monitor all conversations in real-time. Jump in when needed to assist your customers.
              </p>
            </div>
          </div>

          <!-- Feature 4 -->
          <div class="md:col-span-8 bg-[#050505]/80 border border-[#222] rounded-3xl p-10 md:p-12 relative overflow-hidden group hover:border-[#333] transition-all duration-500">
            <div class="absolute bottom-0 right-0 w-60 h-60 bg-[#F59E0B]/[0.02] blur-[80px] group-hover:bg-[#F59E0B]/[0.04] transition-all duration-700 pointer-events-none"></div>
            <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
              <div class="max-w-sm">
                <div class="w-14 h-14 bg-white/5 border border-white/10 rounded-2xl flex items-center justify-center mb-8 group-hover:scale-110 group-hover:bg-white/10 transition-all duration-500">
                  <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h3 class="text-2xl md:text-3xl font-semibold mb-4 tracking-tight">Multi-Channel Support</h3>
                <p class="text-[#888888] text-[16px] leading-relaxed">
                  Connect your agents to Telegram, WhatsApp, and more. Reach customers on every platform.
                </p>
              </div>
              <div class="flex -space-x-5">
                <div class="w-16 h-16 rounded-2xl border-2 border-[#222] bg-[#111] flex items-center justify-center text-xl font-bold group-hover:border-[#333] transition-all shadow-xl">T</div>
                <div class="w-16 h-16 rounded-2xl border-2 border-[#222] bg-[#111] flex items-center justify-center text-xl font-bold group-hover:border-[#333] transition-all shadow-xl">W</div>
                <div class="w-16 h-16 rounded-2xl border-2 border-[#222] bg-[#111] flex items-center justify-center text-xl font-bold group-hover:border-[#333] transition-all shadow-xl">M</div>
                <div class="w-16 h-16 rounded-2xl border-2 border-[#222] bg-[#111] flex items-center justify-center text-sm font-bold text-[#888] group-hover:border-[#333] transition-all shadow-xl">+5</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section id="how-it-works" class="py-32 px-6 relative">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-[#3B82F6]/[0.01] to-transparent pointer-events-none"></div>
      
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <p class="text-[#3B82F6] text-[12px] font-bold uppercase tracking-[0.2em] mb-4">Simple setup</p>
        <h2 class="text-4xl md:text-5xl font-semibold tracking-tight mb-5 gradient-text">Get started in 3 steps</h2>
        <p class="text-[#888888] text-lg mb-20">Up and running in under a minute.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Step 1 -->
          <div class="bg-[#050505]/80 border border-[#222] rounded-3xl p-8 group hover:border-[#A855F7]/30 transition-all duration-500 relative overflow-hidden">
            <div class="absolute inset-0 bg-[#A855F7]/[0.02] opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            <div class="relative z-10">
              <div class="w-16 h-16 bg-[#A855F7]/10 border border-[#A855F7]/20 rounded-2xl flex items-center justify-center mx-auto mb-8 group-hover:scale-110 group-hover:shadow-[0_0_30px_rgba(168,85,247,0.15)] transition-all duration-500">
                <span class="text-2xl font-bold text-[#A855F7]">1</span>
              </div>
              <h3 class="text-lg font-semibold mb-3 tracking-tight">Create an Agent</h3>
              <p class="text-[#888888] text-[14px] leading-relaxed">Give your AI agent a name and connect your Telegram bot. It takes 10 seconds.</p>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="bg-[#050505]/80 border border-[#222] rounded-3xl p-8 group hover:border-[#3B82F6]/30 transition-all duration-500 relative overflow-hidden">
            <div class="absolute inset-0 bg-[#3B82F6]/[0.02] opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            <div class="relative z-10">
              <div class="w-16 h-16 bg-[#3B82F6]/10 border border-[#3B82F6]/20 rounded-2xl flex items-center justify-center mx-auto mb-8 group-hover:scale-110 group-hover:shadow-[0_0_30px_rgba(59,130,246,0.15)] transition-all duration-500">
                <span class="text-2xl font-bold text-[#3B82F6]">2</span>
              </div>
              <h3 class="text-lg font-semibold mb-3 tracking-tight">Add Knowledge</h3>
              <p class="text-[#888888] text-[14px] leading-relaxed">Upload your FAQs, docs, or paste text. Your agent learns your business instantly.</p>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="bg-[#050505]/80 border border-[#222] rounded-3xl p-8 group hover:border-[#10B981]/30 transition-all duration-500 relative overflow-hidden">
            <div class="absolute inset-0 bg-[#10B981]/[0.02] opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            <div class="relative z-10">
              <div class="w-16 h-16 bg-[#10B981]/10 border border-[#10B981]/20 rounded-2xl flex items-center justify-center mx-auto mb-8 group-hover:scale-110 group-hover:shadow-[0_0_30px_rgba(16,185,129,0.15)] transition-all duration-500">
                <span class="text-2xl font-bold text-[#10B981]">3</span>
              </div>
              <h3 class="text-lg font-semibold mb-3 tracking-tight">Go Live</h3>
              <p class="text-[#888888] text-[14px] leading-relaxed">Connect to Telegram or test directly. Your agent is ready to handle conversations.</p>
            </div>
          </div>
        </div>

        <!-- Connector line -->
        <div class="hidden md:flex items-center justify-center mt-12">
          <div class="flex items-center space-x-4 text-[#333]">
            <div class="w-3 h-3 rounded-full border-2 border-[#A855F7]/30"></div>
            <div class="w-24 h-px bg-gradient-to-r from-[#A855F7]/20 to-[#3B82F6]/20"></div>
            <div class="w-3 h-3 rounded-full border-2 border-[#3B82F6]/30"></div>
            <div class="w-24 h-px bg-gradient-to-r from-[#3B82F6]/20 to-[#10B981]/20"></div>
            <div class="w-3 h-3 rounded-full border-2 border-[#10B981]/30"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-40 px-6 text-center relative">
      <div class="absolute inset-0 bg-gradient-to-t from-[#A855F7]/[0.02] to-transparent pointer-events-none"></div>
      <div class="max-w-2xl mx-auto relative z-10">
        <h2 class="text-4xl md:text-5xl font-semibold mb-6 gradient-text tracking-tighter">Ready to get started?</h2>
        <p class="text-lg text-[#888888] mb-12 leading-relaxed">Create your first AI agent for free. No credit card required.</p>
        <NuxtLink to="/register" class="bg-white text-black px-12 py-5 rounded-xl text-lg font-semibold hover:bg-gray-100 transition-all active:scale-95 shadow-xl shadow-white/10 inline-flex items-center group">
          Get Started Free
          <svg class="w-5 h-5 ml-2 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
        </NuxtLink>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-16 px-6 border-t border-white/5">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center space-y-6 md:space-y-0 text-[#666] text-[13px]">
        <div class="flex items-center space-x-3">
          <div class="w-6 h-6 rounded overflow-hidden">
            <img src="/logo.png" alt="IngiteAI" class="w-full h-full object-cover" />
          </div>
          <span class="font-semibold text-white">IngiteAI</span>
        </div>
        <div class="flex items-center space-x-10">
          <NuxtLink to="/pricing" class="hover:text-white transition-colors duration-300">Pricing</NuxtLink>
          <a href="mailto:support@ingiteai.com" class="hover:text-white transition-colors duration-300">Contact</a>
        </div>
        <div>© 2025 IngiteAI. All rights reserved.</div>
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
  animation: fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.animate-fade-in-up {
  animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.animation-delay-100 {
  animation-delay: 0.15s;
}

.animation-delay-200 {
  animation-delay: 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse-slow {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

.animate-pulse-slow {
  animation: pulse-slow 4s ease-in-out infinite;
}
</style>
