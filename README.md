# my-first-blog

implement the simple blog by The Django Girls tutorial.

## Tutorial

- [Django Girls のチュートリアル](https://tutorial.djangogirls.org/ja/)
- [Homework: add more to your website!](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/en/homework/)

## Heroku files

- [Deploy!](https://djangogirlsjapan.gitbooks.io/workshop_tutorialjp/deploy/)
- Procfile
- runtime.txt

## 環境構築

仮想環境のPythonをactivateすると、myvenv\Scriptsにパスが通っている状態になります。
そのためdjango-admin.exeなども使えるようになります。

```powershell
py -3 -m venv myvenv
myvenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
django-admin.exe startproject mysite .
python manage.py migrate
python manage.py runserver
python manage.py startapp blog
python manage.py makemigrations blog
python manage.py migrate blog

python manage.py createsuperuser

```

## requirements.txtのセーブとロード

```powershell
pip freeze > requirements.txt
pip install -r requirements.txt
```
