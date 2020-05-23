from DataProcessor import DataReader
from DataProcessor.Naive_Bayes_Alg import Naive_Bayes_Alg

data_dict = DataReader.read_csv_data('/Users/juliadebecka/Documents/GitHub/NAI/NaiveBayes/Resources/car.data')

test_data_dict = DataReader.read_csv_data('/Users/juliadebecka/Documents/GitHub/NAI/NaiveBayes/Resources/car.test.data')


naive = Naive_Bayes_Alg(data_dict)

naive.train()

naive.test_data(test_data_dict)