import React, { useState } from "react";
import axios from 'axios';
import { Form, Button, Col, Container, Row } from 'react-bootstrap';



function CreateTask() {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const createTask = async (title, description,) => {
        try {
            const response = await axios.post(
                'http://0.0.0.0:5000/tasks/',
                {
                    title: title,
                    description: description,
                }
            );
            console.log(response.data);
        } catch (error) {
            console.error("There was an error!", error);
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        createTask(title, description,);
    }

    return (
        <Container>
            <Row className="justify-content-md-center">
                <Col md="6">
                    <Form onSubmit={handleSubmit}>
                        <Form.Group controlId="formTitle">
                            <Form.Label>Название задачи:</Form.Label>
                            <Form.Control type="text" placeholder="Введите заглавие" value={title} onChange={e => setTitle(e.target.value)} />
                        </Form.Group>

                        <Form.Group controlId="formContent">
                            <Form.Label>description</Form.Label>
                            <Form.Control as="textarea" rows={3} value={description} onChange={e => setDescription(e.target.value)} />
                        </Form.Group>

                        
                        <Button variant="primary" type="submit">
                            Отправить POST запрос
                        </Button>
                    </Form>
                </Col>
            </Row>        
        </Container>
    );
}

export default CreateTask;