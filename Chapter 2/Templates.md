# Templates

Templates allow you to keep the view/presentation seperate from the business logic. They make your code cleaner and have to reside in a templates folder.

Inside the app folder create a templates folder and create an index.html page inside of it. With the following code:

app/templates/index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }} - Microblog</title>
  </head>
  <body>
    <h1>Hello, {{ user.username }}!</h1>
  </body>
</html>
```

the `{{}}` parts are where the dynamic content will go. It will only be known at run time

# Rendering templates

app/routes.py: use render_template() function to show the template we created

```python
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miquel'}
    return render_template('index.html', title='Home', user=user)

```

the render_template will render the file given as the first argument 'index.html' in this case, the next arguments are any dynamic variables listed in the template. In this case those variables would be title and user

The render_template() invokes the Jinja2 template engine that comes bundled with the Flask framework. Jinja2 replaces the {{}} with corresponding values, given by the arguments passed in the render_template() call.

# Conditional Statements

You can use {% %} as conditional statments in templates. The example in the mega tutorial is for if someone forgets to include a title, it will return "Welcome to Microblog". For example:

```html
<!DOCTYPE html>
<html>
  <head>
    {% if title %}
    <title>{{ title }} - Microbe</title>
    {% else %}
    <title>Welcome to Microblog!</title>
    {% endif %}
  </head>
  <body>
    <h1>Hello, {{ user.username }}!</h1>
  </body>
</html>
```

# Looping through data

Jinja2 gives you a 'for' control structure to iterate over a list or object.

```html
<body>
  <h1>Hi, {{user.username}}!</h1>
  {% for post in posts % }
  <div>
    <p>{{ post.author.username }} says: <b> {{ post.body }} </b></p>
    {% endfor %}
  </div>
</body>
```
