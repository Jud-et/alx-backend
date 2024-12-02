# 0x02. i18n Backend Project README 🌍🚀

## Project Overview
This project focuses on internationalization (i18n) in a Flask application, demonstrating how to create a multilingual web application that can dynamically adjust language and locale settings.

## 🎯 Learning Objectives Achieved

### 1. Parametrizing Flask Templates for Multiple Languages 🌐
- Implemented Flask-Babel for internationalization
- Created translation files (messages.po) for English and French
- Used `gettext()` and `_()` functions to mark translatable strings
- Configured babel.cfg for extracting and compiling translations
- Demonstrated dynamic language switching in templates

**Code Example:**
```python
from flask_babel import gettext as _

@app.route('/')
def index():
    return render_template('index.html', 
        title=_('home_title'), 
        header=_('home_header'))
```

### 2. Inferring Correct Locale 🕵️‍♀️
Implemented multiple strategies for locale selection:
- URL parameter detection
- User preference detection
- Browser language detection
- Fallback to default locale

**Locale Selection Logic:**
```python
@babel.localeselector
def get_locale():
    # Priority: 
    # 1. URL parameter
    # 2. User settings
    # 3. Request headers
    # 4. Default locale
    
    # URL parameter check
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    
    # User preference check
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Browser language detection
    return request.accept_languages.best_match(app.config['LANGUAGES'])
```

### 3. Localizing Timestamps 🕰️
- Used `pytz` for timezone handling
- Implemented timezone selection logic
- Displayed localized timestamps based on user preferences

**Timezone Selection:**
```python
@babel.timezoneselector
def get_timezone():
    # Priority:
    # 1. URL parameter
    # 2. User settings
    # 3. Fallback to UTC
    
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    
    if g.user and g.user['timezone']:
        return g.user['timezone']
    
    return 'UTC'
```

## 🛠 Key Technologies
- Flask
- Flask-Babel
- pytz
- Jinja2 translations
- Python type annotations

## 📦 Project Structure
```
0x02-i18n/
├── app.py
├── babel.cfg
├── templates/
│   └── index.html
└── translations/
    ├── en/
    └── fr/
```

## 🚀 How to Run
1. Install dependencies:
```bash
pip install flask flask-babel==2.0.0 pytz
```

2. Extract translation strings:
```bash
pybabel extract -F babel.cfg -o messages.pot .
```

3. Initialize translations:
```bash
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
```

4. Compile translations:
```bash
pybabel compile -d translations
```

5. Run the application:
```bash
python app.py
```

## 💡 Advanced Features
- Mocked user login system
- Dynamic language and timezone selection
- Localized welcome messages
- Timezone-aware timestamp display

## 🌟 Challenges Overcome
- Implementing flexible locale detection
- Managing translations across multiple languages
- Handling timezone complexities
- Creating a seamless user experience

## 📝 Lessons Learned
- Importance of internationalization in web applications
- Techniques for language and locale management
- Best practices for creating multilingual interfaces

## 🔍 Potential Improvements
- Add more languages
- Implement persistent user language preferences
- Enhanced timezone handling
- More comprehensive translation coverage

## 📄 License
This project is part of the ALX Backend Engineering curriculum.

---

**Note:** This README demonstrates the comprehensive approach to internationalization in a Flask application, showcasing how to create a flexible, multilingual web experience. 🌍🚀
