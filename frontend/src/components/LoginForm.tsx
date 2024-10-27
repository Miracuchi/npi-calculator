import axios from "axios";
import { useState } from "react";
import Form from "./Form";

export default function LoginForm() {
  const [username, setUsername] = useState<string>();
  const loginApiUrl = "http://localhost:8000/login/";

  const handleLogin = async () => {
    try {
      const response = await axios.post(
        loginApiUrl,
        {
          username: username,
        },
        { withCredentials: true }
      );
      localStorage.setItem("user_id", response.data.id);
      localStorage.setItem("token", response.data.token);
      localStorage.setItem("username", response.data.username);
      window.location.href = "/";
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <Form
      title="Se connecter"
      username={username as string}
      setUsername={setUsername}
      handler={handleLogin}
      buttonText="Connecter"
    />
  );
}
