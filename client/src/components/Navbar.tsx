import Tooltip from "@/components/Tooltip";
import { Sun, Moon } from "lucide-react";
import { useState, useEffect } from "react";

const Navbar = () => {
    const [theme, setTheme] = useState<"light" | "dark">("light");

    useEffect(() => {
        if (theme === "dark") {
            document.documentElement.classList.add("dark");
        } else {
            document.documentElement.classList.remove("dark");
        }
    }, [theme]);

    const toggleTheme = () => {
        setTheme(theme === "light" ? "dark" : "light");
    };

    return (
        <div className="w-full p-4 border-b border-gray-800 flex justify-between">
            <div className="flex align-middle gap-2">
                <div className="flex align-middle gap-1">
                    <div className="w-[20px] h-[20px] bg-slate-600"></div>
                    <span>NaviLogix</span>
                </div>
                <span>2024/01/01</span>
            </div>
            <button onClick={toggleTheme}>
                {theme === "light" ? (
                    <Tooltip
                        content="dark mode"
                        position="bottom">
                        <Moon />
                    </Tooltip>
                ) : (
                    <Tooltip
                        content="light mode"
                        position="bottom">
                        <Sun />
                    </Tooltip>
                )}
            </button>
        </div>
    );
};

export default Navbar;
