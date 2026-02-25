<template>
  <div class="flex h-[calc(100vh-56px)] text-white overflow-hidden font-sans relative">


    <!-- Sidebar / Chat List -->
    <div class="w-80 md:w-96 border-r border-white/5 bg-[#0A0A0B]/60 backdrop-blur-xl flex flex-col z-20 overflow-hidden relative">
      <div class="p-10 relative z-10">
        <h2 class="text-3xl font-semibold tracking-[-0.04em] text-white">Live Streams</h2>
        <p class="text-[13px] text-[#A1A1AA] mt-2 font-medium">Monitor your active customer conversations</p>
      </div>
      
      <div class="flex-1 overflow-y-auto wope-scroll px-4 pb-10 space-y-2 relative z-10">
        <div 
          v-for="chat in chats" 
          :key="chat.id" 
          @click="selectChat(chat)" 
          class="group p-5 rounded-2xl cursor-pointer transition-all duration-300 border"
          :class="selectedChat?.id === chat.id ? 'bg-[#111] border-[#333] shadow-lg' : 'bg-transparent border-transparent hover:bg-white/[0.02] hover:border-white/5'"
        >
          <div class="flex items-center space-x-5">
            <div class="w-11 h-11 rounded-2xl bg-[#0A0A0B] border border-[#222] flex items-center justify-center text-[13px] font-semibold text-[#888888] group-hover:text-white group-hover:border-[#444] transition-all shadow-inner">
              {{ chat.telegram_chat_id ? chat.telegram_chat_id.toString().slice(-2) : '?' }}
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between mb-1.5">
                <span class="text-[14px] font-semibold tracking-tight truncate text-[#E4E4E5]">Customer #{{ chats.indexOf(chat) + 1 }}</span>
                <span v-if="chat.needs_human" class="w-2 h-2 bg-[#A855F7] rounded-full animate-pulse shadow-[0_0_12px_rgba(168,85,247,0.8)]"></span>
              </div>
              <p class="text-[12px] text-[#A1A1AA] truncate leading-normal font-medium">
                {{ chat.last_message?.content || 'Awaiting uplink...' }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Chat Area -->
    <div class="flex-1 flex flex-col relative z-10 bg-transparent">
      <div v-if="selectedChat" class="flex-1 flex flex-col h-full max-w-5xl mx-auto w-full relative">
        <!-- Header -->
        <header class="h-20 border-b border-white/5 flex items-center px-12 justify-between backdrop-blur-xl relative z-20">
          <div class="flex items-center space-x-4">
            <h3 class="text-[16px] font-semibold tracking-tight text-white">Customer #{{ chats.indexOf(selectedChat) + 1 }}</h3>
            <div class="flex items-center space-x-1.5 bg-[#111] px-3 py-1.5 rounded-full border border-[#222] shadow-inner">
               <div class="w-1.5 h-1.5 bg-[#A855F7] rounded-full opacity-80 animate-pulse"></div>
               <span class="text-[9px] font-bold text-[#A1A1AA] uppercase tracking-[0.15em]">Active</span>
            </div>
          </div>
          <div class="text-[11px] text-[#A1A1AA] font-bold uppercase tracking-wider">
             {{ chats.length }} Active Chats
          </div>
        </header>

        <!-- Messages Area -->
        <div ref="messageContainer" class="flex-1 overflow-y-auto wope-scroll px-12 py-16 space-y-12 scroll-smooth relative z-10">
          <TransitionGroup name="stream">
          <div v-for="msg in messages" :key="msg.id" 
            class="flex flex-col group animate-slide-up"
            :class="msg.sender === 'user' ? 'items-start' : 'items-end'"
          >
            <div class="max-w-[80%]">
              <div 
                class="px-6 py-4 rounded-3xl relative transition-all duration-300"
                :class="[
                  msg.sender === 'user' 
                    ? 'bg-[#111] border border-[#222] text-[#E4E4E5]' 
                    : 'bg-white text-black font-semibold shadow-[0_10px_40px_rgba(255,255,255,0.1)]'
                ]"
              >
                <p class="text-[15px] leading-relaxed tracking-tight">{{ msg.content }}</p>

                <!-- Product Display -->
                <div v-if="msg.metadata?.products?.length" class="mt-6 space-y-3">
                  <div v-for="product in msg.metadata.products" :key="product.name" 
                    class="p-4 bg-[#050505] border border-[#222] rounded-2xl flex items-center space-x-4 hover:border-[#444] transition-all group/prod">
                    <img v-if="product.image_url" :src="product.image_url" class="w-12 h-12 rounded-xl object-cover bg-black">
                    <div class="flex-1 text-left">
                      <h4 class="text-[13px] font-semibold text-white group-hover/prod:text-[#A855F7] transition-colors">{{ product.name }}</h4>
                      <p class="text-[12px] text-[#A1A1AA] font-medium">{{ product.price }}</p>
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
                  class="bg-[#111] hover:bg-[#222] text-[#E4E4E5] font-semibold py-2 px-5 text-[12px] rounded-full border border-[#222] hover:border-[#444] transition-all tracking-tight shadow-sm"
                >
                  {{ reply }}
                </button>
              </div>

              <div class="mt-3 px-2 text-[10px] text-[#4B5563] font-bold uppercase tracking-[0.1em]">
                {{ formatTime(msg.created_at) }}
              </div>
            </div>
          </div>
          </TransitionGroup>
        </div>

        <!-- Input Bar -->
        <div class="px-12 pb-12 pt-4 relative z-20">
          <div class="max-w-4xl mx-auto">
            <div class="relative bg-[#050505]/90 rounded-2xl p-1.5 focus-within:border-[#A855F7]/50 border border-[#222] shadow-2xl transition-all backdrop-blur-xl">
              <div class="flex items-center px-4 bg-[#111] rounded-xl border border-transparent">
                <input 
                  v-model="newMessage" 
                  @keydown.enter.prevent="sendMessage"
                  type="text" 
                  class="flex-1 bg-transparent border-none focus:ring-0 text-white placeholder-[#888] py-5 text-[15px] tracking-tight font-medium" 
                  placeholder="Type a message..."
                >
                <button 
                  @click="sendMessage"
                  :disabled="!newMessage.trim() || sending"
                  class="bg-white hover:bg-gray-200 text-black p-3.5 rounded-xl disabled:opacity-30 disabled:hover:bg-white shadow-lg transition-all"
                >
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </button>
              </div>
            </div>
            <div class="mt-6 flex items-center justify-center space-x-4 opacity-30">
               <div class="h-px w-24 bg-gradient-to-r from-transparent to-[#A1A1AA]"></div>
               <span class="text-[10px] font-bold uppercase tracking-[0.2em] text-[#A1A1AA]">Administrator Terminal</span>
               <div class="h-px w-24 bg-gradient-to-l from-transparent to-[#A1A1AA]"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="flex-1 flex items-center justify-center bg-transparent">
        <div class="text-center group">
          <div class="w-20 h-20 rounded-[28px] bg-[#111] border border-[#222] flex items-center justify-center mx-auto mb-8 shadow-2xl relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-[#A855F7]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            <div class="w-6 h-6 bg-[#333] rounded-lg group-hover:bg-[#A855F7] transition-colors duration-500 shadow-inner relative z-10"></div>
          </div>
          <h2 class="text-3xl font-semibold tracking-tight text-white mb-4">Select a stream</h2>
          <p class="text-[15px] text-[#A1A1AA] font-medium max-w-[280px] mx-auto leading-relaxed">Select a conversation from the sidebar to view messages.</p>
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
