Draftail extensions for the Wagtail CMS
---------------------------------------

This repo has examples of extensions for the Draftail editor which is used in the Wagtail CMS.

An explanation of these extensions can be found in [this post](https://medium.com/@timlwhite/custom-in-line-styles-with-draftail-939201c2bbda).

The `home/wagtail_hooks.py` file is where you should look for the extensions.

How to use:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Browse to http://127.0.0.1:8000/admin/pages/3/edit/ to edit the home page and try out the extensions in the body field.  You'll need to log in as the user you created in the `createsuperuser` step above.

This project shell was generated with `wagtail start`.

