<template>
  <div class="relative min-h-[calc(100vh-56px)] bg-black text-white font-sans overflow-hidden">
    <!-- Deep Ambient Glows (Evervault style) -->
    <div class="fixed top-[-20%] left-[-10%] w-[50%] h-[50%] bg-[#6D28D9]/20 blur-[150px] rounded-full pointer-events-none z-0"></div>
    <div class="fixed bottom-[-20%] right-[-10%] w-[40%] h-[40%] bg-[#4C1D95]/15 blur-[120px] rounded-full pointer-events-none z-0"></div>
    
    <!-- Grid Overlay -->
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik02MCAwaC0xdjYwaDFWMHptMCA1OWgtdjFoMVY1OXoiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wMykiLz4KPC9zdmc+')] [mask-image:linear-gradient(to_bottom,white,transparent_80%)] z-0 pointer-events-none opacity-50"></div>

    <div class="relative z-10 max-w-7xl mx-auto px-6 md:px-12 py-20 pb-32">
      <!-- Hero Section -->
      <div class="mb-24 flex flex-col md:flex-row md:items-center justify-between gap-12">
        <div class="max-w-3xl">
          <h1 class="text-5xl md:text-6xl font-semibold tracking-[-0.04em] text-transparent bg-clip-text bg-gradient-to-br from-white via-white to-white/40 mb-6 drop-shadow-sm">
            Flexible Intelligence Security
          </h1>
          <p class="text-[17px] text-[#A1A1AA] leading-relaxed max-w-2xl font-medium">
            <strong class="text-white font-semibold">IngiteAI</strong> — Take control of your neural agents. Seamlessly inject knowledge, monitor live sentiment streams, and analyze fleet performance globally without sacrificing compliance or latency.
          </p>
          <div class="mt-8 flex items-center space-x-4">
             <button class="bg-white text-black px-6 py-3 rounded-full text-[14px] font-semibold hover:bg-gray-200 transition-all active:scale-95 shadow-[0_0_20px_rgba(255,255,255,0.3)]">
               Deploy Agent
             </button>
             <button class="bg-white/5 border border-white/10 text-white px-6 py-3 rounded-full text-[14px] font-medium hover:bg-white/10 transition-all active:scale-95 backdrop-blur-md">
               View Documentation
             </button>
          </div>
        </div>
        
        <!-- Animated Status Badge -->
        <div class="hidden md:flex flex-col items-end justify-center">
            <div class="bg-white/[0.03] border border-white/10 backdrop-blur-xl px-6 py-4 rounded-2xl shadow-2xl relative overflow-hidden group">
               <div class="absolute inset-0 bg-gradient-to-r from-purple-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
               <div class="flex items-center space-x-3 relative z-10">
                 <div class="relative flex h-3 w-3">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-purple-400 opacity-40"></span>
                    <span class="relative inline-flex rounded-full h-3 w-3 bg-purple-500 shadow-[0_0_10px_rgba(168,85,247,0.8)]"></span>
                 </div>
                 <span class="text-[11px] font-bold text-white uppercase tracking-[0.2em]">Fleet Operational</span>
               </div>
               <p class="text-[12px] text-[#71717A] mt-2 font-medium">Latency: 24ms</p>
            </div>
        </div>
      </div>

      <!-- Live Dashboard Section -->
      <div class="mb-8 flex items-center space-x-3">
         <span class="w-1.5 h-1.5 bg-white/40 rounded-full"></span>
         <h2 class="text-[12px] font-semibold text-[#A1A1AA] uppercase tracking-[0.2em]">Live Telemetry</h2>
      </div>

      <!-- Bento Grid Layout -->
      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 auto-rows-[280px]">
        
        <!-- Primary Metric: Chart -->
        <div class="md:col-span-8 bg-[#09090B]/80 backdrop-blur-2xl border border-white/10 rounded-3xl p-10 flex flex-col justify-between relative overflow-hidden group hover:border-purple-500/30 transition-colors duration-500 shadow-2xl">
           <div class="absolute inset-0 bg-gradient-to-br from-purple-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-1000"></div>
           
           <div class="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between mb-8">
             <div>
               <h3 class="text-xl font-medium tracking-tight text-white shadow-sm">Lead Classification Matrix</h3>
               <p class="text-[13px] text-[#71717A] mt-1 font-medium">Real-time analytical distribution across active fleet</p>
             </div>
             
             <div class="flex items-center space-x-4 mt-4 md:mt-0 bg-black/40 border border-white/5 rounded-full px-4 py-2">
               <div v-for="l in ['Cold', 'Warm', 'Hot']" :key="l" class="flex items-center space-x-2">
                 <span class="w-2.5 h-2.5 rounded-full" 
                   :class="l === 'Hot' ? 'bg-[#A855F7] shadow-[0_0_10px_rgba(168,85,247,0.6)]' : l === 'Warm' ? 'bg-white/60' : 'bg-[#27272A] border border-white/10'"></span>
                 <span class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-wider">{{ l }}</span>
               </div>
             </div>
           </div>
           
           <div class="flex-1 relative flex items-center justify-center z-10 w-full h-full">
             <div class="h-56 w-full max-w-sm">
               <Doughnut v-if="chartData" :data="chartData" :options="chartOptions" />
               <div v-else class="h-full flex flex-col items-center justify-center border border-dashed border-white/10 rounded-full bg-white/[0.02]">
                 <svg class="w-6 h-6 text-white/20 animate-spin mb-3" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                 <span class="text-[10px] font-bold text-[#71717A] uppercase tracking-[0.2em]">Aggregating</span>
               </div>
             </div>
           </div>
        </div>

        <!-- Sentiment Bento -->
        <div class="md:col-span-4 bg-[#09090B]/80 backdrop-blur-2xl border border-white/10 rounded-3xl p-10 flex flex-col justify-between group hover:border-white/20 transition-colors shadow-2xl">
           <h3 class="text-[12px] font-semibold text-[#A1A1AA] uppercase tracking-[0.2em]">Neural Sentiment</h3>
           <div class="space-y-8 mt-6">
              <div v-for="(val, key) in sentiment" :key="key">
                 <div class="flex justify-between items-baseline mb-3">
                    <span class="text-[14px] font-semibold text-white/80 tracking-tight">{{ key }}</span>
                    <span class="text-[16px] font-bold text-white">{{ val }}%</span>
                 </div>
                 <div class="h-[3px] bg-white/5 rounded-full overflow-hidden">
                    <div class="h-full transition-all duration-1000 ease-out"
                     :class="key === 'Positive' ? 'bg-gradient-to-r from-purple-600 to-purple-400 shadow-[0_0_10px_rgba(168,85,247,0.5)]' : key === 'Neutral' ? 'bg-white/40' : 'bg-[#27272A]'"
                     :style="`width: ${val}%`"
                    ></div>
                 </div>
              </div>
           </div>
        </div>

        <!-- Metric Bento 1 -->
        <div class="md:col-span-3 bg-[#09090B]/80 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 flex flex-col justify-between group hover:bg-white/[0.02] transition-colors shadow-xl">
          <div class="w-10 h-10 rounded-full bg-purple-500/10 border border-purple-500/20 flex items-center justify-center mb-4 text-purple-400">
             <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          </div>
          <div>
            <p class="text-[11px] font-bold text-[#71717A] uppercase tracking-[0.2em] mb-1">Total Events</p>
            <div class="flex items-baseline space-x-2">
              <p class="text-5xl font-semibold tracking-tighter text-white">{{ stats[0].value }}</p>
            </div>
          </div>
        </div>

        <!-- Metric Bento 2 -->
        <div class="md:col-span-3 bg-[#09090B]/80 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 flex flex-col justify-between group hover:bg-white/[0.02] transition-colors shadow-xl">
          <div class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center mb-4 text-white">
             <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 012-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          </div>
          <div>
            <p class="text-[11px] font-bold text-[#71717A] uppercase tracking-[0.2em] mb-1">Fleet Strength</p>
            <div class="flex items-baseline space-x-2">
              <p class="text-5xl font-semibold tracking-tighter text-white">{{ stats[1].value }}</p>
            </div>
          </div>
        </div>

        <!-- Quick Action Bento -->
        <div class="md:col-span-6 bg-transparent flex flex-col md:flex-row gap-4">
           <NuxtLink v-for="action in quickActions" :key="action.title" :to="action.to" 
             class="flex-1 w-full bg-[#09090B]/80 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 hover:border-white/30 hover:bg-white/[0.05] transition-all duration-300 group overflow-hidden relative shadow-xl focus:outline-none focus:ring-2 focus:ring-purple-500/50">
             <div class="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
             
             <div class="relative z-10 flex flex-col justify-between h-full">
               <div class="flex items-center justify-between mb-4">
                 <div class="w-12 h-12 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center text-white group-hover:scale-110 group-hover:bg-white group-hover:text-black transition-all duration-500 shadow-lg" v-html="action.icon"></div>
                 <svg class="w-5 h-5 text-white/20 group-hover:text-white group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
               </div>
               <div>
                 <h3 class="text-[16px] font-semibold text-white mb-2 tracking-tight">{{ action.title }}</h3>
                 <p class="text-[13px] text-[#A1A1AA] leading-relaxed font-medium">{{ action.description }}</p>
               </div>
             </div>
           </NuxtLink>
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
  { name: 'Active Agents', value: '0' },
  { name: 'Growth', value: '0%' },
  { name: 'Priority Leads', value: '0' },
]);

const sentiment = ref({
  'Positive': 0,
  'Neutral': 0,
  'Escalated': 0
});

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
      backgroundColor: 'rgba(9, 9, 11, 0.9)',
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

const quickActions = [
  {
    title: 'Active Streams',
    description: 'Monitor real-time agent communications and intervene manually.',
    to: '/chats',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>'
  },
  {
    title: 'Knowledge Base',
    description: 'Inject proprietary business intelligence and PDF assets.',
    to: '/faq',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>'
  }
];

onMounted(async () => {
  const config = useRuntimeConfig();
  try {
    const data = await $fetch<any>(`${config.public.apiBaseUrl}/api/v1/dashboard/analytics/`, { 
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    analyticsData.value = data;
    
    if (data.metrics) {
      stats.value[0].value = data.metrics.total_messages?.toString() || '0';
      stats.value[1].value = data.metrics.total_conversations?.toString() || '0'; 
      stats.value[3].value = data.metrics.hot_leads?.toString() || '0';
      
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
