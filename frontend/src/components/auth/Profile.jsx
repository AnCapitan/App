import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Profile = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        // Получение токена из локального хранилища
        const token = localStorage.getItem('token');
        
        if (token) {
          const config = {
            headers: {
              'Authorization': `Bearer ${token}` // Добавление токена в заголовок
            }
          };

          const response = await axios.get('http://0.0.0.0:5000/users/me', config);
          setUser(response.data);
          setLoading(false);
        } else {
          console.error('Токен не найден');
          setLoading(false);
        }
      } catch (error) {
        console.error('Ошибка при загрузке данных пользователя:', error);
        setLoading(false);
      }
    };

    fetchUserData();
  }, []);

  return (
    <div>
      {loading ? (
        <p>Загрузка данных...</p>
      ) : user ? (
        <div>
          <h1>Профиль пользователя</h1>
          <p>Имя: {user.username}</p>
          <p>Email: {user.email}</p>
        </div>
      ) : (
        <p>Не удалось загрузить данные пользователя.</p>
      )}
    </div>
  );
};

export default Profile;
