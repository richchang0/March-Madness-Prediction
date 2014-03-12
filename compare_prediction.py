import os

def add_question_marks(fileName):
	filename = open("textfiles/model_data/" + fileName + ".csv","r")

	writing_file = open("textfiles/model_data/" + fileName + "_predict.csv","w")

	isFirst = True
	for line in filename:
		if isFirst:
			isFirst = False
			writing_file.write(line)
		else:
			splitline = line.strip("\n").split(",")
			splitline[-1] = "?"
			str_to_write = ",".join(map(str,splitline))
			writing_file.write(str_to_write+"\n")


def calculate_accuracy():
	actual = open("textfiles/games/march_games.txt","r")
	predict = open("textfiles/model_results/march_games_data_fixed_predict_results.csv","r")

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

def main():
	# fileName = 'march_games_data_fixed'
	# add_question_marks(fileName)

	# resultFileName = ''
	calculate_accuracy()

main()