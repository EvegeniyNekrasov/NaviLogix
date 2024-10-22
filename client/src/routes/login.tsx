import { isAuthenticated } from "@/utils/auth";
import { createFileRoute, redirect } from "@tanstack/react-router";

export const Route = createFileRoute("/login")({
    beforeLoad: async () => {
        if (!isAuthenticated()) {
            throw redirect({ to: "/login" });
        }
    },
    component: () => <div>Hello /login!</div>,
});
