import { defineStore } from 'pinia';

const formatAuthError = (error: any, fallback: string) => {
    if (error?.response?._data) {
        if (typeof error.response._data === 'object') {
            return Object.values(error.response._data).flat().join(' | ');
        }
        return String(error.response._data);
    }

    if (error?.data) {
        if (typeof error.data === 'object') {
            return Object.values(error.data).flat().join(' | ');
        }
        return String(error.data);
    }

    if (error?.message?.includes('Failed to fetch')) {
        return 'Network or CORS error: backend did not respond to the browser request.';
    }

    return error?.message || fallback;
};

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
                throw new Error(formatAuthError(error, 'Registration failed'));
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
                throw new Error(formatAuthError(error, 'Login failed'));
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
                throw new Error(formatAuthError(error, 'Google login failed'));
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
                throw new Error(formatAuthError(error, 'Google login with code failed'));
            }
        },
        setToken(token: string) {
            this.token = token;
            this.isAuthenticated = !!token;
            if (process.client) {
                localStorage.setItem('auth_token', token);
                document.cookie = 'auth_logged_in=1; path=/; max-age=31536000; SameSite=Lax';
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
                document.cookie = 'auth_logged_in=; path=/; max-age=0';
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
        async initialize() {
            if (process.client) {
                const token = localStorage.getItem('auth_token');
                if (token) {
                    this.setToken(token);
                    await this.fetchUser();
                }
            }
        },
    },
});
