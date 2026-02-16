<template>
  <div class="px-10 py-12 bg-black min-h-[calc(100vh-56px)] text-white font-sans">
    <div class="max-w-6xl mx-auto">
      <!-- Header Section -->
      <div class="mb-16">
        <h1 class="text-3xl font-semibold tracking-[-0.022em] text-white">Intelligence Overview</h1>
        <p class="mt-2 text-[#6B7280] text-[14px] flex items-center">
          <span class="w-1.5 h-1.5 bg-white rounded-full mr-2 opacity-50"></span>
          Real-time neural metrics and lead classification.
        </p>
      </div>

      <!-- Stats Grid (Reflect Style) -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-16">
        <div v-for="stat in stats" :key="stat.name" class="p-6 bg-black border border-[#1A1A1A] rounded-xl">
          <p class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em] mb-4">{{ stat.name }}</p>
          <p class="text-3xl font-medium tracking-[-0.011em] text-white">{{ stat.value }}</p>
        </div>
      </div>

      <!-- Main Columns -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        <!-- Chart Section -->
        <div class="lg:col-span-8 space-y-12">
          <div class="p-8 bg-black border border-[#1A1A1A] rounded-2xl">
             <div class="flex items-center justify-between mb-10">
               <div>
                 <h2 class="text-lg font-medium tracking-tight">Lead Classification</h2>
                 <p class="text-[12px] text-[#6B7280] mt-1">Classification across the agent fleet</p>
               </div>
               <div class="flex items-center space-x-4">
                 <div class="flex items-center space-x-1.5 font-medium text-[11px] text-[#6B7280]">
                    <span class="w-2 h-2 rounded-full border border-[#1A1A1A]"></span>
                    <span>Cold</span>
                 </div>
                 <div class="flex items-center space-x-1.5 font-medium text-[11px] text-[#6B7280]">
                    <span class="w-2 h-2 rounded-full border border-white opacity-40"></span>
                    <span>Warm</span>
                 </div>
                 <div class="flex items-center space-x-1.5 font-medium text-[11px] text-white">
                    <span class="w-2 h-2 rounded-full bg-white"></span>
                    <span>Hot</span>
                 </div>
               </div>
             </div>
             
             <div class="h-64 relative">
               <Doughnut v-if="chartData" :data="chartData" :options="chartOptions" />
               <div v-else class="h-full flex items-center justify-center border border-dashed border-[#1A1A1A] rounded-xl">
                 <span class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em]">Aggregating Intelligence...</span>
               </div>
             </div>
          </div>

          <!-- Focused Action Links -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <NuxtLink v-for="action in quickActions" :key="action.title" :to="action.to" 
              class="flex flex-col p-6 rounded-xl border border-[#1A1A1A] hover:border-white/20 transition-all duration-300 group">
              <div class="flex items-center justify-between mb-3">
                 <div v-html="action.icon" class="text-[#6B7280] group-hover:text-white transition-colors"></div>
                 <svg class="w-4 h-4 text-[#262626] group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </div>
              <h3 class="text-[14px] font-medium text-white mb-1">{{ action.title }}</h3>
              <p class="text-[12px] text-[#6B7280] leading-relaxed">{{ action.description }}</p>
            </NuxtLink>
          </div>
        </div>

        <!-- Right Side: Sentiment -->
        <div class="lg:col-span-4 space-y-8">
           <div class="p-8 bg-black border border-[#1A1A1A] rounded-2xl h-full">
              <h2 class="text-sm font-medium text-[#6B7280] uppercase tracking-[0.1em] mb-12">Neural Sentiment</h2>
              
              <div class="space-y-10">
                 <div v-for="(val, key) in sentiment" :key="key">
                    <div class="flex justify-between items-baseline mb-3">
                       <span class="text-[13px] font-medium text-[#9CA3AF]">{{ key }}</span>
                       <span class="text-[15px] font-medium text-white">{{ val }}%</span>
                    </div>
                    <div class="h-[3px] bg-[#1A1A1A] rounded-full overflow-hidden">
                       <div class="h-full bg-white transition-all duration-700"
                        :class="key === 'Positive' ? 'opacity-100' : key === 'Neutral' ? 'opacity-40' : 'opacity-10'"
                        :style="`width: ${val}%`"
                       ></div>
                    </div>
                 </div>
              </div>

              <div class="mt-20 p-5 rounded-lg border border-dashed border-[#1A1A1A]">
                <p class="text-[11px] text-[#4B5563] leading-relaxed">
                  System health optimal. All neural pathways synchronized.
                </p>
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
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js';

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
      borderColor: '#000000',
      borderWidth: 4,
      hoverOffset: 0
    }]
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    tooltip: {
      backgroundColor: '#0D0D0D',
      padding: 12,
      cornerRadius: 6,
      borderColor: '#262626',
      borderWidth: 1,
      titleFont: { size: 12, weight: 'semibold' },
      bodyFont: { size: 12 }
    }
  },
  cutout: '82%'
};

const quickActions = [
  {
    title: 'Active Streams',
    description: 'Monitor real-time agent communications.',
    to: '/chats',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>'
  },
  {
    title: 'Knowledge Core',
    description: 'Manage business intelligence assets.',
    to: '/faq',
    icon: '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>'
  }
];

onMounted(async () => {
  try {
    const data = await $fetch<any>('http://localhost:8000/api/v1/dashboard/analytics/', { 
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    analyticsData.value = data;
    
    stats.value[0].value = data.metrics.total_messages.toString();
    stats.value[1].value = data.metrics.total_conversations.toString(); 
    stats.value[3].value = data.metrics.hot_leads.toString();
    
    const total = data.metrics.total_conversations || 1;
    sentiment.value.Positive = Math.round((data.sentiment.positive / total) * 100);
    sentiment.value.Neutral = Math.round((data.sentiment.neutral / total) * 100);
    sentiment.value.Escalated = Math.round((data.sentiment.needs_attention / total) * 100);
    
  } catch (err) {
    console.error('Failed to fetch analytics', err);
  }
});
</script>
