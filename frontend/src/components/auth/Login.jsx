import React, { useState, useContext } from 'react';
import { AuthContext } from './authContext';   // import context here 
                                                

const LoginForm = () => {

    const { login } = useContext(AuthContext);   // destructure the login function
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        login(username,password);  // instead of axios, use the login function from context
        setUsername('');
        setPassword('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Username:
                <input 
                    type="text" 
                    value={username} 
                    onChange={event => setUsername(event.target.value)}
                    required 
                />
            </label>
            <label>
                Password:
                <input 
                    type="password" 
                    value={password} 
                    onChange={event => setPassword(event.target.value)}
                    required 
                />
            </label>
            <button type="submit">Log in</button>
        </form>
    );
};

export default LoginForm;