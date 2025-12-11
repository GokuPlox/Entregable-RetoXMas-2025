from pydantic_settings import BaseSettings
from pydantic import Field, field_validator

#Se usa pydantic porque maneja los casos de eerror cuando no se 
#  pueda acceder con el url dado para db o lo q sea que pong


class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")


    @field_validator("DATABASE_URL")
    #se usa @ para decorar la funcion y que haga mas con menos, procesa y registra la funcion
    def validate_database_url(cls, v):
        #cls es la clase q esta siendo usada , setting q es la q usa pydantic
        #v es el valor que se esta validando
        if "://" not in v:
            #se :// pq todoas las url comeinzan asi 
            raise ValueError("Database URL no existe o no es correcto")
        #raise detiene la ekecicion si no se cumple la condicion
        return v
    
    class Config:
        env_file = ".env"
        #esto es para q lea el archiovo de env
    
settings = Settings()