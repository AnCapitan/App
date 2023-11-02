import React, { useState } from "react";
import axios from "axios";

export function GetRequest() {
  const [responseData, setResponseData] = useState(null);

  const sendGetRequest = async () => {
    try {
      const response = await axios.get('http://0.0.0.0:5000/users/');
      setResponseData(response.data);
    } catch (error) {
      console.error("Ошибка при выполнении GET-запроса:", error);
    }
  };

  return (
    <div>
      <button onClick={sendGetRequest}>Отправить GET-запрос</button>
      {responseData && <div>Ответ: {JSON.stringify(responseData)}</div>}
    </div>
  );
}

export default GetRequest;