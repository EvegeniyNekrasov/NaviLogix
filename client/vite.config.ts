import path from "path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import { TanStackRouterVite } from "@tanstack/router-plugin/vite";

export default defineConfig({
    plugins: [TanStackRouterVite(), react()],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "src"),
            // "@components": path.resolve(__dirname, "src/components"),
            // "@ui": path.resolve(__dirname, "src/ui"),
            // "@hooks": path.resolve(__dirname, "src/hooks"),
            // "@types": path.resolve(__dirname, "src/types"),
            // "@utils": path.resolve(__dirname, "src/utils"),
        },
    },
});
