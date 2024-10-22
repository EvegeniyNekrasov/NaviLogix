import { createLazyFileRoute } from "@tanstack/react-router";

export const Route = createLazyFileRoute("/ports")({
    component: Ports,
});

function Ports() {
    return (
        <div className="p-4 flex flex-col gap-3">
            <span>port 1</span>
            <span>port 2</span>
            <span>port 3</span>
            <span>port 4</span>
        </div>
    );
}
