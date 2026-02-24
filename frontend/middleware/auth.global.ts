export default defineNuxtRouteMiddleware(async (to, from) => {
    // Skip auth check on server (no localStorage on SSR)
    if (import.meta.server) return;

    const auth = useAuthStore();

    // Restore token from localStorage and wait for user data
    if (!auth.isAuthenticated) {
        await auth.initialize();
    }

    // Public pages that don't require authentication
    const publicPages = ['/login', '/register', '/auth/callback', '/landing'];
    const isPublic = publicPages.some(page => to.path.startsWith(page));

    if (!isPublic && !auth.isAuthenticated) {
        return navigateTo('/login');
    }

    if (auth.isAuthenticated && (to.path === '/login' || to.path === '/register')) {
        return navigateTo('/');
    }
});
