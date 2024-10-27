import axios from "axios";

export default function DownloadListCSV() {
  const userDownloadApiUrl = "http://localhost:8000/download_results";
  const userId = localStorage.getItem("user_id");
  const username = localStorage.getItem("username");

  const dowloadList = async () => {
    try {
      const response = await axios.get(
        `${userDownloadApiUrl}?user_id=${userId}`
      );
      const url = window.URL.createObjectURL(new Blob([response.data]));

      // Crée un lien temporaire et clique dessus pour déclencher le téléchargement
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", `results ${username}.csv`);
      document.body.appendChild(link);
      link.click();

      // Nettoyage : supprime le lien après le téléchargement
      document.body.removeChild(link);
    } catch (err: unknown) {
      console.log(err);
    }
  };
  console.log();

  return (
    <button
      onClick={dowloadList}
      className="w-full mt-2 grid-cols-none lg:hover:bg-blue-600"
    >
      Télécharger
    </button>
  );
}
