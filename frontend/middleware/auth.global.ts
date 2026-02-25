export default defineNuxtRouteMiddleware(async (to, from) => {
    const auth = useAuthStore();

    // Public pages that don't require authentication
    const publicPages = ['/', '/login', '/register', '/auth/callback', '/landing', '/pricing'];
    const isPublic = publicPages.some(page => to.path === page) || to.path.startsWith('/auth/');

    if (import.meta.server) {
        // SSR: check cookie to know if user was logged in
        const cookie = useCookie('auth_logged_in');
        if (!isPublic && !cookie.value) {
            return navigateTo('/login');
        }
        return;
    }

    // Client: restore token from localStorage
    if (!auth.isAuthenticated) {
        await auth.initialize();
    }

    if (!isPublic && !auth.isAuthenticated) {
        return navigateTo('/login');
    }

    if (auth.isAuthenticated && (to.path === '/login' || to.path === '/register')) {
        return navigateTo('/home');
    }
});
