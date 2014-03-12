
def add_question_marks():
	filename = open("textfiles/training_data_2012-2013.txt","r")
	writing_file = open("textfiles/march_games_predict.csv","w")
	for line in filename:
		splitline = line.strip("\n").split(",")
		splitline[-1] = "?"
		str_to_write = ",".join(map(str,splitline))
		writing_file.write(str_to_write+"\n")

def calculate_accuracy():
	actual = open("textfiles/march_games.txt","r")
	predict = open("textfiles/march_games_predict.csv","r")

	actual_result = []
	for line in actual:
		actual_result.append(line.strip("\n").split(",")[-1])


	predicted_result = []
	for line in predict:
		predicted_result.append(line.strip("\n").split(",")[-1])

	correct = 0
	total = len(actual_result)

	for i in range(total):
		if actual_result[i] == predicted_result[i]:
			correct+=1

	print float(correct)/float(total)

add_question_marks()
# calculate_accuracy()