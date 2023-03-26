# antibrows3r

## Установка chromedrive.exe в папку с проектом:  
https://chromedriver.chromium.org/  
Советую устанавливать ChromeDriver 111.0.5563.64 (Latest stable release)  

## Создаём файл .env следующего содержания: 
```bash
PROXY_HOST=<IP>  
PROXY_PORT=<PORT>  
PROXY_USER=<USER>  
PROXY_PASS=<PASSWORD>  
```  
## Устанавливаем необходимые библиотеки:  
```bash
python3 -m pip install -r /requirements.txt
```  
## В конструкции задаём стартовую страницу X:
```python
def main
...
    driver.get("X")
...
```
## В конструкции задаём необходимое количество процессов Y (окон браузера):  
```python
with Pool(processes=Y) as p:
        windows = [[600 * i % 1800, 0] for i in range(Y)]
        p.map(main, windows)
```
## Запускаем проект:  
```bash
python3 antibrows3r.py
```
### Для закрытия всех окон необходимо перейти в терминал и подать команду "Esc" в количестве запущенных процессов
