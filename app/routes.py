from flask import Flask, redirect, render_template
from app import app
from app.emails import Email
from app.models import Reminder
from datetime import datetime, timedelta, date

@app.route('/', methods=['GET'])
def index():
    return 'index'

@app.route('/reminder/<send_to>/<reminder_message>/<reminder_days>', methods=['GET'])
def set_reminder(send_to ,reminder_message, reminder_days):
  
    day_to_be_reminded = date.today() + timedelta(days=int(reminder_days))
    Reminder.add_reminder(send_to, reminder_message, day_to_be_reminded)

    return f'Reminder Set! An email will be sent to {send_to} on {day_to_be_reminded} with the following reminder: {reminder_message}'


