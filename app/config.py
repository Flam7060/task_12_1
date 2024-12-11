from pydantic_settings import BaseSettings

class Config(BaseSettings):
    app_name: str = "Калькулятор треугольника"
    width: int = 400
    height: int = 400

    class Config:
        env_file = ".env"   

get_config = Config()   