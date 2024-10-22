import { Link } from "@/types/sidebar";
import {
    Anchor,
    BriefcaseConveyorBelt,
    HomeIcon,
    Route,
    Ship,
    ShipWheel,
    Users,
    Container,
    User,
    Handshake
} from "lucide-react";

export const linksArray: Link[] = [
    {
        id: 1,
        name: "Dasboard",
        path: "/",
        icon: HomeIcon,
    },
    {
        id: 2,
        name: "Vessels",
        path: "/vessels",
        icon: Ship,
    },
    {
        id: 3,
        name: "Ports",
        path: "/ports",
        icon: ShipWheel,
    },
    {
        id: 4,
        name: "Customers",
        path: "/customers",
        icon: Handshake,
    },
    {
        id: 5,
        name: "Routes",
        path: "/routes",
        icon: Route,
    },
    {
        id: 6,
        name: "Voyages",
        path: "/voyages",
        icon: Anchor,
    },
    {
        id: 7,
        name: "Shipments",
        path: "/shipments",
        icon: BriefcaseConveyorBelt,
    },
    {
        id: 8,
        name: "Containers",
        path: "/containers",
        icon: Container,
    },
    {
        id: 9,
        name: "Employees",
        path: "/employees",
        icon: User,
    },
];
