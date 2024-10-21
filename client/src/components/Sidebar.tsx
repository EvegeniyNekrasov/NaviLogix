import type React from "react";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";

const Sidebar = ({ children }: { children: React.ReactNode }) => {
    return (
        <SidebarProvider>
            <main>
                <SidebarTrigger />
                {children}
            </main>
        </SidebarProvider>
    );
};

export default Sidebar;
