import datetime

def get_data_atual() -> str:
    agora = datetime.datetime.now()
    chegada = f"{agora.day}-{agora.month}-{agora.year} {agora.hour}:{agora.minute}"
    return chegada