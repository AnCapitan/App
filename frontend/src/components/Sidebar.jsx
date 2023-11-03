import React from 'react';
import { Nav, Card } from 'react-bootstrap';

const Sidebar = () => {
  return (
    <Card className="sidebar">
      <Card.Body>
        <Nav defaultActiveKey="/home" className="flex-column">
          <Nav.Link href="/home">Главная</Nav.Link>
          <Nav.Link href="/tasks">Задачи</Nav.Link>
          <Nav.Link href="/create_task">Создать задачу</Nav.Link>
          <Nav.Link href="/lk">Личный кабинет</Nav.Link>
        </Nav>
      </Card.Body>
    </Card>
  );
};

export default Sidebar;
