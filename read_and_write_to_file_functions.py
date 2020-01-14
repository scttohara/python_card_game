import csv
import animals_list


def get_animal_names():
    """

    @return: animals_list
    @rtype: list of lists
    """
    #  try catch for opening and reader from animal name file
    animals_list_of_lists = []
    try:
        with open('animal_names.txt', newline='\n') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                animals_list_of_lists.append(row)

            csv_file.close()

    except PermissionError:
        print('\nALERT:\nCannot open file for reading')
        print('File might be open in another program.')
        print('The default list of animals will be used\n')
        pass
    except FileNotFoundError:
        print('\nALERT:\nCheck that the animal_names.txt file exist in the folder this game is in')
        print('The default list of animals will be used\n')
        pass
    except FileExistsError:
        print('\nALERT:\nIssue with reading in animal names from external file. Will use default list\n')
        pass

    # checks that the list has all the animals if not the animals list is set to a
    # pre-existing list
    try:
        if int(animals_list_of_lists[19][0]) != 10:
            raise IndexError
    except IndexError:
        animals_list_of_lists = animals_list.animals_list_function()

    return animals_list_of_lists


# noinspection PyUnboundLocalVariable,PyUnboundLocalVariable,PyUnboundLocalVariable
def get_game_results_record(path_choice=1):
    """
    try catch for opening and reader from animal name file

    @param path_choice: 1 if user wants to attempt to load past records. 2 if they want to start with new records
    @type path_choice: int
    @return: list of records, player1's record, player2's record, and the draw record
    @rtype: tuple
    """
    records_list_of_lists = []
    if path_choice == 1:  # loads from saved results
        try:
            with open('results_record.txt', newline='\n') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    # print(row)
                    records_list_of_lists.append(row)

                # print(animals_list_of_list[19][0])
                csv_file.close()

        except PermissionError:
            print('\nALERT:\nCannot open file for reading')
            print('File might be open in another program.\n')
            print('Past records will be set to zero for this session\n')
            pass
        except FileNotFoundError:
            print('\nALERT:\nCheck that the results_record.txt file exist in the folder this game is in')
            print('Past records will be set to zero for this session\n')
            pass
        except FileExistsError:
            print('\nALERT:\nCheck that the results_record.txt file exist in the folder this game is in')
            print('Past records will be set to zero for this session\n')
            pass

    if path_choice == 1 or path_choice == 2:  # checks results load or sets results to 0 depending on situation
        #  makes sure something is in records_list_of_lists when it is returned
        try:
            player1 = int(records_list_of_lists[-3][1])
            player2 = int(records_list_of_lists[-2][1])
            draws = int(records_list_of_lists[-1][1])
        except IndexError:
            player1 = 0
            player2 = 0
            draws = 0
            records_list_of_lists.append(['player1', str(player1)])
            records_list_of_lists.append(['player2', str(player2)])
            records_list_of_lists.append(['draws', str(draws)])

    return records_list_of_lists, player1, player2, draws


def write_game_results_record_to_file(results_record, player1, player2, draws):
    """
    try catch for opening and reader from animal name file.

    @param results_record: holds records
    @type results_record: list
    @param player1: count of player1 wins
    @type player1: int
    @param player2: count of player2 wins
    @type player2: int
    @param draws: count of draws
    @type draws: int
    @return: none
    @rtype: none
    """
    try:
        results_record.append(['player1', str(player1)])
        results_record.append(['player2', str(player2)])
        results_record.append(['draws', str(draws)])

        csv_file = open('results_record.txt', 'a', newline='\n')
        csv_writer = csv.writer(csv_file)

        count = -3
        while count < 0:
            line_to_write = [results_record[count][0], results_record[count][1]]

            csv_writer.writerow(line_to_write)
            count += 1

        csv_file.close()
    except PermissionError:
        print('Cannot open file for writing')
        print('File might be open in another program.')
