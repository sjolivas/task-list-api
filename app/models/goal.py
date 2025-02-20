from flask import current_app
from app import db

class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal", lazy=True)


    def goal_dict(self):
        return {
            "id": self.goal_id,
            "title": self.title
        }


    def goal_and_task_dict(self):
        return{
            "id": self.goal_id,
            "title": self.title,
            "tasks": [task.task_and_goal_dict() for task in self.tasks]
        }
