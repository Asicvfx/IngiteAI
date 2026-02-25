export default defineNuxtRouteMiddleware(async (to, from) => {
    const auth = useAuthStore();

    // Public pages that don't require authentication
    const publicPages = ['/', '/login', '/register', '/auth/callback', '/landing', '/pricing'];
    const isPublic = publicPages.some(page => to.path === page) || to.path.startsWith('/auth/');

    if (import.meta.server) {
        const cookie = useCookie('auth_logged_in');
        // Logged-in user on landing → redirect to overview
        if (to.path === '/' && cookie.value) {
            return navigateTo('/overview');
        }
        if (!isPublic && !cookie.value) {
            return navigateTo('/login');
        }
        return;
    }

    // Client: restore token from localStorage
    if (!auth.isAuthenticated) {
        await auth.initialize();
    }

    // Logged-in user on landing → redirect to overview
    if (auth.isAuthenticated && to.path === '/') {
        return navigateTo('/overview');
    }

    if (!isPublic && !auth.isAuthenticated) {
        return navigateTo('/login');
    }

    if (auth.isAuthenticated && (to.path === '/login' || to.path === '/register')) {
        return navigateTo('/overview');
    }

    // Onboarding: redirect to /welcome if not completed (skip if already on /welcome)
    if (auth.isAuthenticated && auth.user && to.path !== '/welcome' && auth.user.has_completed_onboarding === false) {
        return navigateTo('/welcome');
    }
});
