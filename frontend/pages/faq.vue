<template>
  <div class="px-6 md:px-12 py-16 bg-[#080808] min-h-[calc(100vh-56px)] text-white font-sans">
    <div class="max-w-5xl mx-auto">
      <!-- Header Section -->
      <div class="mb-20">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] gradient-text">Intelligence Base</h1>
        <p class="mt-4 text-[#888888] text-[15px] leading-relaxed max-w-xl">
          Train your neural agents with domain-specific knowledge assets. Synchronize documents and structured data directly into the core intelligence layer.
        </p>
      </div>
      
      <!-- Knowledge Injection Section -->
      <div class="mb-24 wope-card p-10 overflow-hidden relative">
        <div class="absolute top-0 right-0 w-64 h-64 bg-white/[0.02] blur-3xl rounded-full -translate-y-1/2 translate-x-1/2"></div>
        
        <div class="flex items-center justify-between mb-12 pb-8 border-b border-white/5 relative z-10">
          <div>
            <h2 class="text-lg font-medium tracking-tight">Inject Knowledge</h2>
            <p class="text-[12px] text-[#4B5563] mt-1 uppercase tracking-widest font-bold">Synchronize neural pathways</p>
          </div>
          <div class="flex space-x-1 bg-[#0D0D0D] p-1.5 rounded-xl border border-white/5">
            <button @click="activeTab = 'text'" :class="activeTab === 'text' ? 'bg-white text-black shadow-lg' : 'text-[#888888] hover:text-white'" class="px-5 py-2 rounded-lg text-[11px] font-bold transition-all uppercase tracking-wider">Manual Nodes</button>
            <button @click="activeTab = 'file'" :class="activeTab === 'file' ? 'bg-white text-black shadow-lg' : 'text-[#888888] hover:text-white'" class="px-5 py-2 rounded-lg text-[11px] font-bold transition-all uppercase tracking-wider">Cloud Assets</button>
          </div>
        </div>

        <form @submit.prevent="createItem" class="space-y-10 relative z-10">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="space-y-3">
              <label class="text-[11px] font-bold text-[#4B5563] uppercase tracking-[0.2em]">Target Agent</label>
              <div class="relative group">
                <select v-model="newItem.bot" required class="w-full bg-[#0D0D0D] border border-white/5 rounded-xl px-5 py-4 text-[14px] text-white focus:border-white/20 outline-none transition-all appearance-none cursor-pointer group-hover:border-white/10">
                  <option v-for="bot in bots" :key="bot.id" :value="bot.id" class="bg-[#0D0D0D] text-white">{{ bot.name }}</option>
                </select>
                <div class="absolute right-5 top-1/2 -translate-y-1/2 pointer-events-none text-[#4B5563]">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </div>
              </div>
            </div>
            <div class="space-y-3">
              <label class="text-[11px] font-bold text-[#4B5563] uppercase tracking-[0.2em]">Asset Label</label>
              <input v-model="newItem.title" type="text" placeholder="e.g. Service Protocols" required class="w-full bg-[#0D0D0D] border border-white/5 rounded-xl px-5 py-4 text-[14px] text-white focus:border-white/20 outline-none transition-all placeholder-[#262626]">
            </div>
          </div>

          <div v-if="activeTab === 'text'" class="space-y-3">
            <label class="text-[11px] font-bold text-[#4B5563] uppercase tracking-[0.2em]">Contextual Data</label>
            <textarea v-model="newItem.content" rows="6" placeholder="Enter structured business data, FAQs, or operational guidelines..." required class="w-full bg-[#0D0D0D] border border-white/5 rounded-xl px-5 py-4 text-[14px] text-white focus:border-white/20 outline-none transition-all resize-none placeholder-[#262626] leading-relaxed"></textarea>
          </div>

          <div v-else class="space-y-4">
            <div class="relative group h-40 border border-dashed border-white/10 hover:border-white/30 rounded-2xl transition-all flex flex-col items-center justify-center cursor-pointer overflow-hidden bg-white/5">
              <input type="file" @change="onFileChange" class="absolute inset-0 opacity-0 cursor-pointer z-20" accept=".pdf,.doc,.docx,.xls,.xlsx,.txt">
              <div class="text-center group-hover:scale-105 transition-transform duration-500">
                <div class="w-12 h-12 bg-white/10 rounded-xl flex items-center justify-center mx-auto mb-4 border border-white/5">
                  <svg class="w-6 h-6 text-white opacity-40 group-hover:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
                </div>
                <p class="text-[13px] font-semibold text-white tracking-tight">{{ selectedFile ? selectedFile.name : 'Upload Neural Asset' }}</p>
                <p class="text-[10px] text-[#4B5563] uppercase tracking-[0.1em] mt-1">PDF, DOCX, TXT UP TO 10MB</p>
              </div>
            </div>
          </div>

          <div class="flex justify-end pt-4">
            <button type="submit" class="wope-button-primary !px-12 !py-4 shadow-2xl">
               Synchronize Architecture
            </button>
          </div>
        </form>
      </div>

      <!-- Archives Grid -->
      <div class="space-y-10">
        <h2 class="text-[11px] font-bold text-[#4B5563] uppercase tracking-[0.3em] pl-1">Synchronized Archives</h2>
        
        <div v-if="items.length === 0" class="py-24 text-center border border-dashed border-white/5 rounded-3xl group">
           <div class="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform">
             <div class="w-4 h-4 bg-[#1F1F1F] rounded-sm"></div>
           </div>
           <p class="text-[13px] text-[#4B5563] font-medium tracking-tight">No intelligence nodes detected in the current fleet.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div v-for="item in items" :key="item.id" class="wope-card p-8 group hover:translate-y-[-4px] transition-all">
             <div class="flex items-start justify-between mb-8">
               <div class="w-12 h-12 rounded-xl bg-[#0F0F0F] border border-white/5 flex items-center justify-center group-hover:bg-white group-hover:border-white transition-all duration-500">
                 <svg v-if="item.item_type === 'file'" class="w-5 h-5 text-[#4B5563] group-hover:text-black transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                 <svg v-else class="w-5 h-5 text-[#4B5563] group-hover:text-black transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg>
               </div>
               <button @click="deleteItem(item.id)" class="text-[#1A1A1A] hover:text-red-400 p-2 transition-all">
                 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
               </button>
             </div>
             
             <div>
               <div class="flex items-center justify-between mb-2">
                 <h3 class="text-[17px] font-semibold tracking-tight text-white">{{ item.title }}</h3>
                 <span class="text-[9px] font-bold text-[#4B5563] bg-white/5 px-2 py-0.5 rounded border border-white/5 uppercase tracking-wider">{{ item.item_type }}</span>
               </div>
               <p class="text-[12px] font-bold text-[#4B5563] uppercase tracking-widest mb-4">Uplink: {{ getBotName(item.bot) }}</p>
               <p class="text-[14px] text-[#888888] leading-relaxed line-clamp-3 font-medium">{{ item.content || '(Binary source node synchronized via cloud uplink)' }}</p>
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
const items = ref<any[]>([]);
const bots = ref<any[]>([]);
const activeTab = ref<'text' | 'file'>('text');
const newItem = ref({
  bot: null as any,
  title: '',
  content: '',
  item_type: 'text' as 'text' | 'file'
});
const selectedFile = ref<File | null>(null);

onMounted(async () => {
  await loadBots();
  await loadItems();
});

const loadBots = async () => {
  try {
    const data = await $fetch<any[]>(`${config.public.apiBaseUrl}/api/v1/bots/`, {
       headers: { Authorization: `Bearer ${auth.token}` }
    });
    bots.value = data;
    if (bots.value.length > 0) newItem.value.bot = bots.value[0].id;
  } catch (e) { console.error(e) }
};

const loadItems = async () => {
  try {
    const data = await $fetch<any[]>(`${config.public.apiBaseUrl}/api/v1/bots/knowledge/`, {
       headers: { Authorization: `Bearer ${auth.token}` }
    });
    items.value = data;
  } catch (e) { console.error(e) }
};

const onFileChange = (e: any) => {
  selectedFile.value = e.target.files[0];
  if (selectedFile.value && !newItem.value.title) {
    newItem.value.title = selectedFile.value.name;
  }
};

const createItem = async () => {
  try {
    const formData = new FormData();
    formData.append('bot', newItem.value.bot);
    formData.append('title', newItem.value.title);
    formData.append('item_type', activeTab.value);
    
    if (activeTab.value === 'file' && selectedFile.value) {
      formData.append('file', selectedFile.value);
    } else {
      formData.append('content', newItem.value.content);
    }

    await $fetch(`${config.public.apiBaseUrl}/api/v1/bots/knowledge/`, {
      method: 'POST',
      body: formData,
      headers: { Authorization: `Bearer ${auth.token}` }
    });

    newItem.value.title = ''; newItem.value.content = ''; selectedFile.value = null;
    await loadItems();
  } catch (e) { console.error(e) }
};

const deleteItem = async (id: number) => {
  if (!confirm('Purge this intelligence node?')) return;
  try {
     await $fetch(`${config.public.apiBaseUrl}/api/v1/bots/knowledge/${id}/`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    await loadItems();
  } catch (e) { console.error(e) }
};

const getBotName = (botId: number) => {
  const bot = bots.value.find(b => b.id === botId);
  return bot ? bot.name : 'Unknown Agent';
};
</script>
