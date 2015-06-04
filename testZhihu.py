from zhihu import Question

url = "http://www.zhihu.com/question/24269892"
question = Question(url)
answers = question.get_all_answers()
for answer in answers:
    answer.to_txt()
