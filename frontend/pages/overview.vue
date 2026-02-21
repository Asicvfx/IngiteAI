<template>
  <div class="min-h-[calc(100vh-56px)] bg-[#0A0A0B] text-white font-sans overflow-x-hidden relative">
    <!-- Huge background glow similar to Evervault -->
    <div class="absolute bottom-0 left-0 right-0 h-[800px] bg-gradient-to-t from-[#6A25FF]/60 via-[#6A25FF]/10 to-transparent pointer-events-none opacity-60"></div>
    
    <div class="relative z-10 max-w-6xl mx-auto px-6 py-16 md:py-20 flex flex-col items-center">
      
      <div class="w-full mb-12 flex justify-between items-end">
        <div>
           <h1 class="text-3xl font-semibold tracking-[-0.04em] text-white">Live Telemetry</h1>
           <p class="mt-2 text-[#A1A1AA] text-[15px] font-medium">Real-time overview of your agent fleet performance</p>
        </div>
      </div>

      <!-- Large Descriptive Data Cards -->
      <div class="w-full grid grid-cols-1 md:grid-cols-2 gap-8">
         <!-- Card 1: Description + Chart -->
         <div class="bg-[#050505]/95 border border-[#1A1A1A] rounded-3xl p-10 md:p-12 flex flex-col justify-between group hover:border-[#333333] transition-all relative overflow-hidden min-h-[500px]">
            
            <div class="relative z-10 mb-8">
               <p class="text-[#A855F7] text-[12px] font-bold uppercase tracking-widest mb-3">Accelerate your agent product</p>
               <h3 class="text-[26px] md:text-[28px] font-semibold tracking-tight text-white mb-4 leading-snug">Monitor the security and performance of your active fleet</h3>
               <p class="text-[#A1A1AA] text-[14px] leading-relaxed">
                  Improve your agent response times from seconds to milliseconds, by using IngiteAI to track lead classifications, monitor API latencies, and reveal real-time communication events to administrators.
               </p>
               <NuxtLink to="/chats" class="mt-6 inline-flex items-center text-[13px] font-bold uppercase tracking-widest text-[#A855F7] hover:text-purple-400 group/link transition-colors">
                 Live Streams <svg class="w-4 h-4 ml-1 transform group-hover/link:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
               </NuxtLink>
            </div>

            <!-- Visualization inside Card -->
            <div class="relative z-10 flex-1 flex justify-center items-end w-full mt-4">
               <div class="w-[280px] h-[280px] relative shrink-0 p-4 bg-[#0A0A0B] rounded-full border border-white/5 shadow-2xl translate-y-8">
                 <Doughnut v-if="chartData" :data="chartData" :options="chartOptions" />
                 <div v-else class="h-full flex items-center justify-center">
                    <span class="text-[10px] text-zinc-500 uppercase tracking-widest font-bold">Loading</span>
                 </div>
               </div>
            </div>
         </div>

         <!-- Card 2: Sentiment and Strength -->
         <div class="bg-[#050505]/95 border border-[#1A1A1A] rounded-3xl p-10 md:p-12 flex flex-col justify-between group hover:border-[#333333] transition-all relative overflow-hidden min-h-[500px]">

            <div class="relative z-10 mb-8">
               <p class="text-[#3B82F6] text-[12px] font-bold uppercase tracking-widest mb-3">Optimize neural performance</p>
               <h3 class="text-[26px] md:text-[28px] font-semibold tracking-tight text-white mb-4 leading-snug">Improve engagement scores with a multi-node AI setup</h3>
               <p class="text-[#A1A1AA] text-[14px] leading-relaxed">
                  Avoid catastrophic customer interactions and optimize retention rates by selectively tracking escalated positive, neutral, and negative conversations.
               </p>
            </div>

            <!-- Visual Stats -->
            <div class="relative z-10 grid grid-cols-2 gap-4 mt-auto">
               <div class="bg-[#0D0D12] border border-[#222] rounded-2xl p-5 flex flex-col items-center justify-center shadow-inner">
                 <p class="text-[10px] font-bold text-[#A1A1AA] uppercase tracking-wider mb-2">Total Events</p>
                 <p class="text-[32px] font-semibold tracking-tight text-white">{{ stats[0]?.value }}</p>
               </div>
               <div class="bg-[#0D0D12] border border-[#222] rounded-2xl p-5 flex flex-col items-center justify-center shadow-inner">
                 <p class="text-[10px] font-bold text-[#A1A1AA] uppercase tracking-wider mb-2">Fleet Strength</p>
                 <p class="text-[32px] font-semibold tracking-tight text-white">{{ stats[1]?.value }}</p>
               </div>
               
               <div class="col-span-2 bg-[#0D0D12] border border-[#222] rounded-2xl px-6 py-5 mt-2 shadow-inner">
                  <div v-for="(val, key) in sentiment" :key="key" class="mb-3.5 last:mb-0">
                    <div class="flex justify-between items-baseline mb-2">
                        <span class="text-[12px] font-medium text-[#A1A1AA]">{{ key }}</span>
                        <span class="text-[12px] font-bold text-white">{{ val }}%</span>
                    </div>
                    <div class="h-[3px] bg-[#1A1A1A] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-blue-500 to-indigo-400 transition-all duration-1000" :style="`width: ${val}%`"></div>
                    </div>
                  </div>
               </div>
            </div>
            
         </div>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useAuthStore } from '~/stores/auth';
