import { createLazyFileRoute } from "@tanstack/react-router";
import Container from "@ui/Container";
import { Camera } from "lucide-react";

export const Route = createLazyFileRoute("/")({
    component: Index,
});

function Index() {
    return (
        <Container>
            <Camera />
            <span className="text-4xl text-blue-500">Some text</span>
        </Container>
    );
}
