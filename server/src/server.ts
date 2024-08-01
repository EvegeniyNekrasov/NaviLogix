import { ENV } from "@/utils/envConfig";
import cors from "cors";
import express, { type Express } from "express";
import { pino } from "pino";

const logger = pino({ name: "server start" });
const app: Express = express();

app.set("trust proxy", true);
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors({ origin: ENV.CORS_ORIGIN, credentials: true }));
app.get("/", (req, res) => {
    res.send([
        {
            id: 1,
            name: "John Doe",
            age: 25,
        },
        {
            id: 2,
            name: "Jane Doe2",
            age: 22,
        },
    ])
})



export { app, logger };
