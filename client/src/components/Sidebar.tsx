import { useEffect, useState } from "react";
import { Link, useRouterState } from "@tanstack/react-router";
import { PanelLeftClose, PanelRightClose } from "lucide-react";

import Tooltip from "@/components/Tooltip";
import { linksArray } from "@/utils/sidebar";

const Sidebar = () => {
    const [isExpanded, setIsExpanded] = useState(true);
    const actualRoute = useRouterState();

    useEffect(() => {
        const isOpened = localStorage.getItem("sidebar");
        if (isOpened) {
            isOpened === "true" ? setIsExpanded(true) : setIsExpanded(false);
        }
    }, []);

    const handleExpandSidebar = () => {
        setIsExpanded(!isExpanded);
        if (isExpanded) {
            localStorage.setItem("sidebar", "false");
        }
        if (!isExpanded) {
            localStorage.setItem("sidebar", "true");
        }
    };

    return (
        <div
            className={`flex flex-col p-4 relative h-screen border-r border-gray-800 ${isExpanded ? "w-64" : "w-20"} ${!isExpanded ? "items-center" : ""}`}>
            <button
                className="text-black dark:text-white absolute p-2"
                onClick={handleExpandSidebar}>
                {isExpanded ? (
                    <Tooltip
                        content="close"
                        position="right">
                        <PanelLeftClose />
                    </Tooltip>
                ) : (
                    <Tooltip
                        content="open"
                        position="right">
                        <PanelRightClose />
                    </Tooltip>
                )}
            </button>

            <nav className="mt-10">
                <ul>
                    {linksArray.map((item) => (
                        <li key={item.id}>
                            <Link
                                className={`
                                        flex items-center rounded p-2 text-dark dark:text-white hover:bg-neutral-100 hover:dark:bg-neutral-800 
                                        ${item.path === actualRoute.location.pathname ? "text-cyan-500 dark:text-cyan-500" : ""}
                                    `}
                                to={item.path}>
                                {!isExpanded && (
                                    <Tooltip
                                        content={item.name}
                                        position="right">
                                        <item.icon className="h-6 w-6" />
                                    </Tooltip>
                                )}

                                {isExpanded && (
                                    <>
                                        <item.icon className="h-6 w-6" />
                                        <span className="ml-4">
                                            {item.name}
                                        </span>
                                    </>
                                )}
                            </Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </div>
    );
};

export default Sidebar;
