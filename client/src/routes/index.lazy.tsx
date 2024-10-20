import { useQuery } from "@tanstack/react-query";
import { createLazyFileRoute } from "@tanstack/react-router";

export const Route = createLazyFileRoute("/")({
    component: Index,
});

const getPorts = async () => {
    try {
        const request = await fetch("http://127.0.0.1:8000/ports");
        if (!request.ok) throw new Error("nop...");
        return await request.json();
    } catch (err) {
        console.error(err);
    }
};

function Index() {
    const { data, isLoading, isError } = useQuery({
        queryKey: ["ports"],
        queryFn: getPorts,
    });

    if (isLoading) return <span>Loading...</span>;
    if (isError) return <span>Oooopss... fix this error</span>;

    console.log(data);

    return (
        <div>
            {data.map((item) => (
                <ul key={item.id}>
                    <li
                        style={{
                            display: "flex",
                            flexDirection: "column",
                            gap: "10px",
                            padding: "10px",
                            background: "#c2c2c2",
                        }}>
                        <span>{item.code}</span>
                        <span>{item.country}</span>
                        <span>{item.name}</span>
                        <span>{item.timezone}</span>
                    </li>
                </ul>
            ))}
        </div>
    );
}