import { Doughnut } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, type ChartOptions } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

const auth = useAuthStore();
const analyticsData = ref<any>(null);

const stats = ref([
  { name: 'Total Messages', value: '0' },
  { name: 'Active Agents', value: '0' }
]);

const sentiment = ref({
  'Positive': 0,
  'Neutral': 0,
  'Escalated': 0
});

const features = [
  { name: 'Agent\nCompliance', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>' },
  { name: 'Fleet\nOptimization', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>' },
  { name: 'Lead\nClassification', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>' },
  { name: 'Neural\nTokens', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 012-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>' },
  { name: 'Live\nInsights', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"></path></svg>' },
  { name: 'Key\nManagement', icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>' }
];

const chartData = computed(() => {
  if (!analyticsData.value?.leads) return null;
  
  const counts = [0, 0, 0];
  analyticsData.value.leads.forEach((item: any) => {
    if (item.lead_type === 'cold') counts[0] = item.count;
    if (item.lead_type === 'warm') counts[1] = item.count;
    if (item.lead_type === 'hot') counts[2] = item.count;
  });

  return {
    labels: ['Cold', 'Warm', 'Hot'],
    datasets: [{
      data: counts,
      backgroundColor: ['#27272A', '#D4D4D8', '#A855F7'],
      borderColor: '#000000',
      borderWidth: 8,
      hoverOffset: 4,
      borderRadius: 4
    }]
  };
});

const chartOptions: ChartOptions<'doughnut'> = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    tooltip: {
      backgroundColor: 'rgba(5, 5, 5, 0.9)',
      padding: 14,
      cornerRadius: 12,
      borderColor: 'rgba(255, 255, 255, 0.1)',
      borderWidth: 1,
      titleFont: { size: 13, weight: 'bold', family: 'Inter' },
      bodyFont: { size: 13, family: 'Inter' },
      displayColors: true,
      boxPadding: 6,
      usePointStyle: true,
    }
  },
  cutout: '80%',
  animation: {
    animateScale: true,
    animateRotate: true,
    duration: 2000,
    easing: 'easeOutQuart'
  }
};

onMounted(async () => {
  const config = useRuntimeConfig();
  try {
    const data = await $fetch<any>(`${config.public.apiBaseUrl}/api/v1/dashboard/analytics/`, { 
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    analyticsData.value = data;
    
    if (data.metrics) {
      if (stats.value[0]) stats.value[0].value = data.metrics.total_messages?.toString() || '0';
      if (stats.value[1]) stats.value[1].value = data.metrics.total_conversations?.toString() || '0'; 
      
      const total = data.metrics.total_conversations || 1;
      if (data.sentiment) {
        sentiment.value.Positive = Math.round((data.sentiment.positive / total) * 100);
        sentiment.value.Neutral = Math.round((data.sentiment.neutral / total) * 100);
        sentiment.value.Escalated = Math.round((data.sentiment.needs_attention / total) * 100);
      }
    }
    
  } catch (err) {
    console.error('Failed to fetch analytics', err);
  }
});
</script>
