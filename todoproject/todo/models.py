from django.db import models

PRIORITY = (('danger','high'),('warning','middle'),('info', 'normal'))
class TodoModel(models.Model):
  "項目を作成していきます"
  title = models.CharField(max_length=100) # 文字列のフィールド
  memo = models.TextField()
  priority = models.CharField(
    max_length = 50,
    choices = PRIORITY # 選択肢(selectboxのようなもの)
  )
  duedate = models.DateField() # 期限
  def __str__(self):
    return self.title
