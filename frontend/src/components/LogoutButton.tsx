export default function LogoutButton() {
  const handleLogout = () => {
    localStorage.clear();
    window.location.href = "/";
  };
  return (
    <button onClick={handleLogout} className="mt-2 lg:hover:bg-red-600">
      Se déconnecter
    </button>
  );
}
