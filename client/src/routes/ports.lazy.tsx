import Map from "@/components/Map";
import GenericTable from "@/components/Table";
import { useQuery } from "@tanstack/react-query";
import { createLazyFileRoute } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import { LatLngExpression } from "leaflet";
import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

import Card from "@/components/Card";

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
    country: string;
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
    const [chartData, setChartData] = useState<null | [string, number][]>(null);
    const [filter, setFilter] = useState("");

    useEffect(() => {
        if (data && data.length > 0) {
            const lat = data[0].latitude;
            const lng = data[0].longitude;

            const groupByCountry = data.reduce(
                (result, item) => {
                    if (!result[item.country]) {
                        result[item.country] = [];
                    }

                    result[item.country].push(item);
                    return result;
                },
                {} as Record<string, Ports[]>
            );

            const chardD = Object.keys(groupByCountry).map((country) => ({
                country,
                count: groupByCountry[country].length, // Count of people in each country
            }));

            console.log(groupByCountry);

            setPorts(data);
            setPosition([lat, lng]);
            setChartData(chardD);
        }
    }, [data]);

    return (
        <div className=" flex flex-col gap-4 p-4">
            {ports ? (
                <>
                    <div className="w-full h-[250px]">
                        <Card>
                            <span>Total ports: {ports.length}</span>
                            {chartData && (
                                <ResponsiveContainer
                                    width="100%"
                                    height="90%">
                                    <BarChart
                                        data={chartData}
                                        onClick={(e) =>
                                            setFilter(e.activeLabel || "")
                                        }
                                        margin={{
                                            top: 0,
                                            right: 0,
                                            left: 0,
                                            bottom: 0,
                                        }}>
                                        <CartesianGrid strokeDasharray="3 3" />
                                        <XAxis
                                            dataKey="country"
                                            padding={{ left: 10, right: 10 }}
                                        />
                                        <YAxis />
                                        <Tooltip />
                                        <Bar
                                            dataKey="count"
                                            fill="var(--primary)"
                                        />
                                    </BarChart>
                                </ResponsiveContainer>
                            )}
                        </Card>
                    </div>
                    <div className="flex gap-3">
                        <GenericTable<Ports>
                            size={10}
                            data={ports}
                            filter={filter}
                        />
                        {position && (
                            <div className="bg-white-700 w-[40%]">
                                <Map positions={position} />
                            </div>
                        )}
                    </div>
                </>
            ) : null}
            {isLoading && <div>lodaing...</div>}
            {isError && <div>error...</div>}
        </div>
    );
}
