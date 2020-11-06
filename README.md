**0. Prerequisites:**

```
Python 3.6+, gcc (for compiling sqlalchemy)
```

**1. Installation:**
```
git clone https://github.com/lasagnu/fastapi-postgres
cd ./fastapi-postgres
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Configuration:**

All required data/credentials could be passed via [environment variables](https://www.google.com/search?q=how+to+set+environment+variables+linux), their names could be found  in 
**backend/app/core/config.py**

**3. Startup:**

Once the configuration data is provided (or isn't..) just run the **main.py** file:
```
python main.py
```

Enjoy this awesome framework!
