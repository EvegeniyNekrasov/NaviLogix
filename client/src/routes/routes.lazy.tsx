import GenericTable from "@/components/Table";
import { useQuery } from "@tanstack/react-query";
import { createLazyFileRoute } from "@tanstack/react-router";

export const Route = createLazyFileRoute("/routes")({
    component: RoutesComponent,
});

const getData = async () => {
    try {
        const req = await fetch("http://127.0.0.1:8000/routes");
        if (!req.ok) throw new Error("some error");
        return await req.json();
    } catch (err) {
        console.error(err);
    }
};

interface Routes {
    id: number;
    name: string;
    origin_port_id: number;
    destination_port_id: number;
    distance: number;
}

function RoutesComponent() {
    const { isError, isLoading, data } = useQuery({
        queryKey: ["routes"],
        queryFn: getData,
    });

    if (isLoading) return <div>Loading...</div>;
    if (isError) return <div>Error...</div>;

    return (
        <div className="flex flex-col gap-5 p-6 ">
            <span>Total routes: {data.length}</span>
            <GenericTable<Routes> data={data} />
        </div>
    );
}
