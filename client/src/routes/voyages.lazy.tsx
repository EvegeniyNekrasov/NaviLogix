import GenericTable from "@/components/Table";
import { useQuery } from "@tanstack/react-query";
import { createLazyFileRoute } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createLazyFileRoute("/voyages")({
    component: Voyages,
});

const getData = async () => {
    try {
        const req = await fetch("http://127.0.0.1:8000/voyages");
        if (!req.ok) throw new Error("some error");
        return await req.json();
    } catch (err) {
        console.error(err);
    }
};

interface Voyages {
    id: number;
    vessel_id: number;
    route_id: number;
    departure_date: string;
    arrival_date: string;
    status: string;
}

function Voyages() {
    const { isError, isLoading, data } = useQuery({
        queryKey: ["voyages"],
        queryFn: getData,
    });

    if (isLoading) return <div>Loading...</div>;
    if (isError) return <div>Error...</div>;

    return (
        <div className="flex flex-col gap-5">
            <GenericTable<Voyages> data={data} />
        </div>
    );
}
