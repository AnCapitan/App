import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

function MeNavbar() {
  return (
    <>
    <Navbar bg="dark" data-bs-theme="dark">
      <Container>
        <Navbar.Brand href="/">Just</Navbar.Brand>
        <Nav className="me-auto">
            <Nav.Link href="/todo/profile">Профиль</Nav.Link>
            <Nav.Link href="/todo/tasks">Задачи</Nav.Link>
            <Nav.Link href="/todo/timetable">Расписание</Nav.Link>
            <Nav.Link href="/todo/contacts">Контакты</Nav.Link>
        </Nav>
        <Navbar.Collapse className="justify-content-end">
          <Navbar.Text>
            Signed in as: <a href="#login">Admin</a>
          </Navbar.Text>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    </>
  );
}

export default MeNavbar;
