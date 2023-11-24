import axios from "axios";
import React, { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

function ListTasks() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios
      .get("http://0.0.0.0:8000/tasks/")
      .then((resp) => {
        setTasks(resp.data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  return (
    <div className="container mt-5">
      <table className="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Название</th>
            <th scope="col">Описание</th>
            <th scope="col">Действия</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map((task) => (
            <tr key={task.id}>
              <th scope="row">{task.id}</th>
              <td>{task.title}</td>
              <td>{task.description}</td>
              <td>
                <a href={`tasks/${task.id}`} className="btn btn-dark">
                  Посмотреть подробнее
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ListTasks;
