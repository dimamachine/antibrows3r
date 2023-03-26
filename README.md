# antibrows3r

## Установка chromedrive.exe в папку с проектом:  
https://chromedriver.chromium.org/  
Советую устанавливать ChromeDriver 111.0.5563.64 (Latest stable release)  

## Создаём файл .evn следующего содержания: 
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
## В конструкции задаём необходимое количество процессов X (окон браузера):  
```python
with Pool(processes=X) as p:
        windows = [[600 * i % 1800, 0] for i in range(X)]
        p.map(main, windows)
```
## Запускаем проект:  
```bash
python3 test.py
```
