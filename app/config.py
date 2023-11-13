from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    ACCESS_TOKEN_EXPIRES_IN: int
    REFRESH_TOKEN_EXPIRES_IN: int

    CLIENT_ORIGIN: str

    JWT_ALGORITHM: str
    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str

    class Config:
        env_file = './.env'


settings = Settings()
