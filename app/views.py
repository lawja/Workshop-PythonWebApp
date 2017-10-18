from flask import url_for, redirect, render_template, request, session
from app import app
import sqlite3
import time

@app.route('/', methods=["GET", "POST"])
def index():
    conn = sqlite3.connect(app.config['DATABASE_PATH'])

    c = conn.cursor()

    create_table = '''
    CREATE TABLE
    IF NOT EXISTS posts (
     id integer PRIMARY KEY,
     title text NOT NULL,
     content text,
     create_time text NOT NULL
    );
    '''

    c.execute(create_table)

    conn.commit()

    get_posts = '''
    SELECT * FROM posts
    '''

    posts = c.execute(get_posts)

    formatted_posts = []
    for post in posts:
        number, title, content, post_time = post

        formatted_post = '''
        <div class="col-md-12 post">
          <strong>{post_number} ({post_time}) - {post_title}</strong>
          <br>
          {post_content}
        </div>'''.format(post_number=number, post_time=post_time,
                         post_title=title, post_content=content)

        formatted_posts.append(formatted_post)
    formatted_posts = '\n'.join(formatted_posts[::-1])

    conn.close()

    return render_template('index.html', posts=formatted_posts)

@app.route('/write-post', methods=["POST"])
def write_post():
    data = request.form
    title = data['title']
    content = data['content']
    key = data['key']

    if(key == app.config['BLOG_KEY']):
        conn = sqlite3.connect(app.config['DATABASE_PATH'])

        c = conn.cursor()

        create_table = '''
        CREATE TABLE
        IF NOT EXISTS posts (
         id integer PRIMARY KEY,
         title text NOT NULL,
         content text,
         create_time text NOT NULL
        );
        '''

        c.execute(create_table)

        raw_time = time.localtime()

        timestamp = str(raw_time.tm_mon) + '-' + str(raw_time.tm_mday) + \
                    '-' + str(raw_time.tm_year)


        insert_post = '''
        INSERT INTO posts (
          title,
          content,
          create_time)
        VALUES
          (
            "%s",
            "%s",
            "%s"
          )''' % (title, content, timestamp)

        c.execute(insert_post)

        conn.commit()
        conn.close()

    return redirect(url_for(".index"))