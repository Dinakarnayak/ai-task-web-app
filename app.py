import openai
from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

# Set your OpenAI API key
openai.api_key = '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'

app = Flask(__name__)

# Function to interact with OpenAI API
def handle_task(prompt, max_tokens=150):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response['choices'][0]['text'].strip()
    except openai.error.OpenAIError as e:
        return f"Error occurred: {e}"

# Function to insert result into the database
def insert_to_db(table, data):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} (content, timestamp) VALUES (?, ?)", (data, datetime.now()))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faq', methods=['POST'])
def faq():
    question = request.form['question']
    prompt = f"You are a support assistant. Answer the following question in one paragraph: {question}"
    answer = handle_task(prompt)
    
    insert_to_db('faq', answer)  # Save result to database
    return render_template('result.html', task='FAQ', result=answer)

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    prompt = f"Summarize the following text in under 150 words: {text}"
    summary = handle_task(prompt)
    
    insert_to_db('summaries', summary)  # Save result to database
    return render_template('result.html', task='Summary', result=summary)

@app.route('/journal', methods=['POST'])
def journal():
    journal_entry = request.form['journal_entry']
    prompt = f"Generate a positive reflection or insight based on this journal entry: {journal_entry}"
    reflection = handle_task(prompt)
    
    insert_to_db('journals', reflection)  # Save result to database
    return render_template('result.html', task='Journal Reflection', result=reflection)

@app.route('/idea', methods=['POST'])
def idea():
    topic = request.form['topic']
    prompt = f"Generate three unique ideas related to the following topic: {topic}"
    ideas = handle_task(prompt)
    
    insert_to_db('ideas', ideas)  # Save result to database
    return render_template('result.html', task='Ideas', result=ideas)

@app.route('/email', methods=['POST'])
def email():
    email_content = request.form['email_content']
    prompt = f"Write a professional reply to the following email: {email_content}"
    reply = handle_task(prompt)
    
    insert_to_db('emails', reply)  # Save result to database
    return render_template('result.html', task='Email Reply', result=reply)

@app.route('/code', methods=['POST'])
def code():
    task_description = request.form['task_description']
    prompt = f"Write a Python function that solves the following problem: {task_description}"
    code_snippet = handle_task(prompt)
    
    insert_to_db('code_snippets', code_snippet)  # Save result to database
    return render_template('result.html', task='Code Snippet', result=code_snippet)

@app.route('/blog', methods=['POST'])
def blog():
    keywords = request.form['keywords']
    prompt = f"Write a short blog post about: {keywords}"
    blog_content = handle_task(prompt, max_tokens=300)
    
    insert_to_db('blogs', blog_content)  # Save result to database
    return render_template('result.html', task='Blog', result=blog_content)

@app.route('/quiz', methods=['POST'])
def quiz():
    topic = request.form['quiz_topic']
    prompt = f"Generate 5 quiz questions with answers about: {topic}"
    quiz = handle_task(prompt, max_tokens=300)
    
    insert_to_db('quizzes', quiz)  # Save result to database
    return render_template('result.html', task='Quiz', result=quiz)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.form['sentiment_text']
    prompt = f"Analyze the sentiment of the following text and classify it as Positive, Negative, or Neutral: {text}"
    sentiment = handle_task(prompt, max_tokens=50)
    
    insert_to_db('sentiments', sentiment)  # Save result to database
    return render_template('result.html', task='Sentiment', result=sentiment)

@app.route('/review', methods=['POST'])
def review():
    review = request.form['review']
    prompt = f"Summarize the following product review in a few sentences: {review}"
    summary = handle_task(prompt)
    
    insert_to_db('product_reviews', summary)  # Save result to database
    return render_template('result.html', task='Product Review', result=summary)

@app.route('/course', methods=['POST'])
def course():
    description = request.form['description']
    subject = request.form['subject']
    level = request.form['level']
    prompt = f"Create a table of contents for a course based on this description: {description}. Subject: {subject}, Level: {level}"
    table_of_contents = handle_task(prompt, max_tokens=300)
    
    insert_to_db('courses', table_of_contents)  # Save result to database
    return render_template('result.html', task='Course Table of Contents', result=table_of_contents)

if __name__ == '__main__':
    app.run(debug=True)
