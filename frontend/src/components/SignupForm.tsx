import axios from "axios";
import { useState } from "react";
import Form from "./Form";

export default function SignUpForm() {
  const [username, setUsername] = useState<string>();
  const createUserApiUrl = "http://localhost:8000/create_user/";

  const handleCreateUser = async () => {
    try {
      const { data } = await axios.post(createUserApiUrl, {
        username: username,
      });
      console.log(data);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <Form
      title="Créer un pseudo"
      username={username as string}
      setUsername={setUsername}
      handler={handleCreateUser}
      buttonText="Soumettre"
    />
  );
}
