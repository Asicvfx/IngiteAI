<template>
  <div class="px-6 md:px-12 py-16 bg-[#080808] min-h-[calc(100vh-56px)] text-white font-sans">
    <div class="max-w-7xl mx-auto">
      <!-- Header Section -->
      <div class="mb-20 flex flex-col md:flex-row md:items-end md:justify-between gap-6">
        <div>
          <h1 class="text-4xl font-semibold tracking-[-0.04em] gradient-text">Intelligence Overview</h1>
          <p class="mt-4 text-[#888888] text-[15px] leading-relaxed max-w-xl">
            Real-time neural metrics and lead classification across your synchronized agent fleet.
          </p>
        </div>
        <div class="flex items-center space-x-2 text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em] bg-white/5 px-4 py-2 rounded-full border border-white/5">
          <span class="w-1.5 h-1.5 bg-white rounded-full animate-pulse"></span>
          <span>Core Synchronized</span>
        </div>
      </div>

      <!-- Bento Grid Layout -->
      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 auto-rows-[240px]">
        <!-- Primary Metric -->
        <div class="md:col-span-8 wope-card p-10 flex flex-col justify-between">
           <div class="flex items-center justify-between mb-8">
             <div>
               <h2 class="text-lg font-medium tracking-tight">Lead Classification</h2>
               <p class="text-[12px] text-[#888888] mt-1">Classification across the agent fleet</p>
             </div>
             <div class="flex items-center space-x-6">
               <div v-for="l in ['Cold', 'Warm', 'Hot']" :key="l" class="flex items-center space-x-2">
                 <span class="w-2 h-2 rounded-full border border-white/20" :class="l === 'Hot' ? 'bg-white' : l === 'Warm' ? 'bg-white/40' : ''"></span>
                 <span class="text-[11px] font-medium text-[#888888] uppercase tracking-wider">{{ l }}</span>
               </div>
             </div>
           </div>
           
           <div class="flex-1 relative flex items-center justify-center">
             <div class="h-48 w-full">
               <Doughnut v-if="chartData" :data="chartData" :options="chartOptions" />
               <div v-else class="h-full flex items-center justify-center border border-dashed border-[#1A1A1A] rounded-2xl">
                 <span class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em]">Aggregating Intelligence...</span>
               </div>
             </div>
           </div>
        </div>

        <!-- Sentiment Bento -->
        <div class="md:col-span-4 wope-card p-10 flex flex-col justify-between">
           <h2 class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em]">Neural Sentiment</h2>
           <div class="space-y-8">
              <div v-for="(val, key) in sentiment" :key="key">
                 <div class="flex justify-between items-baseline mb-2">
                    <span class="text-[13px] font-medium text-[#888888]">{{ key }}</span>
                    <span class="text-[14px] font-semibold text-white">{{ val }}%</span>
                 </div>
                 <div class="h-[2px] bg-[#1A1A1A] rounded-full overflow-hidden">
                    <div class="h-full bg-white transition-all duration-1000"
                     :class="key === 'Positive' ? 'opacity-100' : key === 'Neutral' ? 'opacity-40' : 'opacity-10'"
                     :style="`width: ${val}%`"
                    ></div>
                 </div>
              </div>
           </div>
        </div>

        <!-- Metric Bento 1 -->
        <div class="md:col-span-3 wope-card p-8 flex flex-col justify-between">
          <p class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em]">Total Events</p>
          <div class="flex items-baseline space-x-2">
            <p class="text-4xl font-semibold tracking-tighter">{{ stats[0].value }}</p>
            <span class="text-[11px] text-white/40">nodes</span>
          </div>
        </div>

        <!-- Metric Bento 2 -->
        <div class="md:col-span-3 wope-card p-8 flex flex-col justify-between">
          <p class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em]">Fleet Strength</p>
          <div class="flex items-baseline space-x-2">
            <p class="text-4xl font-semibold tracking-tighter">{{ stats[1].value }}</p>
            <span class="text-[11px] text-white/40">active</span>
          </div>
        </div>

        <!-- Quick Action Bento -->
        <div class="md:col-span-6 wope-card p-2 flex flex-col md:flex-row gap-2">
           <NuxtLink v-for="action in quickActions" :key="action.title" :to="action.to" 
             class="flex-1 w-full bg-[#0D0D0D] border border-white/5 rounded-2xl p-6 hover:bg-[#111111] transition-all group overflow-hidden relative">
             <div class="absolute top-0 right-0 w-32 h-32 bg-white/[0.01] blur-2xl group-hover:bg-white/[0.03] transition-all"></div>
             <div class="relative z-10 flex flex-col justify-between h-full">
               <div v-html="action.icon" class="text-[#404040] group-hover:text-white transition-colors mb-4 scale-125 origin-left"></div>
               <div>
                 <h3 class="text-[14px] font-semibold text-white mb-1">{{ action.title }}</h3>
                 <p class="text-[12px] text-[#888888] leading-tight">{{ action.description }}</p>
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
      backgroundColor: ['#1A1A1A', '#404040', '#FFFFFF'],
      borderColor: '#080808',
      borderWidth: 6,
      hoverOffset: 0
    }]
  };
});

const chartOptions: ChartOptions<'doughnut'> = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    tooltip: {
      backgroundColor: '#0D0D0D',
      padding: 12,
      cornerRadius: 8,
      borderColor: '#1F1F1F',
      borderWidth: 1,
      titleFont: { size: 12, weight: 'bold' },
      bodyFont: { size: 12 },
      displayColors: false
    }
  },
  cutout: '84%'
};

const quickActions = [
  {
    title: 'Active Streams',
    description: 'Monitor real-time agent communications.',
    to: '/chats',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>'
  },
  {
    title: 'Knowledge Base',
    description: 'Inject business intelligence assets.',
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
