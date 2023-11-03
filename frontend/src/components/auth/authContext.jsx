import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    const login = async (username, password) => {
        const authData = new URLSearchParams();
        authData.append('username', username);
        authData.append('password', password);
        await axios.post('http://0.0.0.0:5000/token', authData)
            .then(response => {
                localStorage.setItem('token', response.data.access_token);
                localStorage.setItem('token_type', response.data.token_type);
                setUser({
                    token: response.data.access_token, // response.data.access_token, чтобы сохранить токен
                });
            })
            .catch(error => {
                console.log(error);
            });
    };

    // имитация выхода из системы
    const logout = () => {
        setUser(null);
    };

    useEffect(() => {
        const savedUser = localStorage.getItem('user');
        if (savedUser) {
            setUser(JSON.parse(savedUser));
        }
    }, []);

    useEffect(() => {
        if (user) {
            localStorage.setItem('user', JSON.stringify(user));
            localStorage.setItem('token', user.token);
            localStorage.setItem('token_type', 'bearer');
        } else {
            localStorage.removeItem('user');
            localStorage.removeItem('token');
            localStorage.removeItem('token_type');
        }
    }, [user]);

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export default AuthProvider;