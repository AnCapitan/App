import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

// Не забудьте подключить ваш CSS файл, со стилями написанными выше
import '../App.css'; // Это предполагаемое название файла со стилями

// Импорты для компонентов React Bootstrap остаются прежними

function MeFooter() {
  const year = new Date().getFullYear(); // Динамический год для подвала

  return (
    <div id="footer">
      <Navbar bg="dark" variant="dark" className="mt-5">
        <Container>
          <Nav className="me-auto">
            <Nav.Link href="/todo/about">О нас</Nav.Link>
            <Nav.Link href="/todo/services">Услуги</Nav.Link>
            <Nav.Link href="/todo/partners">Партнеры</Nav.Link>
            <Nav.Link href="/todo/careers">Карьера</Nav.Link>
          </Nav>
          <Navbar.Collapse className="justify-content-end">
            <Navbar.Text>
              © {year} Just, All Rights Reserved
            </Navbar.Text>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
}

export default MeFooter;
