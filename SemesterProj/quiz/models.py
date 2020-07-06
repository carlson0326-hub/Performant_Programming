from django.db import models

class Quiz(models.Model):
    quizTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.quizTitle

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=512)

    def __str__(self):
        return self.questionText

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answerText = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct', default=False)

    def __str__(self):
        return self.answerText