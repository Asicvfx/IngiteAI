export default defineNuxtRouteMiddleware((to, from) => {
    const auth = useAuthStore();

    // Restore token from localStorage on every navigation (fixes logout on refresh)
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
