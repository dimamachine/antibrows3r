# antibrows3r

Установка chromedrive.exe в папку с проектом:  

https://chromedriver.chromium.org/ - советую устанавливать ChromeDriver 111.0.5563.64 (Latest stable release)  

Создаём файл .evn с следующим содержанием:  

PROXY_HOST=<IP>  
PROXY_PORT=<PORT>  
PROXY_USER=<USER>  
PROXY_PASS=<PASSWORD>  

Устанавливаем необходимые библиотеки:  

python3 -m pip install -r /requirements.txt  

В конструкции 
```python
with Pool(processes=10) as p:
        windows = [[600 * i % 1800, 0] for i in range(10)]
        p.map(main, windows)
```

python3 test.py
```
