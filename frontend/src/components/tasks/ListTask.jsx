import axios from "axios";
import React, { useState, useEffect } from "react";

function ListTask() {
  const [tasks, setResponse] = useState([]);

  useEffect(() => {
    axios
      .get("http://0.0.0.0:5000/tasks/")
      .then((resp) => {
        const Tasks = resp.data;
        setResponse(Tasks);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  const Task = ({ task }) => (
    <div key={task.id} className="card mt-3" style={{width: "18rem;"}}>
      <div className="card-header">Номер задачи '{task.id}'</div>
      <div className="card-body">
        <h5 className="card-title">{task.title}</h5>
        <p className="card-text">{task.description}</p>
        <a href={`tasks/${task.id}`} className="btn btn-primary">Посмотреть подробнее</a>
      </div>
    </div>
  );

  return (
    <div className="container">
      <div className="row">
        {tasks.map((task) => {
          return (
            <div className="col-md-6" key={task.id}>
              <Task task={task} />
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default ListTask;