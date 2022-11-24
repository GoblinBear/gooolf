import random
from log import Logger


logger = Logger(enable_stream_handler=True)


class Golf:
    def __init__(self, iterations, topn, filepath):
        self.iterations = iterations
        self.topn = topn
        self.number_of_golfer = 0
        self.golfer_name = []
        self.mean = []
        self.standard_deviation = []
        self.tournament_score = []
        self.win_fraction = []
        self.top_n_fraction = []

        try:
            self.__read_input_file(filepath)
        except FileNotFoundError:
            logger.error(f'FileNotFoundError: Input file not found.')
        except ValueError:
            logger.error(f'ValueError: Lines in input file too few.')
    
    def __read_input_file(self, filepath):
        lines = None
        size = None

        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
                size = len(lines)
                if size < 2:
                    raise ValueError
        except FileNotFoundError:
            raise
        except ValueError:
            raise
        finally:
            f.close()

        del lines[0]
        self.number_of_golfer = size - 1

        for line in lines:
            golfer = line[:-1].split()

            golfer_name = ''
            for i in range(len(golfer) - 2):
                golfer_name = golfer_name + golfer[i] + ' '

            self.golfer_name.append(golfer_name[:-1])
            self.mean.append(float(golfer[-2]))
            self.standard_deviation.append(float(golfer[-1]))

    def set_iterations(self, n):
        self.iterations = n

    def __predict_score(self, mean, stdev):
        return random.normalvariate(mean, stdev)

    def __monte_carlo(self, mean, stdev):
        result = 0
        for i in range(self.iterations):
            score = 0
            for round in range(4):
                score = score + self.__predict_score(mean, stdev)
            
            result = result + score / self.iterations
        
        return result

    def __calculate_win_fraction(self):
        self.win_fraction.clear()
        win_score = self.tournament_score[0]
        for score in self.tournament_score:
            if score == win_score:
                self.win_fraction.append(1.0)
            else:
                break

        win_number = len(self.win_fraction)
        for win in self.win_fraction:
            win = round(win / win_number, 2)

        for i in range(win_number, self.number_of_golfer):
            self.win_fraction.append(0)

    def __calculate_top_n_fraction(self):
        self.top_n_fraction.clear()
        for i in range(self.topn):
            self.top_n_fraction.append(1.0)

        score_nth = self.tournament_score[self.topn - 1]

        for i in range(self.topn, self.number_of_golfer):
            if self.tournament_score[i] == score_nth:
                self.top_n_fraction.append(0)
            else:
                break

        score_nth_amount = 0
        for i in range(len(self.top_n_fraction) - 1, -1, -1):
            if self.tournament_score[i] == score_nth:
                score_nth_amount = score_nth_amount + 1
            else:
                break

        remain_score = self.topn - (len(self.top_n_fraction) - score_nth_amount)
        for i in range(len(self.top_n_fraction) - score_nth_amount,
                       len(self.top_n_fraction)):
            self.top_n_fraction[i] = round(remain_score / score_nth_amount, 2)

        for i in range(len(self.top_n_fraction), self.number_of_golfer):
            self.top_n_fraction.append(0)
    
    def run_monte_carlo(self):
        if self.number_of_golfer < 1:
            logger.error(f'No golfer data.')
            return
        
        for i in range(self.number_of_golfer):
            result = self.__monte_carlo(self.mean[i],
                                        self.standard_deviation[i])
            self.tournament_score.append(round(result))

        self.tournament_score.sort()

        self.__calculate_win_fraction()
        self.__calculate_top_n_fraction()

    def display_tournament(self):
        if self.number_of_golfer < 1:
            logger.error(f'No golfer data.')
            return
        
        golfer = 'Golfer'.center(30, ' ')
        score = 'Tournament Score'.center(18, ' ')
        win = 'Win Fraction'.center(16, ' ')

        print(f'{golfer}|{score}|{win}| Top {self.topn} Fraction')
        print(''.center(84, '-'))

        for i in range(self.number_of_golfer):
            print(f'{self.golfer_name[i]: ^30}', end='')
            print(f'{self.tournament_score[i]: ^18}', end='')
            print(f'{self.win_fraction[i]: ^16.2f}', end='')
            print(f'{self.top_n_fraction[i]: ^15.2f}', end='')
            print('')
            print(''.center(84, '-'))


def main():
    golf = Golf(1000, 5, 'ratings.txt')
    golf.run_monte_carlo()
    golf.display_tournament()


if __name__ == '__main__':
    main()
