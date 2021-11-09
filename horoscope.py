import random

data_list={
    "Время":["утром","в обед","перед сном","перед пробуждением","ночью","после обеда"],
    "Совет":["ожидайте","остерегайтесь","примите","будьте готовы","будьте открыты для"],
    "Событие":["денег","долгожданную встречу","новое знакомство","приятных перемен","неприятностей"],
    "Пожелание":["удачи","крепись","бди","жди"]
}

time = ["утром","в обед","перед сном","перед пробуждением","ночью","после обеда"]
advice = ["ожидайте","остерегайтесь","примите","будьте готовы","будьте открыты для"]
promiss = ["денег","долгожданную встречу","новое знакомство","приятных перемен","неприятностей"]
add = ["удачи","крепись","бди","жди"]



def generate_paragraphs(total_num=3,total_sentence=4):
    prophecies = []
    for i in range(total_num):
        forecast = ""
        for j in range(total_sentence):
            t=random.choice(time)
            a=random.choice(advice)
            p=random.choice(promiss)
            ad=random.choice(add)
            sentence = f"{t.title()} {a} {p}, {ad}."
            if j!=total_sentence-1:
                sentence = f"{sentence} "
            forecast = forecast + sentence
        prophecies.append(forecast)
    return prophecies

def generate_ol():
    ol=""
    for i in data_list:
        ul=""
        for j in data_list[i]:
            ul+=f"<li>{j}</li>\n"
        ol+=f"<ol>{i}:\n<ul>\n{ul}</ul>\n</ol>\n"
    return f"{ol}<a href = 'index.html'>Назад</a>\n"
