# python.org 
## example implementation of Zoot automation framework

## Usage

### 1.) Install library
```
    pip install zoot

```

### 2.) Configure

#### config.json

```json
{
    "data_path":"features",
    "step_path":"definitions",
    "tags":"home",
    "os":"windows",
    "browser":"chrome",
    "driver_path":"resources\\chromedriver.exe",
    "appium_path":null,
    "url":"http://python.org",
    "mlo":["env.py", "pages.py", "steps.py"]
}

```

### 3.) Run

```
zoot config.json

```