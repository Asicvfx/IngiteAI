<template>
  <div class="px-10 py-12 bg-black min-h-[calc(100vh-56px)] text-white font-sans">
    <div class="max-w-4xl mx-auto">
      <div class="mb-16">
        <h1 class="text-3xl font-semibold tracking-[-0.022em]">Intelligence Base</h1>
        <p class="mt-2 text-[#6B7280] text-[14px]">Train your neural agents with domain-specific knowledge.</p>
      </div>
      
      <!-- Add New Item Section (Reflect Style) -->
      <div class="mb-20 p-8 bg-black border border-[#1A1A1A] rounded-2xl">
        <div class="flex items-center justify-between mb-10 pb-6 border-b border-[#1A1A1A]">
          <h2 class="text-[14px] font-medium text-white uppercase tracking-[0.1em]">Inject Knowledge</h2>
          <div class="flex space-x-1 bg-[#0D0D0D] p-1 rounded-lg border border-[#1A1A1A]">
            <button @click="activeTab = 'text'" :class="activeTab === 'text' ? 'bg-white text-black' : 'text-[#6B7280] hover:text-white'" class="px-4 py-1.5 rounded-md text-[11px] font-medium transition-all">Text Article</button>
            <button @click="activeTab = 'file'" :class="activeTab === 'file' ? 'bg-white text-black' : 'text-[#6B7280] hover:text-white'" class="px-4 py-1.5 rounded-md text-[11px] font-medium transition-all">Upload File</button>
          </div>
        </div>

        <form @submit.prevent="createItem" class="space-y-8">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-2">
              <label class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em]">Target Agent</label>
              <select v-model="newItem.bot" required class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all appearance-none cursor-pointer">
                <option v-for="bot in bots" :key="bot.id" :value="bot.id" class="bg-black text-white">{{ bot.name }}</option>
              </select>
            </div>
            <div class="space-y-2">
              <label class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em]">Label</label>
              <input v-model="newItem.title" type="text" placeholder="e.g. Service Protocols" required class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all placeholder-[#262626]">
            </div>
          </div>

          <div v-if="activeTab === 'text'" class="space-y-2">
            <label class="text-[11px] font-medium text-[#6B7280] uppercase tracking-[0.1em]">Content</label>
            <textarea v-model="newItem.content" rows="4" placeholder="Enter structured business data..." required class="w-full bg-black border border-[#1A1A1A] rounded-xl px-4 py-3 text-[14px] text-white focus:border-white/30 outline-none transition-all resize-none placeholder-[#262626]"></textarea>
          </div>

          <div v-else class="space-y-4">
            <div class="relative group h-32 border border-dashed border-[#1A1A1A] hover:border-white/30 rounded-xl transition-all flex flex-col items-center justify-center cursor-pointer overflow-hidden">
              <input type="file" @change="onFileChange" class="absolute inset-0 opacity-0 cursor-pointer z-20" accept=".pdf,.doc,.docx,.xls,.xlsx,.txt">
              <div class="text-center opacity-40 group-hover:opacity-100 transition-opacity">
                <svg class="w-6 h-6 text-white mb-2 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
                <p class="text-[12px] font-medium">{{ selectedFile ? selectedFile.name : 'Click or drop file' }}</p>
              </div>
            </div>
          </div>

          <div class="flex justify-end">
            <button type="submit" class="px-8 py-3 bg-white text-black text-[13px] font-semibold rounded-xl hover:bg-gray-200 transition active:scale-95">
               Synchronize Knowledge
            </button>
          </div>
        </form>
      </div>

      <!-- Knowledge List -->
      <div class="space-y-4">
        <h2 class="text-[11px] font-medium text-[#4B5563] uppercase tracking-[0.2em] mb-8">Synchronized Archives</h2>
        <div v-if="items.length === 0" class="py-12 text-center border border-dashed border-[#1A1A1A] rounded-xl">
           <p class="text-[12px] text-[#4B5563]">No knowledge nodes detected.</p>
        </div>
        
        <div v-for="item in items" :key="item.id" class="p-6 bg-black border border-[#1A1A1A] rounded-xl hover:border-white/20 transition-all flex items-start space-x-6">
           <div class="w-10 h-10 rounded-lg bg-[#0D0D0D] border border-[#1A1A1A] flex items-center justify-center shrink-0">
             <svg v-if="item.item_type === 'file'" class="w-5 h-5 text-[#6B7280]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
             <svg v-else class="w-5 h-5 text-[#6B7280]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg>
           </div>
           
           <div class="flex-1 min-w-0">
             <div class="flex items-center justify-between mb-3">
               <div>
                 <h3 class="text-[14px] font-medium text-white">{{ item.title }}</h3>
                 <p class="text-[11px] text-[#6B7280] font-medium mt-0.5">Assigned to {{ getBotName(item.bot) }}</p>
               </div>
               <button @click="deleteItem(item.id)" class="text-[#262626] hover:text-red-400 transition-colors">
                 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
               </button>
             </div>
             <p class="text-[13px] text-[#9CA3AF] leading-relaxed line-clamp-2">{{ item.content || '(Binary source node)' }}</p>
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
    items.value = await $fetch<any[]>(`${config.public.apiBaseUrl}/api/v1/bots/knowledge/`, {
       headers: { Authorization: `Bearer ${auth.token}` }
    });
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
