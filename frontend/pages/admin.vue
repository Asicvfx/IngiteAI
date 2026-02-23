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
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl p-8 hover:border-[#A855F7]/30 transition-colors">
            <p class="text-[#666] text-xs uppercase tracking-widest font-bold mb-3">Total Users</p>
            <p class="text-4xl font-bold text-white">{{ stats.total_users }}</p>
          </div>
          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl p-8 hover:border-green-500/30 transition-colors">
            <p class="text-[#666] text-xs uppercase tracking-widest font-bold mb-3">New Today</p>
            <p class="text-4xl font-bold text-green-400">+{{ stats.new_today }}</p>
          </div>
          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl p-8 hover:border-blue-500/30 transition-colors">
            <p class="text-[#666] text-xs uppercase tracking-widest font-bold mb-3">New This Week</p>
            <p class="text-4xl font-bold text-blue-400">+{{ stats.new_this_week }}</p>
          </div>
        </div>

        <!-- Users Table -->
        <section>
          <div class="flex items-center space-x-3 px-2 border-l-2 border-[#A855F7] mb-6">
            <h2 class="text-[11px] font-bold text-[#A1A1AA] uppercase tracking-[0.2em]">All Users</h2>
          </div>

          <div class="bg-[#050505]/80 border border-[#222] rounded-2xl overflow-hidden">
            <table class="w-full text-left">
              <thead>
                <tr class="border-b border-[#222]">
                  <th class="px-6 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Username</th>
                  <th class="px-6 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Email</th>
                  <th class="px-6 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold hidden md:table-cell">Joined</th>
                  <th class="px-6 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold hidden md:table-cell">Last Login</th>
                  <th class="px-6 py-4 text-[11px] text-[#666] uppercase tracking-widest font-bold">Role</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in stats.users" :key="user.id"
                    class="border-b border-[#111] hover:bg-[#A855F7]/5 transition-colors">
                  <td class="px-6 py-4">
                    <span class="text-white font-medium text-sm">{{ user.username }}</span>
                  </td>
                  <td class="px-6 py-4">
                    <span class="text-[#A1A1AA] text-sm">{{ user.email || '—' }}</span>
                  </td>
                  <td class="px-6 py-4 hidden md:table-cell">
                    <span class="text-[#666] text-sm">{{ formatDate(user.date_joined) }}</span>
                  </td>
                  <td class="px-6 py-4 hidden md:table-cell">
                    <span class="text-[#666] text-sm">{{ formatDate(user.last_login) }}</span>
                  </td>
                  <td class="px-6 py-4">
                    <span v-if="user.is_superuser" class="bg-[#A855F7]/20 text-[#A855F7] text-[10px] font-bold uppercase tracking-wider px-2 py-1 rounded">Admin</span>
                    <span v-else class="bg-[#222] text-[#666] text-[10px] font-bold uppercase tracking-wider px-2 py-1 rounded">User</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '~/stores/auth';

const auth = useAuthStore();
const config = useRuntimeConfig();

const loading = ref(true);
const error = ref('');
const stats = ref({
  total_users: 0,
  new_today: 0,
  new_this_week: 0,
  users: [] as any[],
});

const formatDate = (dateStr: string | null) => {
  if (!dateStr) return '—';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
};

onMounted(async () => {
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
});
</script>
