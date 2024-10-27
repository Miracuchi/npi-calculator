import { useEffect, useState } from "react";
import "./App.css";
import Calculator from "./components/Calculator";
import LoginForm from "./components/LoginForm";
import SignUpForm from "./components/SignupForm";
import "./index.css";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Vérifiez si le token ou l'ID est présent
    const token = localStorage.getItem("token"); // ou sessionStorage
    const userId = localStorage.getItem("user_id"); // ou sessionStorage

    // Si le token et l'ID sont présents, l'utilisateur est authentifié
    if (token && userId) {
      setIsAuthenticated(true);
    }
  }, []);

  return (
    <div className="lg:flex">
      {isAuthenticated ? (
        <Calculator />
      ) : (
        <div className="flex gap-3">
          <LoginForm /> <SignUpForm />
        </div>
      )}
    </div>
  );
}

export default App;
