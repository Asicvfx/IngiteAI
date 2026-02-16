export default defineNuxtRouteMiddleware((to, from) => {
    const auth = useAuthStore();

    // Public pages
    const publicPages = ['/login', '/register'];
    const authRequired = !publicPages.includes(to.path);

    if (authRequired && !auth.isAuthenticated) {
        return navigateTo('/login');
    }

    if (auth.isAuthenticated && publicPages.includes(to.path)) {
        return navigateTo('/');
    }
});
