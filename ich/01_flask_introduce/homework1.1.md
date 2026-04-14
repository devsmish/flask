# Найдите ошибку в коде:

```Python
from flask import Flask


app = Flask(__name__)

@app.route('')  # ошибка (Роут всегда должен начинаться с '/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

# Правильный вариант
```@app.route('/')```
