import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    const login = async (username, password) => {

        const authData = {
            username: username,
            password: password,
        };
       await axios.post('http://127.0.0.1:8000/api/login/', authData)   // use axios here
            .then(response => {
                console.log(response);
                localStorage.setItem('token', response.data.token);
                setUser({
                    id: response.data.user_id,
                    email: response.data.email,
                    username: response.data.username,
                    token: response.data.token,
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
        } else {
            localStorage.removeItem('user');
        }
    }, [user]);

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export default AuthProvider;