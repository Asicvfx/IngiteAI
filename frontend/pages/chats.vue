<template>
  <div class="flex h-[calc(100vh-56px)] bg-[#080808] text-white overflow-hidden font-sans relative">
    <!-- Sidebar / Chat List -->
    <div class="w-80 md:w-96 border-r border-white/5 bg-[#080808] flex flex-col z-20 overflow-hidden">
      <div class="p-10">
        <h2 class="text-3xl font-semibold tracking-[-0.04em] gradient-text">Streams</h2>
        <p class="text-[13px] text-[#888888] mt-2">Active neural synchronizations</p>
      </div>
      
      <div class="flex-1 overflow-y-auto wope-scroll px-4 pb-10 space-y-1">
        <div 
          v-for="chat in chats" 
          :key="chat.id" 
          @click="selectChat(chat)" 
          class="group p-5 rounded-2xl cursor-pointer transition-all duration-300 border border-transparent"
          :class="selectedChat?.id === chat.id ? 'bg-white/5 border-white/10' : 'hover:bg-white/[0.02]'"
        >
          <div class="flex items-center space-x-5">
            <div class="w-11 h-11 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-[13px] font-semibold text-[#888888] group-hover:text-white transition-colors">
              {{ chat.telegram_chat_id ? chat.telegram_chat_id.toString().slice(-2) : '?' }}
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between mb-1.5">
                <span class="text-[14px] font-semibold tracking-tight truncate text-white">Node #{{ chat.telegram_chat_id }}</span>
                <span v-if="chat.needs_human" class="w-1.5 h-1.5 bg-white rounded-full animate-pulse shadow-[0_0_8px_rgba(255,255,255,0.5)]"></span>
              </div>
              <p class="text-[12px] text-[#4B5563] truncate leading-normal">
                {{ chat.last_message?.content || 'Awaiting uplink...' }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Chat Area -->
    <div class="flex-1 flex flex-col relative z-10 bg-[#080808]">
      <div v-if="selectedChat" class="flex-1 flex flex-col h-full max-w-5xl mx-auto w-full">
        <!-- Header -->
        <header class="h-20 border-b border-white/5 flex items-center px-12 justify-between bg-[#080808]/50 backdrop-blur-md">
          <div class="flex items-center space-x-4">
            <h3 class="text-[16px] font-semibold tracking-tight text-white">Stream #{{ selectedChat.telegram_chat_id }}</h3>
            <div class="flex items-center space-x-1.5 bg-white/5 px-2.5 py-1 rounded-full border border-white/5">
               <div class="w-1 h-1 bg-white rounded-full opacity-40"></div>
               <span class="text-[9px] font-bold text-[#4B5563] uppercase tracking-[0.15em]">Uplink Stable</span>
            </div>
          </div>
          <div class="text-[11px] text-[#4B5563] font-semibold uppercase tracking-wider">
             {{ chats.length }} Live Nodes
          </div>
        </header>

        <!-- Messages Area -->
        <div ref="messageContainer" class="flex-1 overflow-y-auto wope-scroll px-12 py-16 space-y-12 scroll-smooth">
          <TransitionGroup name="stream">
          <div v-for="msg in messages" :key="msg.id" 
            class="flex flex-col group animate-slide-up"
            :class="msg.sender === 'user' ? 'items-start' : 'items-end'"
          >
            <div class="max-w-[80%]">
              <div 
                class="px-6 py-4 rounded-2xl relative transition-all duration-300"
                :class="[
                  msg.sender === 'user' 
                    ? 'bg-[#0E0E0E] border border-white/5 text-[#EDEDED]' 
                    : 'bg-white text-black font-medium shadow-[0_10px_30px_rgba(255,255,255,0.05)]'
                ]"
              >
                <p class="text-[15px] leading-relaxed tracking-normal">{{ msg.content }}</p>

                <!-- Product Display -->
                <div v-if="msg.metadata?.products?.length" class="mt-6 space-y-3">
                  <div v-for="product in msg.metadata.products" :key="product.name" 
                    class="p-4 bg-white/5 border border-white/5 rounded-2xl flex items-center space-x-4 hover:border-white/20 transition-all group/prod">
                    <img v-if="product.image_url" :src="product.image_url" class="w-12 h-12 rounded-xl object-cover bg-black">
                    <div class="flex-1 text-left">
                      <h4 class="text-[13px] font-semibold text-white group-hover/prod:text-white transition-colors">{{ product.name }}</h4>
                      <p class="text-[12px] text-[#888888]">{{ product.price }}</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Quick Action Pills -->
              <div v-if="msg.metadata?.quick_replies?.length" class="mt-5 flex flex-wrap gap-2.5" :class="msg.sender !== 'user' ? 'justify-end' : 'justify-start'">
                <button 
                  v-for="reply in msg.metadata.quick_replies" 
                  :key="reply"
                  @click="sendQuickReply(reply)"
                  class="wope-button-secondary !py-2 !px-4 !text-[11px] !rounded-full !tracking-normal !bg-white/5 border-white/5"
                >
                  {{ reply }}
                </button>
              </div>

              <div class="mt-3 px-1 text-[10px] text-[#4B5563] font-bold uppercase tracking-[0.1em]">
                {{ formatTime(msg.created_at) }}
              </div>
            </div>
          </div>
          </TransitionGroup>
        </div>

        <!-- Input Bar -->
        <div class="px-12 pb-12 pt-4">
          <div class="max-w-4xl mx-auto">
            <div class="relative wope-card p-1.5 focus-within:border-white/30 transition-all">
              <div class="flex items-center px-4 bg-[#0E0E0E] rounded-xl border border-white/5 focus-within:border-white/10">
                <input 
                  v-model="newMessage" 
                  @keydown.enter.prevent="sendMessage"
                  type="text" 
                  class="flex-1 bg-transparent border-none focus:ring-0 text-white placeholder-[#404040] py-5 text-[15px] tracking-tight" 
                  placeholder="Direct neural override..."
                >
                <button 
                  @click="sendMessage"
                  :disabled="!newMessage.trim() || sending"
                  class="wope-button-primary !p-3 !rounded-xl disabled:opacity-20 shadow-xl"
                >
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </button>
              </div>
            </div>
            <div class="mt-4 flex items-center justify-center space-x-4 opacity-20">
               <div class="h-px w-20 bg-white"></div>
               <span class="text-[10px] font-bold uppercase tracking-[0.2em] text-white">Administrator Terminal</span>
               <div class="h-px w-20 bg-white"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="flex-1 flex items-center justify-center bg-[#080808]">
        <div class="text-center group">
          <div class="w-16 h-16 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mx-auto mb-8 group-hover:scale-110 group-hover:bg-white transition-all duration-500">
            <div class="w-5 h-5 bg-[#1F1F1F] rounded group-hover:bg-black transition-colors"></div>
          </div>
          <h2 class="text-2xl font-semibold tracking-tighter text-white mb-3">Select a stream</h2>
          <p class="text-[14px] text-[#4B5563] max-w-[240px] mx-auto leading-relaxed">Select an active neural node from the sidebar to begin oversight.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick, watch } from 'vue';
