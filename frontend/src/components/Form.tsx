import { FormProps } from "../type";

export default function Form(formProps: FormProps) {
  const onSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault(); // Empêche le rechargement de la page
    formProps.handler(); // Appelle le gestionnaire passé en props
  };
  return (
    <div>
      <div className="text-lg mb-2">{formProps.title}</div>
      <form
        onSubmit={onSubmit}
        className="flex flex-col items-center space-y-4"
      >
        <input
          type="text"
          value={formProps.username}
          onChange={(e) => formProps.setUsername(e.target.value)}
          placeholder="Entrez votre nom d'utilisateur"
          className="border border-gray-300 rounded-lg p-2 w-64"
          required
        />
        <button
          type="submit"
          className=" text-white rounded-lg p-2 lg:hover:bg-green-600"
        >
          {formProps.buttonText}
        </button>
      </form>
    </div>
  );
}
