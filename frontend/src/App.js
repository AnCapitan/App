import React from 'react';
import Sidebar from './components/Sidebar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ListTask from './components/tasks/ListTask';
import CreateTask from './components/tasks/CreateTask';

function App() {
  return (
    <div> 
   <Router>
   <Sidebar />
       <Routes>
         <Route path="tasks/" element={<ListTask/>} />
         <Route path="create_task/" element={<CreateTask/>}/>
       </Routes>
   </Router>
</div>
);
};


export default App;