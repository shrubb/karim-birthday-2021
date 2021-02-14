Minimal word puzzle in [Django](https://www.djangoproject.com/)
===

I made this word puzzle to congratulate [karfly](https://github.com/karfly/), but hope someone else finds it useful too.

![image](https://user-images.githubusercontent.com/9570420/107872930-2bf1ae00-6ebf-11eb-9f6a-22bd606d0f0f.png)

Features:
* An insecure login page (no passwords).
* A word-specific image pops up on correct guess of a "target" word, and a random image on a nonsense "extra"/"obfuscating" word.
* Record tracking and a leaderboard.

Running:
* Prepare the database:
  * If you want to replicate the original birthday version, download and unpack images, the actual historical birthday database, and some extra word-related helpers from [Releases](https://github.com/shrubb/karim-birthday-2021/releases).
  * Else, use [initialize_field_and_words_in_db.py](./initialize_field_and_words_in_db.py) and put some images to `static/images/random/vsratoslav` and to `static/images/specific/lobster`.
* Install dependencies: `pip install -r requirements.txt`
* Run `python manage.py runserver` (not for production) and visit http://127.0.0.1:8000/
