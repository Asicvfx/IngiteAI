<template>
  <div class="px-6 md:px-12 py-16 bg-[#080808] min-h-[calc(100vh-56px)] text-white font-sans selection:bg-white/20">
    <div class="max-w-5xl mx-auto">
      <!-- Header Section -->
      <div class="mb-20">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] gradient-text">Neural Schedule</h1>
        <p class="mt-4 text-[#888888] text-[15px] max-w-xl leading-relaxed">
          Manage your automated bookings and consultations. All temporal nodes are synchronized with your agent's executive functions.
        </p>
      </div>

      <!-- Meetings List -->
      <div class="space-y-6">
        <div v-if="meetings.length === 0" class="py-24 text-center border border-dashed border-white/5 rounded-3xl group">
          <div class="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-500">
             <div class="w-4 h-4 bg-[#1A1A1A] rounded-sm"></div>
          </div>
          <p class="text-[13px] text-[#4B5563] font-bold uppercase tracking-[0.2em]">No scheduled nodes detected.</p>
        </div>
        
        <div v-for="meeting in meetings" :key="meeting.id" 
          class="wope-card p-8 group hover:translate-y-[-2px] transition-all relative overflow-hidden">
           <div class="absolute top-0 right-0 w-32 h-32 bg-white/[0.01] blur-2xl group-hover:bg-white/[0.03] transition-all"></div>
           
           <div class="flex flex-col md:flex-row md:items-center justify-between gap-8 relative z-10">
             <div class="flex items-center space-x-6">
               <div class="w-14 h-14 rounded-2xl bg-[#0F0F0F] border border-white/5 flex items-center justify-center group-hover:bg-white group-hover:border-white transition-all duration-500">
                  <span class="text-[18px] font-semibold text-[#4B5563] group-hover:text-black transition-colors">{{ meeting.customer_name?.[0] || 'L' }}</span>
               </div>
               <div>
                 <h3 class="text-[17px] font-semibold text-white tracking-tight">{{ meeting.customer_name }}</h3>
                 <p class="text-[11px] text-[#4B5563] font-black uppercase tracking-[0.2em] mt-1">{{ meeting.customer_email }}</p>
               </div>
             </div>
             
             <div class="flex items-center justify-between md:justify-end md:space-x-16">
               <div class="text-left md:text-right">
                 <div class="text-[15px] font-bold text-white mb-1 tracking-tight">
                   {{ formatDate(meeting.start_time) }}
                 </div>
                 <div class="flex items-center md:justify-end space-x-2">
                   <div class="w-1.5 h-1.5 rounded-full" :class="meeting.status === 'confirmed' ? 'bg-white shadow-[0_0_8px_rgba(255,255,255,0.4)]' : 'bg-[#1A1A1A]'"></div>
                   <span class="text-[9px] font-black uppercase tracking-[0.3em]" :class="meeting.status === 'confirmed' ? 'text-white' : 'text-[#4B5563]'">
                     {{ meeting.status }}
                   </span>
                 </div>
               </div>

               <div class="flex space-x-3">
                  <button @click="updateStatus(meeting.id, 'confirmed')" v-if="meeting.status === 'pending'"
                    class="w-10 h-10 rounded-xl bg-white text-black flex items-center justify-center hover:bg-gray-200 transition-all shadow-lg active:scale-90">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                  </button>
                  <button @click="updateStatus(meeting.id, 'cancelled')"
                    class="w-10 h-10 rounded-xl bg-white/5 border border-white/5 text-[#4B5563] flex items-center justify-center hover:bg-red-500/10 hover:text-red-500 hover:border-red-500/20 transition-all active:scale-90">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                  </button>
               </div>
             </div>
           </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '~/stores/auth';

const auth = useAuthStore();
const config = useRuntimeConfig();
const meetings = ref<any[]>([]);

const loadMeetings = async () => {
   try {
     const data = await $fetch<any[]>(`${config.public.apiBaseUrl}/api/v1/meetings/`, {
        headers: { Authorization: `Bearer ${auth.token}` }
     });
     meetings.value = data;
   } catch (e) {
     console.error(e);
   }
};

const updateStatus = async (id: number, status: string) => {
  try {
    await $fetch(`${config.public.apiBaseUrl}/api/v1/meetings/${id}/`, {
      method: 'PATCH',
      body: { status },
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    await loadMeetings();
  } catch (e) {
    console.error(e);
  }
}

const formatDate = (dateStr: string) => {
  return new Date(dateStr).toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

onMounted(loadMeetings);
</script>

</script>
