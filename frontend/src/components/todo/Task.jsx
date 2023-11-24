import React, { useState } from 'react';
import CreateTask from "./tasks/CreateTask";
import ListTask from './tasks/ListTasks';
import Button from 'react-bootstrap/Button';
import './task.css';

function ButtonCreateTask({ onToggleCreateTask, isCreating }) {
  const buttonVariant = isCreating ? "danger" : "dark";
  const buttonText = isCreating ? "Убрать форму" : "Показать форму";

  return (
    <div className="block-example-container"> 
      <Button 
        variant={buttonVariant} 
        onClick={onToggleCreateTask} 
        className="block-example-button"
      >
        {buttonText}
      </Button>
    </div>
  );
}

function ButtonShowTask({ onToggleTaskList, isShow }) {
  const buttonVariant = isShow ? "danger" : "dark";
  const buttonText = isShow ? "Спрятать задачи" : "Показать задачи"; 

  return (
    <div className="block-example-container"> 
      <Button 
        variant={buttonVariant} 
        onClick={onToggleTaskList} 
        className="block-example-button"
      >
        {buttonText}
      </Button>
    </div>
  );
}

function Task() {
  const [showCreateTask, setShowCreateTask] = useState(false);
  const [showListTasks, setShowListTasks] = useState(false);

  const handleToggleShowTasks = () => {
    setShowListTasks(prev => !prev);
  }

  const handleToggleCreateTask = () => {
    setShowCreateTask(prev => !prev);
  };

  return (
    <div>
      <ButtonCreateTask isCreating={showCreateTask} onToggleCreateTask={handleToggleCreateTask} />
      {showCreateTask && <CreateTask />}
      
      <ButtonShowTask isShow={showListTasks} onToggleTaskList={handleToggleShowTasks} />
      {showListTasks && <ListTask />}
    </div>
  );
}

export default Task;
