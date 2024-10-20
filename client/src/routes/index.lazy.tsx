import { createLazyFileRoute } from "@tanstack/react-router";
import Container from "../ui/Container";

export const Route = createLazyFileRoute("/")({
    component: Index,
});

function Index() {
    return (
        <Container>
            <span className="text-4xl text-blue-500">Some text</span>
        </Container>
    );
}