import { useAuthStore } from '~/stores/auth';

const auth = useAuthStore();
const config = useRuntimeConfig();
const chats = ref<any[]>([]);
const messages = ref<any[]>([]);
const selectedChat = ref<any | null>(null);
const newMessage = ref('');
const sending = ref(false);
const messageContainer = ref<HTMLElement | null>(null);
const socket = ref<WebSocket | null>(null);

onMounted(async () => {
  await loadChats();
  connectWebSocket();
});

const connectWebSocket = () => {
  const wsBase = config.public.apiBaseUrl.replace('http', 'ws');
  const wsUrl = `${wsBase}/ws/chat/`;
  socket.value = new WebSocket(wsUrl);

  socket.value.onopen = () => console.log('Uplink active.');

  socket.value.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const chatIndex = chats.value.findIndex(c => c.id === data.conversation);
    if (chatIndex !== -1) {
      chats.value[chatIndex].last_message = data;
      chats.value[chatIndex].updated_at = data.created_at;
      chats.value.sort((a, b) => new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime());
    } else {
      loadChats();
    }

    if (selectedChat.value && selectedChat.value.id === data.conversation) {
      if (!messages.value.find(m => m.id === data.id)) {
        messages.value.push(data);
        scrollToBottom();
      }
    }
  };

  socket.value.onclose = () => setTimeout(connectWebSocket, 5000);
};

const loadChats = async () => {
  try {
    const data = await $fetch<any[]>(`${config.public.apiBaseUrl}/api/v1/conversations/`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    chats.value = data.sort((a, b) => new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime());
  } catch (error) {
    console.error(error);
  }
};

const selectChat = async (chat: any) => {
  selectedChat.value = chat;
  await loadMessages(chat.id);
};

const loadMessages = async (chatId: number) => {
  try {
    const data = await $fetch<any[]>(`${config.public.apiBaseUrl}/api/v1/messages/?conversation=${chatId}`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    messages.value = data;
    await scrollToBottom();
  } catch (error) {
    console.error(error);
  }
};

const sendMessage = async () => {
  if (!newMessage.value.trim() || !selectedChat.value || sending.value) return;
  await performMessageSend(newMessage.value);
  newMessage.value = '';
};

const sendQuickReply = async (reply: string) => {
  if (!selectedChat.value || sending.value) return;
  await performMessageSend(reply);
};

const performMessageSend = async (content: string) => {
  sending.value = true;
  try {
    const msg = await $fetch<any>(`${config.public.apiBaseUrl}/api/v1/messages/`, {
      method: 'POST',
      body: { conversation: selectedChat.value.id, content, sender: 'admin' },
      headers: { Authorization: `Bearer ${auth.token}` }
    });
    messages.value.push(msg);
    await loadChats();
    await scrollToBottom();
  } catch (error) {
    console.error(error);
  } finally {
    sending.value = false;
  }
};

const scrollToBottom = async () => {
  await nextTick();
  if (messageContainer.value) {
    messageContainer.value.scrollTop = messageContainer.value.scrollHeight;
  }
};

const formatTime = (isoString: string) => {
  const date = new Date(isoString);
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
};

watch(selectedChat, (newVal) => {
  if (newVal) scrollToBottom();
});
</script>

<style scoped>
.stream-enter-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.stream-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-slide-up {
  animation: slide-up 0.5s ease-out forwards;
}
</style>



<style scoped>
.fade-enter-active {
  transition: all 0.3s ease-out;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
</style>
