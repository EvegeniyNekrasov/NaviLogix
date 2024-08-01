
interface User {
  id: number;
  name: string;
  age: number;
}

export async function getUsuarios() {
  const res = await fetch(`http://localhost:6969`);
  const data = await res.json();
  return data;
}

export default async function Home() {
  const users = await getUsuarios();
  return (
    <div>
      <h1>Data from API:</h1>
      {users.map((user: User) => (
        <div key={user.id}>
          <h2>{user.name}</h2>
          <p>{user.age}</p>
        </div>
      ))}
    </div>
  );
}
