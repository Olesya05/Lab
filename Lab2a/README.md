File message

1. Result of `python .`
 ```
We are in the __main__
2020-11-10 21:11:58.857192
win32

```
 
 2 . Result of  `python . -h`
 
 ```
 usage: _main_.py [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.
```

 3. Result of  `python . -o "Цей текст також має вивестись"`
 ```
 We are in the __main__
2020-11-07 21:57:41.107362
win32
З консолі було передано аргумент
 ========== >> Цей текст також має вивестись << ==========
```

 4 . Result of `python . --logs`
 
 ```
 2020-11-10 21:15:21,565 root INFO: Тут буде просто інформативне повідомлення
2020-11-10  21:15:21,566 root WARNING: Це Warning повідомлення
2020-11-10  21:00:21,567 root ERROR: Це повідомлення про помилку
```
