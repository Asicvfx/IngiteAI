<template>
  <div class="px-6 md:px-12 py-16 min-h-[calc(100vh-56px)] text-white font-sans relative overflow-hidden">

    <div class="max-w-5xl mx-auto relative z-10 w-full">
      <div class="mb-14">
        <h1 class="text-4xl font-semibold tracking-[-0.04em] text-white">Admin Panel</h1>
        <p class="mt-4 text-[#A1A1AA] text-[15px] leading-relaxed font-medium">
          Monitor users, track registrations, and manage the platform.
        </p>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="flex items-center justify-center py-20">
        <div class="w-10 h-10 border-2 border-white/10 border-t-[#A855F7] rounded-full animate-spin"></div>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="text-center py-20">
        <p class="text-red-400 text-lg font-medium">{{ error }}</p>
        <p class="text-[#666] text-sm mt-2">Only superusers can access this page.</p>
      </div>

      <div v-else>
        <!-- Stats Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-5 mb-12">
          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl p-7 hover:border-[#A855F7]/30 transition-colors">
            <p class="text-[#666] text-xs uppercase tracking-widest font-bold mb-3">Total Users</p>
            <p class="text-3xl font-bold text-white">{{ stats.total_users }}</p>
          </div>
          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl p-7 hover:border-green-500/30 transition-colors">
            <p class="text-[#666] text-xs uppercase tracking-widest font-bold mb-3">Online Now</p>
            <p class="text-3xl font-bold text-green-400">{{ stats.online_count }}</p>
          </div>
          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl p-7 hover:border-emerald-500/30 transition-colors">
            <p class="text-[#666] text-xs uppercase tracking-widest font-bold mb-3">New Today</p>
            <p class="text-3xl font-bold text-emerald-400">+{{ stats.new_today }}</p>
          </div>
          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl p-7 hover:border-blue-500/30 transition-colors">
            <p class="text-[#666] text-xs uppercase tracking-widest font-bold mb-3">New This Week</p>
            <p class="text-3xl font-bold text-blue-400">+{{ stats.new_this_week }}</p>
          </div>
        </div>

        <!-- Users Table -->
        <section>
          <div class="flex items-center space-x-3 px-2 border-l-2 border-[#A855F7] mb-6">
            <h2 class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-[0.2em]">All Users</h2>
          </div>

          <!-- Action message -->
          <div v-if="actionMsg" class="mb-4 px-4 py-3 rounded-xl text-sm font-medium"
               :class="actionMsg.type === 'success' ? 'bg-green-500/10 text-green-400 border border-green-500/20' : 'bg-red-500/10 text-red-400 border border-red-500/20'">
            {{ actionMsg.text }}
          </div>

          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl overflow-hidden overflow-x-auto">
            <table class="w-full text-left min-w-[700px]">
              <thead>
                <tr class="border-b border-[#222]">
                  <th class="px-5 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Status</th>
                  <th class="px-5 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Username</th>
                  <th class="px-5 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Email</th>
                  <th class="px-5 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Joined</th>
                  <th class="px-5 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Role</th>
                  <th class="px-5 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in stats.users" :key="user.id"
                    class="border-b border-[#111] hover:bg-[#A855F7]/5 transition-colors">
                  <!-- Online Status -->
                  <td class="px-5 py-4">
                    <div class="flex items-center space-x-2">
                      <span class="w-2 h-2 rounded-full" :class="user.is_online ? 'bg-green-400 shadow-[0_0_6px_rgba(74,222,128,0.6)]' : 'bg-[#333]'"></span>
                      <span v-if="user.is_online" class="text-green-400 text-xs font-medium">{{ user.session_minutes }}m</span>
                      <span v-else class="text-[#444] text-xs">offline</span>
                    </div>
                  </td>
                  <td class="px-5 py-4">
                    <span class="text-white font-medium text-sm">{{ user.username }}</span>
                  </td>
                  <td class="px-5 py-4">
                    <span class="text-[#A1A1AA] text-sm">{{ user.email || '—' }}</span>
                  </td>
                  <td class="px-5 py-4">
                    <span class="text-[#666] text-sm">{{ formatDate(user.date_joined) }}</span>
                  </td>
                  <td class="px-5 py-4">
                    <span v-if="user.is_superuser" class="bg-[#A855F7]/20 text-[#A855F7] text-[10px] font-bold uppercase tracking-wider px-2 py-1 rounded">Admin</span>
                    <span v-else class="bg-[#222] text-[#666] text-[10px] font-bold uppercase tracking-wider px-2 py-1 rounded">User</span>
                  </td>
                  <td class="px-5 py-4">
                    <button v-if="!user.is_superuser"
                      @click="confirmDelete(user)"
                      :disabled="deleting === user.id"
                      class="text-[#666] hover:text-red-400 text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#222] hover:border-red-500/30 hover:bg-red-500/5 transition-all disabled:opacity-30"
                    >
                      <span v-if="deleting === user.id">...</span>
                      <span v-else>Delete</span>
                    </button>
                    <span v-else class="text-[#333] text-xs">—</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </div>

    </div>

    <!-- Delete Modal -->
    <Teleport to="body">
      <div v-if="deleteTarget" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4">
        <div class="bg-[#111] border border-[#333] rounded-2xl p-8 max-w-md w-full shadow-2xl">
          <h3 class="text-lg font-semibold text-white mb-3">Delete User?</h3>
          <p class="text-[#A1A1AA] text-sm mb-6">
            Are you sure you want to delete <strong class="text-white">{{ deleteTarget.username }}</strong> ({{ deleteTarget.email || 'no email' }})?
            This action cannot be undone.
          </p>
          <div class="flex space-x-3 justify-end">
            <button @click="deleteTarget = null" class="px-5 py-2.5 rounded-xl border border-[#333] text-[#A1A1AA] text-sm font-medium hover:bg-white/5 transition-colors">
              Cancel
            </button>
            <button @click="deleteUser(deleteTarget)" class="px-5 py-2.5 rounded-xl bg-red-500/20 border border-red-500/30 text-red-400 text-sm font-semibold hover:bg-red-500/30 transition-colors">
              Delete
            </button>
          </div>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '~/stores/auth';

const auth = useAuthStore();
const config = useRuntimeConfig();

const loading = ref(true);
const error = ref('');
const deleting = ref<number | null>(null);
const deleteTarget = ref<any>(null);
const actionMsg = ref<{ type: string; text: string } | null>(null);

const stats = ref({
  total_users: 0,
  new_today: 0,
  new_this_week: 0,
  online_count: 0,
  users: [] as any[],
});

const formatDate = (dateStr: string | null) => {
  if (!dateStr) return '—';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
};

const fetchStats = async () => {
  try {
    const data = await $fetch<any>(`${config.public.apiBaseUrl}/api/v1/dashboard/admin-stats/`, {
      headers: { Authorization: `Bearer ${auth.token}` },
    });
    stats.value = data;
  } catch (err: any) {
    error.value = err.response?._data?.detail || 'Access denied. Superuser required.';
  } finally {
    loading.value = false;
  }
};

const confirmDelete = (user: any) => {
  deleteTarget.value = user;
};

const deleteUser = async (user: any) => {
  deleteTarget.value = null;
  deleting.value = user.id;
  actionMsg.value = null;

  try {
    await $fetch(`${config.public.apiBaseUrl}/api/v1/dashboard/admin-stats/delete-user/${user.id}/`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${auth.token}` },
    });
    actionMsg.value = { type: 'success', text: `User "${user.username}" deleted.` };
    stats.value.users = stats.value.users.filter((u: any) => u.id !== user.id);
    stats.value.total_users--;
  } catch (err: any) {
    actionMsg.value = { type: 'error', text: err.response?._data?.error || 'Failed to delete user.' };
  } finally {
    deleting.value = null;
    setTimeout(() => { actionMsg.value = null; }, 5000);
  }
};

onMounted(fetchStats);
</script>
