export default defineNuxtRouteMiddleware((to, from) => {
    // Skip auth check on server (no localStorage on SSR)
    if (import.meta.server) return;

    const auth = useAuthStore();

    // Restore token from localStorage
    auth.initialize();

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
