import Map from "@/components/Map";
import GenericTable from "@/components/Table";
import { useQuery } from "@tanstack/react-query";
import { createLazyFileRoute } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import { LatLngExpression } from "leaflet";

const getData = async () => {
    try {
        const req = await fetch("http://127.0.0.1:8000/ports");
        if (!req.ok) throw new Error("some error");
        return await req.json();
    } catch (err) {
        console.error(err);
    }
};

interface Ports {
    id: number;
    name: string;
    code: string;
    latitude: number;
    longitude: number;
    timezone: string;
}

export const Route = createLazyFileRoute("/ports")({
    component: Ports,
});

function Ports() {
    const { isError, isLoading, data } = useQuery({
        queryKey: ["ports"],
        queryFn: getData,
    });

    const [ports, setPorts] = useState<undefined | Ports[]>(undefined);
    const [position, setPosition] = useState<LatLngExpression>([0, 0]);

    useEffect(() => {
        if (data && data.length > 0) {
            const lat = data[0].latitude;
            const lng = data[0].longitude;

            setPorts(data);
            setPosition([lat, lng]);
        }
    }, [data]);

    return (
        <div className="p-4">
            {ports ? (
                <div className="flex flex-col gap-3">
                    <GenericTable<Ports> data={ports} />
                    {position && (
                        <div className="bg-white-700 mx-auto my-5 w-[98%] h-[480px]">
                            <Map positions={position} />
                        </div>
                    )}
                </div>
            ) : null}
            {isLoading && <div>lodaing...</div>}
            {isError && <div>error...</div>}
        </div>
    );
}
