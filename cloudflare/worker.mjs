import { env } from "cloudflare:workers";
import { Container, getContainer } from "@cloudflare/containers";

export class AvtoShopApiContainer extends Container {
  defaultPort = 5000;
  sleepAfter = "10m";
  envVars = {
    APP_NAME: env.APP_NAME,
    API_PORT: env.API_PORT,
    DATABASE_URL: env.DATABASE_URL,
    JWT_SECRET: env.JWT_SECRET,
    JWT_ALGORITHM: env.JWT_ALGORITHM,
    JWT_EXPIRES_MINUTES: env.JWT_EXPIRES_MINUTES,
    CORS_ORIGINS: env.CORS_ORIGINS,
    SEED_ADMIN_EMAIL: env.SEED_ADMIN_EMAIL,
    SEED_ADMIN_PASSWORD: env.SEED_ADMIN_PASSWORD,
    SEED_SAMPLE_DATA: env.SEED_SAMPLE_DATA,
  };
}

export default {
  async fetch(request, workerEnv) {
    return getContainer(workerEnv.API_CONTAINER).fetch(request);
  },
};
