import dotenv from "dotenv";
import { cleanEnv, host, port, str, testOnly } from "envalid";

dotenv.config();

export const ENV = cleanEnv(process.env, {
	NODE_ENV: str({
		devDefault: testOnly("test"),
		choices: ["test", "development", "production"],
	}),
	PORT: port({ devDefault: testOnly(3000) }),
	HOST: host({ devDefault: testOnly("localhost") }),
	CORS_ORIGIN: str({ devDefault: testOnly("http://localhost:3000") }),
});
