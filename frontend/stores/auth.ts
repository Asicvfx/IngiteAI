import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null as any,
        token: null as string | null,
        isAuthenticated: false,
    }),
    actions: {
        async login(credentials: any) {
            try {
                const data = await $fetch<any>('http://localhost:8000/api/v1/auth/login/', {
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
        async googleLogin(token: string) {
            try {
                const data = await $fetch<any>('http://localhost:8000/api/v1/auth/google/', {
                    method: 'POST',
                    body: {
                        access_token: token,
                    },
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
            try {
                const data = await $fetch('http://localhost:8000/api/v1/auth/user/', {
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
