import React from 'react';
import Sidebar from './components/Sidebar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ListTask from './components/tasks/ListTask';
import CreateTask from './components/tasks/CreateTask';
import {AuthProvider} from './components/auth/authContext';
import LoginForm from './components/auth/LoginForm';
import Profile from './components/auth/Profile';

function App() {
  return (
    <div> 
   <Router>
   <AuthProvider>
   <Sidebar />
       <Routes>
         <Route path="tasks/" element={<ListTask/>} />
         <Route path="create_task/" element={<CreateTask/>}/>
         <Route path="login/" element={<LoginForm/>}/>
         <Route path="profile/" element={<Profile/>}/>
       </Routes>
       </AuthProvider>
   </Router>
</div>
);
};


export default App;