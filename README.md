# mkdocs_with_auth

- Hosted on [Heroku](https://mkdocs-with-auth.herokuapp.com).
- Test credentials:
    - username: `user`
    - password: `user-password`


## Prerequisites
- Create a [GitHub](https://github.com) account.
- Create a [Heroku](https://www.heroku.com) account.
- [Download git](https://git-scm.com/downloads).
- [Download heroku cli](https://devcenter.heroku.com/articles/heroku-cli).


## Steps:
- Prepare project:
    ```bash
    # download project
    $ cd <desired>/<path>
    $ git clone https://github.com/ionescuig/mkdocs_with_auth.git
    # install requirements
    $ python3 -m venv venv      # depends on your system: "python" or "python3" or "py"
    $ .\venv\Scripts\activate   # windows
    # or
    $ source venv/bin/activate  # linux/mac
    $ pip install -r requirements.txt
    ```

- Add project to your GitHub repo.
  
- Create new app on Heroku.

- Conect Heroku to GitHub repo and click **Enable Automatic Deploys**.
  
- Set random SECRET_KEY for production
    ```bash
    $ python
    >>> import secrets
    >>> secrets.token_urlsafe(52)
    # copy <KEY>
    >>> quit()
    $ heroku config:set SECRET_KEY=<KEY>
    ```

- Add postgresql addon
    ```bash
    $ heroku addons:create heroku-postgresql:hobby-dev
    ```

- Disable collectstatic on heroku
    ```bash
    $ heroku config:set DISABLE_COLLECTSTATIC=1
    ```

- Migrate, create superuser and scale heroku web dynos.
    ```bash
    $ heroku run python manage.py migrate
    $ heroku run python manage.py createsuperuser
    $ heroku ps:scale web=1
    ```

## Create/Edit documentation
- How To:
  - [Add documetation page](mkdocs/how-to/add-new-documentation-page.md).
  - [Mkdocs commands](mkdocs/index.md).
  - [Markdown useful tips](mkdocs/how-to/use-markdown.md).

-  Check that everything works fine
    ```bash
    $ mkdocs build
    $ python manage.py runserver    # navigate to http://127.0.0.1:8000/
    ```

- Commit and push your changes. Every new push to GitHub repo will trigger a new Heroku build (the build will take a few minutes).

## Links:
- [Mkdocs official page](https://www.mkdocs.org)
