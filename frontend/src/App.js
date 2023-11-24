import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import {AuthProvider} from './components/auth/authContext';
import MeNavbar from './components/Navbar';
import LoginForm from './components/auth/LoginForm';
import Profile from './components/auth/Profile';
import Task from './components/todo/Task';
import MeFooter from './components/Footer';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <MeNavbar />
        <div id="content">
          <Routes>
            <Route path='todo/profile/' element={<Profile />} />
            <Route path="todo/tasks/" element={<Task />} />
            <Route path="login/" element={<LoginForm />} />
            <Route path="profile/" element={<Profile />} />
          </Routes>
        </div>
        <MeFooter />
      </Router>
    </AuthProvider>
  );
};

export default App;