import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null as any,
        token: null as string | null,
        isAuthenticated: false,
    }),
    actions: {
        async register(userData: any) {
            const config = useRuntimeConfig();
            try {
                await $fetch(`${config.public.apiBaseUrl}/api/v1/auth/registration/`, {
                    method: 'POST',
                    body: userData,
                });
                return true;
            } catch (error) {
                console.error('Registration failed', error);
                throw error;
            }
        },
        async login(credentials: any) {
            const config = useRuntimeConfig();
            try {
                const data = await $fetch<any>(`${config.public.apiBaseUrl}/api/v1/auth/login/`, {
                    method: 'POST',
                    body: credentials,
                });
                // Handle both JWT (access) and Token (key) formats
                const token = data.access || data.key;
                this.setToken(token);
                if (data.user) {
                    this.setUser(data.user);
                } else {
                    await this.fetchUser();
                }
                return true;
            } catch (error) {
                console.error('Login failed', error);
                throw error;
            }
        },
        async googleLogin(token: string, tokenType: 'id_token' | 'access_token' = 'id_token') {
            const config = useRuntimeConfig();
            try {
                // Build the request body based on the token type received
                const body: Record<string, string> = {};
                if (tokenType === 'id_token') {
                    body.id_token = token;
                } else {
                    body.access_token = token;
                }
                const data = await $fetch<any>(`${config.public.apiBaseUrl}/api/v1/auth/google/`, {
                    method: 'POST',
                    body,
                });
                const responseToken = data.access || data.key;
                this.setToken(responseToken);
                if (data.user) {
                    this.setUser(data.user);
                } else {
                    await this.fetchUser();
                }
                return true;
            } catch (error) {
                console.error('Google Login failed', error);
                throw error;
            }
        },
        async googleLoginWithCode(code: string, redirectUri: string) {
            const config = useRuntimeConfig();
            try {
                const data = await $fetch<any>(`${config.public.apiBaseUrl}/api/v1/auth/google/`, {
                    method: 'POST',
                    body: { code, redirect_uri: redirectUri },
                });
                const responseToken = data.access || data.key;
                this.setToken(responseToken);
                if (data.user) {
                    this.setUser(data.user);
                } else {
                    await this.fetchUser();
                }
                return true;
            } catch (error) {
                console.error('Google Login with code failed', error);
                throw error;
            }
        },
        setToken(token: string) {
            this.token = token;
            this.isAuthenticated = !!token;
            if (process.client) {
                localStorage.setItem('auth_token', token);
            }
        },
        setUser(user: any) {
            this.user = user;
        },
        logout() {
            this.token = null;
            this.user = null;
            this.isAuthenticated = false;
            if (process.client) {
                localStorage.removeItem('auth_token');
            }
        },
        async fetchUser() {
            if (!this.token) return;
            const config = useRuntimeConfig();
            try {
                const data = await $fetch(`${config.public.apiBaseUrl}/api/v1/auth/user/`, {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    },
                });
                this.setUser(data);
            } catch (error) {
                console.error('Failed to fetch user', error);
                this.logout();
            }
        },
        initialize() {
            if (process.client) {
                const token = localStorage.getItem('auth_token');
                if (token) {
                    this.setToken(token);
                    this.fetchUser();
                }
            }
        },
    },
});
