import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_files = {
        "dev": "config/.env.dev",
        "test": "config/.env.test",
        "prod": "config/.env.prod",
    }

    if environment not in env_files:
        raise ValueError(
            f"Unknown environment '{environment}'. Use dev, test, or prod."
        )

    load_dotenv(env_files[environment])


def load_secrets_to_env(path: str = "secrets.yaml") -> None:
    """
    Wczytuje odszyfrowany plik secrets.yaml i wrzuca wartości do zmiennych środowiskowych.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Secrets file '{path}' not found. Did you decrypt it?")

    with open(path, "r") as f:
        data = yaml.safe_load(f)

    for key, value in data.items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    load_secrets_to_env()

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", settings.api_key)
    print("PASSWORD:", settings.password)
