default_config = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 500,
    "streaming": False
}

user_config = {
    "model": "gpt-4",
    "max_tokens": 1000
}

final_config={**user_config,**default_config}

for key,value in final_config.items():
    print(f"{key}:{value}")
    
# adding elements using setdefaultmethod


config={}

config.setdefault("model","claude")
config.setdefault("temperature",0.7)
print(config)
#  default values for all keys using fromkey()
default=dict.fromkeys(["mode","max","min"],None)
print(default)