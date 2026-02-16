<template>
  <div class="flex h-[calc(100vh-56px)] bg-black text-white overflow-hidden font-sans relative">
    <!-- Sidebar / Chat List (Ultra Minimal) -->
    <div class="w-80 border-r border-[#1A1A1A] bg-black flex flex-col z-20 overflow-hidden">
      <div class="p-8 border-b border-[#1A1A1A]">
        <h2 class="text-xl font-semibold tracking-[-0.022em]">Active Streams</h2>
        <p class="text-[12px] text-[#6B7280] mt-1">Live customer synchronization</p>
      </div>
      
      <div class="flex-1 overflow-y-auto px-2 py-4 space-y-1 custom-scrollbar">
        <div 
          v-for="chat in chats" 
          :key="chat.id" 
          @click="selectChat(chat)" 
          class="group p-4 rounded-xl cursor-pointer transition-colors duration-150 border border-transparent"
          :class="selectedChat?.id === chat.id ? 'bg-white/5 border-white/10' : 'hover:bg-white/[0.02]'"
        >
          <div class="flex items-center space-x-4">
            <div class="w-10 h-10 rounded-lg bg-[#1A1A1A] border border-[#262626] flex items-center justify-center text-[12px] font-medium text-[#9CA3AF]">
              {{ chat.telegram_chat_id ? chat.telegram_chat_id.toString().slice(-2) : '?' }}
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between mb-1">
                <span class="text-[13px] font-medium truncate text-white">#{{ chat.telegram_chat_id }}</span>
                <span v-if="chat.needs_human" class="w-1.5 h-1.5 bg-white rounded-full"></span>
              </div>
              <p class="text-[12px] text-[#6B7280] truncate font-normal">
                {{ chat.last_message?.content || 'Ready for uplink' }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Chat Area (Focus Mode) -->
    <div class="flex-1 flex flex-col relative z-10 bg-black">
      <div v-if="selectedChat" class="flex-1 flex flex-col h-full max-w-4xl mx-auto w-full">
        <!-- Header -->
        <header class="h-16 border-b border-[#1A1A1A] flex items-center px-10 justify-between">
          <div class="flex items-center space-x-3">
            <h3 class="text-[15px] font-medium tracking-tight text-white">Session #{{ selectedChat.telegram_chat_id }}</h3>
            <span class="text-[10px] text-[#4B5563] uppercase tracking-[0.1em] px-2 py-0.5 border border-[#1A1A1A] rounded">Uplink Stable</span>
          </div>
          <div class="text-[11px] text-[#6B7280] font-medium">
             {{ chats.length }} active nodes
          </div>
        </header>

        <!-- Messages Area (Clean Focus) -->
        <div ref="messageContainer" class="flex-1 overflow-y-auto px-10 py-12 space-y-8 custom-scrollbar scroll-smooth">
          <TransitionGroup name="fade">
          <div v-for="msg in messages" :key="msg.id" 
            class="flex flex-col group"
            :class="msg.sender === 'user' ? 'items-start' : 'items-end'"
          >
            <div class="max-w-[85%]" :class="msg.sender !== 'user' ? 'text-right' : 'text-left'">
              <div 
                class="px-5 py-3 rounded-xl relative transition-all duration-200"
                :class="[
                  msg.sender === 'user' 
                    ? 'bg-black border border-[#1A1A1A] text-[#E5E7EB]' 
                    : 'bg-white text-black font-medium'
                ]"
              >
                <p class="text-[14px] leading-relaxed">{{ msg.content }}</p>

                <!-- Product Mini-Cards -->
                <div v-if="msg.metadata?.products?.length" class="mt-4 space-y-2">
                  <div v-for="product in msg.metadata.products" :key="product.name" 
                    class="p-3 bg-black border border-[#1A1A1A] rounded-lg flex items-center space-x-3 hover:border-white/20 transition-colors">
                    <img v-if="product.image_url" :src="product.image_url" class="w-10 h-10 rounded-md object-cover bg-[#0D0D0D]">
                    <div class="flex-1 text-left">
                      <h4 class="text-[12px] font-medium text-white">{{ product.name }}</h4>
                      <p class="text-[11px] text-[#6B7280]">{{ product.price }}</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Quick Replies -->
              <div v-if="msg.metadata?.quick_replies?.length" class="mt-4 flex flex-wrap gap-2" :class="msg.sender !== 'user' ? 'justify-end' : 'justify-start'">
                <button 
                  v-for="reply in msg.metadata.quick_replies" 
                  :key="reply"
                  @click="sendQuickReply(reply)"
                  class="px-3 py-1.5 rounded-lg border border-[#1A1A1A] text-[11px] font-medium text-[#9CA3AF] hover:border-white/30 hover:text-white transition-all"
                >
                  {{ reply }}
                </button>
              </div>

              <div class="mt-2 text-[10px] text-[#4B5563] font-medium uppercase tracking-[0.05em]">
                {{ formatTime(msg.created_at) }}
              </div>
            </div>
          </div>
          </TransitionGroup>
        </div>

        <!-- Input Area (Minimal bar) -->
        <div class="p-10">
          <div class="max-w-3xl mx-auto">
            <div class="relative flex items-center border border-[#1A1A1A] rounded-2xl bg-black focus-within:border-white/30 transition-all px-4">
              <input 
                v-model="newMessage" 
                @keydown.enter.prevent="sendMessage"
                type="text" 
                class="flex-1 bg-transparent border-none focus:ring-0 text-white placeholder-[#4B5563] py-4 text-[14px]" 
                placeholder="Type a message..."
              >
              <button 
                @click="sendMessage"
                :disabled="!newMessage.trim() || sending"
                class="text-white opacity-40 hover:opacity-100 disabled:opacity-10 transition-opacity p-2"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
              </button>
            </div>
            <div class="mt-3 text-[10px] text-[#262626] font-medium uppercase tracking-[0.15em] text-center">
               Direct Admin Override • Local Channel
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="flex-1 flex items-center justify-center bg-black">
        <div class="text-center">
          <div class="w-12 h-12 rounded-lg bg-[#1A1A1A] flex items-center justify-center mx-auto mb-6">
            <div class="w-4 h-4 bg-[#262626] rounded-sm"></div>
          </div>
          <h2 class="text-xl font-medium tracking-tight text-white mb-2">Select a stream</h2>
          <p class="text-[13px] text-[#4B5563] max-w-[200px] mx-auto">Select a node from the sidebar to begin oversight.</p>
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
.fade-enter-active {
  transition: all 0.3s ease-out;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
</style>
