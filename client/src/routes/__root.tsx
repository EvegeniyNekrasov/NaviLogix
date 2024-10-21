import { createRootRoute, Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/router-devtools";
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

export const Route = createRootRoute({
    component: () => (
        <div className="h-screen grid grid-cols-[auto_1fr_1fr] grid-rows-[auto_1fr]">
            <div className="row-span-2">
                <Sidebar>
                    <span>aklsj</span>
                </Sidebar>
            </div>
            <div className="col-span-2 ">
                <Navbar />
            </div>
            <div className="col-span-2">
                <Outlet />
            </div>

            <TanStackRouterDevtools />
        </div>
    ),
});
