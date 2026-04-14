from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AvtoShop API"
    api_port: int = 5000
    database_url: str = "sqlite:///./avtoshop.db"
    jwt_secret: str = "change-this-secret-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expires_minutes: int = 120
    cors_origins: str = "http://localhost:5173"
    seed_admin_email: str = "admin@avtoshop.local"
    seed_admin_password: str = "ChangeMe123!"
    seed_sample_data: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
