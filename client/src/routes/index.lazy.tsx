import { createLazyFileRoute } from "@tanstack/react-router";

export const Route = createLazyFileRoute("/")({
    component: Index,
});

function Index() {
    return <span className="text-4xl text-blue-500">Some text</span>;
}
