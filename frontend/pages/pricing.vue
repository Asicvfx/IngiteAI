<template>
  <div class="px-6 md:px-12 py-16 min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden">

    <div class="max-w-5xl mx-auto relative z-10 w-full">
      <!-- Header -->
      <div class="text-center mb-16">
        <span class="inline-block bg-[#A855F7]/10 text-[#A855F7] text-[11px] font-bold uppercase tracking-[0.2em] px-4 py-1.5 rounded-full border border-[#A855F7]/20 mb-6">Pricing</span>
        <h1 class="text-4xl md:text-5xl font-semibold tracking-[-0.04em] text-white mb-5">Simple, affordable plans</h1>
        <p class="text-[#A1A1AA] text-[16px] leading-relaxed font-medium max-w-xl mx-auto">
          Start free with generous limits. Upgrade when you're ready.
        </p>
      </div>

      <!-- Pricing Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">

        <!-- Free -->
        <div class="bg-[#050505]/80 border border-[#222] rounded-3xl p-8 flex flex-col hover:border-[#333] transition-colors relative group">
          <div class="mb-6">
            <h3 class="text-lg font-semibold text-white mb-1">Free</h3>
            <p class="text-[#666] text-sm">Perfect to get started</p>
          </div>
          <div class="mb-8">
            <span class="text-4xl font-bold text-white">$0</span>
            <span class="text-[#666] text-sm">/month</span>
          </div>
          <ul class="space-y-3 mb-10 flex-1">
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              5 AI Agents
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              1,000 messages/month
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              3 Knowledge Bases
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Analytics dashboard
            </li>
          </ul>
          <button class="w-full py-3.5 rounded-xl border border-[#333] text-white text-sm font-semibold hover:bg-white/5 transition-all">
            Current Plan
          </button>
        </div>

        <!-- Starter (Featured) -->
        <div class="bg-[#050505]/80 border-2 border-[#A855F7]/40 rounded-3xl p-8 flex flex-col relative group scale-[1.02]">
          <div class="absolute -top-3 left-1/2 -translate-x-1/2">
            <span class="bg-[#A855F7] text-white text-[10px] font-bold uppercase tracking-wider px-4 py-1 rounded-full">Best Value</span>
          </div>
          <div class="mb-6">
            <h3 class="text-lg font-semibold text-white mb-1">Starter</h3>
            <p class="text-[#666] text-sm">For growing businesses</p>
          </div>
          <div class="mb-8">
            <span class="text-4xl font-bold text-white">$5</span>
            <span class="text-[#666] text-sm">/month</span>
          </div>
          <ul class="space-y-3 mb-10 flex-1">
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-[#A855F7] shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              15 AI Agents
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-[#A855F7] shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              5,000 messages/month
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-[#A855F7] shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              10 Knowledge Bases
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-[#A855F7] shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Priority queue
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-[#A855F7] shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Advanced analytics
            </li>
          </ul>
          <button class="w-full py-3.5 rounded-xl bg-[#A855F7] text-white text-sm font-semibold hover:bg-[#9333EA] transition-all shadow-lg shadow-[#A855F7]/20">
            Coming Soon
          </button>
        </div>

        <!-- Pro -->
        <div class="bg-[#050505]/80 border border-[#222] rounded-3xl p-8 flex flex-col hover:border-[#333] transition-colors relative group">
          <div class="mb-6">
            <h3 class="text-lg font-semibold text-white mb-1">Pro</h3>
            <p class="text-[#666] text-sm">For power users</p>
          </div>
          <div class="mb-8">
            <span class="text-4xl font-bold text-white">$12</span>
            <span class="text-[#666] text-sm">/month</span>
          </div>
          <ul class="space-y-3 mb-10 flex-1">
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Unlimited AI Agents
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Unlimited messages
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Unlimited Knowledge Bases
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Priority support
            </li>
            <li class="flex items-center text-sm text-[#A1A1AA]">
              <svg class="w-4 h-4 mr-3 text-green-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              Custom branding
            </li>
          </ul>
          <button class="w-full py-3.5 rounded-xl border border-[#333] text-white text-sm font-semibold hover:bg-white/5 transition-all">
            Coming Soon
          </button>
        </div>
      </div>

      <!-- FAQ -->
      <div class="text-center">
        <p class="text-[#666] text-sm">
          Questions? Contact us at <span class="text-[#A855F7]">support@ingiteai.com</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
