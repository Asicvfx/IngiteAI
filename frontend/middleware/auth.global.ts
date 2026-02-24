export default defineNuxtRouteMiddleware(async (to, from) => {
    const auth = useAuthStore();

    // On client, restore token from localStorage
    if (import.meta.client && !auth.isAuthenticated) {
        await auth.initialize();
    }

    // Public pages that don't require authentication
    const publicPages = ['/login', '/register', '/auth/callback', '/landing'];
    const isPublic = publicPages.some(page => to.path.startsWith(page));

    // Not authenticated → go to login (works on both SSR and client)
    if (!isPublic && !auth.isAuthenticated) {
        return navigateTo('/login');
    }

    // Already logged in → don't show login/register
    if (auth.isAuthenticated && (to.path === '/login' || to.path === '/register')) {
        return navigateTo('/');
    }
});
