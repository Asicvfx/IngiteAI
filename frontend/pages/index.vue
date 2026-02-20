<template>
  <div class="min-h-[calc(100vh-56px)] bg-[#0A0A0B] text-white font-sans overflow-x-hidden relative">
    <!-- Huge background glow similar to Evervault -->
    <div class="absolute bottom-0 left-0 right-0 h-[600px] bg-gradient-to-t from-[#6A25FF]/60 via-[#6A25FF]/10 to-transparent pointer-events-none opacity-60"></div>
    
    <div class="relative z-10 max-w-6xl mx-auto px-6 py-24 md:py-32 flex flex-col items-center">
      <!-- Centered Hero Text -->
      <h1 class="text-5xl md:text-[72px] leading-tight font-semibold tracking-[-0.04em] text-center mb-6 text-white drop-shadow-lg">
        Flexible Intelligence Security
      </h1>
      <h2 class="text-2xl md:text-3xl text-[#E4E4E5] font-medium tracking-tight text-center mb-6">
        Maximum protection, minimum compliance burden
      </h2>
      <p class="text-[17px] text-[#A1A1AA] leading-relaxed max-w-3xl text-center mb-12 font-medium">
        Take control of your neural agents — seamlessly inject knowledge, monitor live sentiment streams, comply with data regulations, avoid vendor lock-in, and spin up scalable AI fleets globally.
      </p>

      <div class="flex items-center justify-center space-x-6 mb-32">
        <NuxtLink to="/overview" class="bg-white text-black px-8 py-3.5 rounded-full text-[15px] font-semibold hover:bg-gray-200 transition-all active:scale-95 shadow-xl flex items-center">
          Open Live Overview <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
        </NuxtLink>
        <NuxtLink to="/bots" class="text-white text-[15px] font-semibold hover:text-gray-300 transition-colors">
          Configure Agents
        </NuxtLink>
      </div>

      <!-- Feature Squares Row -->
      <div class="flex flex-wrap justify-center gap-x-12 gap-y-8 mb-32 max-w-5xl mx-auto">
        <div v-for="feature in features" :key="feature.name" class="flex flex-col items-center group cursor-pointer w-[100px]">
           <div class="w-16 h-16 rounded-[18px] bg-[#111111] border border-[#2A2A2A] flex items-center justify-center mb-4 group-hover:bg-[#1A1A1A] group-hover:border-[#404040] transition-all shadow-lg text-[#888888] group-hover:text-white">
              <span v-html="feature.icon" class="transition-colors"></span>
           </div>
           <p class="text-[12px] font-medium text-center text-[#A1A1AA] group-hover:text-white transition-colors leading-[1.4]">{{ feature.name }}</p>
        </div>
      </div>

      <!-- Large Descriptive Data Cards (Static Introductions) -->
      <div class="w-full grid grid-cols-1 md:grid-cols-2 gap-8">
         <!-- Card 1: Description -->
         <div class="bg-[#050505]/95 border border-[#1A1A1A] rounded-3xl p-10 md:p-14 flex flex-col justify-start group hover:border-[#333333] transition-all relative overflow-hidden h-[400px]">
            <div class="relative z-10 mb-8">
               <p class="text-[#A855F7] text-[13px] font-semibold tracking-wide mb-3">Accelerate your agent product</p>
               <h3 class="text-[28px] md:text-3xl font-semibold tracking-tight text-white mb-6 leading-snug">Expedite the security requirements of launching an AI fleet</h3>
               <p class="text-[#A1A1AA] text-[15px] leading-relaxed max-w-[400px]">
                  Improve your agent response times from seconds to milliseconds, by using IngiteAI to track lead classifications, monitor API latencies, and reveal real-time communication events to administrators safely.
               </p>
               <NuxtLink to="/faq" class="mt-8 inline-flex items-center text-[14px] font-medium text-[#A855F7] hover:text-purple-400 group/link transition-colors">
                 Manage Intelligence <svg class="w-4 h-4 ml-1 transform group-hover/link:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
               </NuxtLink>
            </div>
         </div>

         <!-- Card 2: Description -->
         <div class="bg-[#050505]/95 border border-[#1A1A1A] rounded-3xl p-10 md:p-14 flex flex-col justify-start group hover:border-[#333333] transition-all relative overflow-hidden h-[400px]">
            <div class="relative z-10 mb-8">
               <p class="text-[#3B82F6] text-[13px] font-semibold tracking-wide mb-3">Optimize neural performance</p>
               <h3 class="text-[28px] md:text-3xl font-semibold tracking-tight text-white mb-6 leading-snug">Improve diagnostic visibility with a multi-node AI setup</h3>
               <p class="text-[#A1A1AA] text-[15px] leading-relaxed max-w-[400px]">
                  Avoid catastrophic customer interactions and optimize retention rates by selectively tracking escalated positive, neutral, and negative conversations. Identify and intervene instantly via live streams.
               </p>
               <NuxtLink to="/chats" class="mt-8 inline-flex items-center text-[14px] font-medium text-[#3B82F6] hover:text-blue-400 group/link transition-colors">
                 View Live Streams <svg class="w-4 h-4 ml-1 transform group-hover/link:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
               </NuxtLink>
            </div>
            
         </div>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
const features = [
  { name: 'Agent\nCompliance', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>' },
  { name: 'Fleet\nOptimization', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>' },
  { name: 'Lead\nClassification', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>' },
  { name: 'Neural\nTokens', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 012-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>' },
  { name: 'Live\nInsights', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"></path></svg>' },
  { name: 'Key\nManagement', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>' }
];
</script>
