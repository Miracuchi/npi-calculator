import axios from "axios";
import { useState } from "react";
import DownloadListCSV from "./Download";
import LogoutButton from "./LogoutButton";

export default function Calculator() {
  const [expression, setExpression] = useState<string>("");
  const [result, setResult] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [currentInput, setCurrentInput] = useState<string>("");
  const isOnlyZero = /^0+/;
  const userId = localStorage.getItem("user_id");
  const calculateApiUrl = "http://localhost:8000/calculate";

  const handleButtonClick = (value: string) => {
    setCurrentInput((prev) => prev + value);
  };

  const handleSubmit = () => {
    if (currentInput.trim()) {
      setExpression((prev) => prev + (prev ? " " : "") + currentInput.trim());
      setCurrentInput("");
    }
    if (currentInput.match(isOnlyZero)) setExpression("0");
  };

  const postCalculate = async () => {
    setError(null);
    try {
      const { data } = await axios.post(calculateApiUrl, {
        user: { id: userId },
        operation: { expression: expression.trim() },
      });

      setResult(data);
    } catch (err: unknown) {
      if (axios.isAxiosError(err)) {
        console.error("Error Message:", err.message);
        setError(err.message);
      } else {
        console.error("Unexpected Error:", err);
        setError("Une erreur inattendue est survenue.");
      }
    }
  };

  const clearExpression = () => {
    setExpression("");
    setResult(null);
    setError(null);
    setCurrentInput("");
  };

  return (
    <>
      <div>
        <div className="grid grid-rows-1 mb-3">
          <div className="">
            <div className=" h-24 border border-gray-300 p-2 mb-2 bg-black font-calculator text-xl">
              <div className=" h-[70%]">
                <div className="flex-wrap overflow-auto text-left pl-2">
                  {currentInput || "--"}
                </div>
                <div className="flex-wrap overflow-auto text-left pl-2">
                  {expression || "--"}
                </div>
              </div>
              <div className="h-[30%]">
                {result !== null && <div className="result">{result}</div>}
                {error && <div className="error">Erreur: {error}</div>}
              </div>
            </div>
          </div>
        </div>
        <div className="buttons grid grid-cols-3 gap-2">
          {[1, 2, 3, 4, 5, 6, 7, 8, 9, "."].map((number, i) => (
            <button
              key={i}
              onClick={() => handleButtonClick(number.toString())}
            >
              {number}
            </button>
          ))}
          <button className="buttons" onClick={() => handleButtonClick("0")}>
            0
          </button>

          {["+", "-", "*", "/"].map((button) => (
            <button
              key={button}
              onClick={() => handleButtonClick(button)}
              onMouseDown={handleSubmit}
            >
              {button}
            </button>
          ))}
          <button onClick={handleSubmit} className="text-center">
            Ajouter
          </button>
          <button onClick={postCalculate} className="calculate-button">
            =
          </button>
          <button onClick={clearExpression} className="clear-button">
            C
          </button>
        </div>

        <DownloadListCSV />

        <LogoutButton />
      </div>
    </>
  );
}
