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
            <span>some text</span>
            <button onClick={toggleTheme}>
                {theme === "light" ? (
                    <Tooltip content="dark mode" position="bottom">
                        <Moon />
                    </Tooltip>
                ) : (
                    <Tooltip content="light mode" position="bottom">
                        <Sun />
                    </Tooltip>
                )}
            </button>
        </div>
    );
};

export default Navbar;
