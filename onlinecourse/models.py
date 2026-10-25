
# Question model
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def is_get_score(self, selected_choices):
        correct_choices = self.choice_set.filter(is_correct=True)
        return set(correct_choices) == set(selected_choices)

    def __str__(self):
        return self.question_text


# Choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


# Submission model
class Submission(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
    )
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return (
            f"{self.enrollment.user.username} - "
            f"{self.enrollment.course.name}"
        )
