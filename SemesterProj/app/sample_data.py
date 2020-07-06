def generate():
    from quiz.models import Quiz,Answer

    (quiz1 := Quiz()).save()
    (quiz2 := Quiz()).save()
    Answer(answerText="B", quiz=quiz1).save()
    Answer(answerText="A", quiz=quiz2).save()