<template>
  <div class="px-10 py-12 bg-black min-h-[calc(100vh-56px)] text-white font-sans selection:bg-white/20">
    <div class="max-w-4xl mx-auto">
      <div class="mb-16">
        <h1 class="text-3xl font-semibold tracking-[-0.022em]">Schedule</h1>
        <p class="mt-2 text-[#6B7280] text-[14px]">Manage your automated bookings and consultations.</p>
      </div>

      <!-- Meetings List -->
      <div class="space-y-4">
        <div v-if="meetings.length === 0" class="py-20 text-center border border-dashed border-[#1A1A1A] rounded-2xl">
          <p class="text-[13px] text-[#4B5563]">No scheduled meetings detected.</p>
        </div>
        
        <div v-for="meeting in meetings" :key="meeting.id" 
          class="p-6 bg-black border border-[#1A1A1A] rounded-xl hover:border-white/20 transition-all">
           <div class="flex items-center justify-between">
             <div class="flex items-center space-x-6">
               <div class="w-10 h-10 rounded-lg bg-[#0D0D0D] border border-[#1A1A1A] flex items-center justify-center">
                  <span class="text-[13px] font-semibold text-[#6B7280]">{{ meeting.customer_name?.[0] || 'L' }}</span>
               </div>
               <div>
                 <h3 class="text-[14px] font-medium text-white">{{ meeting.customer_name }}</h3>
                 <p class="text-[11px] text-[#6B7280] font-medium mt-0.5">{{ meeting.customer_email }}</p>
               </div>
             </div>
             
             <div class="flex items-center space-x-12">
               <div class="text-right">
                 <div class="text-[13px] font-medium text-white mb-1">
                   {{ formatDate(meeting.start_time) }}
                 </div>
                 <div class="text-[10px] font-medium uppercase tracking-[0.1em]" :class="meeting.status === 'confirmed' ? 'text-white' : 'text-[#4B5563]'">
                   {{ meeting.status }}
                 </div>
               </div>

               <div class="flex space-x-2">
                  <button @click="updateStatus(meeting.id, 'confirmed')" v-if="meeting.status === 'pending'"
                    class="p-2 rounded-lg border border-[#1A1A1A] hover:border-white/20 text-[#6B7280] hover:text-white transition-all">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                  </button>
                  <button @click="updateStatus(meeting.id, 'cancelled')"
                    class="p-2 rounded-lg border border-[#1A1A1A] hover:border-white/20 text-[#6B7280] hover:text-red-400 transition-all">
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
