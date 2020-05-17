from app.database import db

class Reminder(db.Model):
    __tablename__ = 'reminder'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300))
    message = db.Column(db.String(500))
    send_date = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @staticmethod
    def add_reminder(send_to, message, date):
        new_reminder = Reminder(email=send_to, message=message, send_date=date).add()
        