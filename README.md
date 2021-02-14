Minimal word puzzle in [Django](https://www.djangoproject.com/)
===

I made this word puzzle to congratulate [karfly](https://github.com/karfly/), but hope someone else finds it useful too.

Running:
* Prepare the database:
  * If you want to replicate the original birthday version, download and unpack images, the actual historical birthday database, and some extra word-related helpers from [Releases](./releases).
  * Else, use [initialize_field_and_words_in_db.py](./initialize_field_and_words_in_db.py) and put some images to `static/images/random/vsratoslav` and to `static/images/specific/lobster`.
* Install dependencies: `pip install -r requirements.txt`
* Run `python manage.py runserver` (not for production) and visit http://127.0.0.1:8000/