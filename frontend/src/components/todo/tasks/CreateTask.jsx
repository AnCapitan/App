import React, { useState } from "react";
import axios from 'axios';
import { Form, Button, Col, Container, Row, Card } from 'react-bootstrap';

function CreateTask() {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const createTask = async (title, description) => {
        try {
            const response = await axios.post(
                'http://0.0.0.0:8000/tasks/',
                { title, description }
            );
            console.log(response.data);
        } catch (error) {
            console.error("There was an error!", error);
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        createTask(title, description);
    }

    return (
        <Container>
            <Row className="justify-content-md-center">
                <Col md={6}>
                    <Card>
                        <Card.Body>
                            <Card.Title>Создание новой задачи</Card.Title>
                            <Form onSubmit={handleSubmit}>
                                <Form.Group className="mb-3" controlId="formTitle">
                                    <Form.Label>Название задачи:</Form.Label>
                                    <Form.Control type="text" placeholder="Введите заглавие" value={title} onChange={e => setTitle(e.target.value)} />
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="formContent">
                                    <Form.Label>Описание задачи</Form.Label>
                                    <Form.Control as="textarea" rows={3} placeholder="Опишите задачу" value={description} onChange={e => setDescription(e.target.value)} />
                                </Form.Group>

                                <Button variant="dark" type="submit">
                                    Создать задачу
                                </Button>
                            </Form>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>        
        </Container>
    );
}

export default CreateTask;
