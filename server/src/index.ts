import { app, logger } from "@/server";
import { ENV } from "@/utils/envConfig";

const server = app.listen(ENV.PORT, ENV.HOST, () => {
	const { NODE_ENV, HOST, PORT } = ENV;
	logger.info(`Server (${NODE_ENV}) is running on port http://${HOST}:${PORT}`);
});

const onCloseSignal = () => {
	logger.info("Server is shutting down...");
	server.close(() => {
		logger.info("Server has been shut down.");
		process.exit(0);
	});
	setTimeout(() => process.exit(1), 10000).unref();
};

process.on("SIGINT", onCloseSignal);
process.on("SIGTERM", onCloseSignal);
