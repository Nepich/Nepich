from datetime import datetime as dt
from horoscope  import generate_paragraphs, generate_ol

def generate_head (title):
    head = f"\n<meta charset='utf-8'>\n<title>{title}</title>"
    return f"\n<head>{head}\n</head>"

def generate_body (header,paragraphs):
    body = f"\n<h1>{header}</h1>"
    for i in paragraphs:
        body = f"{body}\n<p>{i}</p>"
    return f"\n<body>{body}\n<a href = 'about.html'>О реализации</a>\n</body>"

def generate_page (head,body):
    index = f"<html>{head}{body}\n</html>"
    return index
 
def generate_file (title,header,paragraphs,output="index.html"):
    fp=open(output,"w", encoding="utf-8")
    fp.write(generate_page (generate_head (title),generate_body(header,paragraphs)))
    fp.close()

def generate_about(title, header, body, output="about.html"):
    fp = open(output, "w", encoding="utf-8")
    about_body = f"<body>\n{generate_ol}</body>"
    fp.write(generate_page(generate_head(title),f"\n<body>\n<h1>{header}</h1>\n{body}\n</body>"))
    fp.close


t=f"Ваше предсказание на {dt.now().date()}"
generate_file ("Гороскоп",t,(generate_paragraphs()))
generate_about ("Страница с инфой","О чем все это",(generate_ol()))