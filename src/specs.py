"""
This file contains methods to automatically

1. Generate query names
2. Generate query parameters
3. Extract specific queries from a sumitted python file

"""


def gen_all_q_names(nb_queries=10):
    """
    Generate list of query names

    :param nb_queries:      Amount of query names to be generated
    :return:
    """

    result = [gen_q_name(i) for i in range(nb_queries)]

    return result


def gen_q_name(q_idx):
    """
    Generate single query name

    :param q_idx:   Index of said query name
    :return:
    """

    result = "query_{:02d}".format(q_idx+1) # One-based indexing
    return result


def gen_all_q_method(module, all_q_names):
    """
    Extract the desired methods from the given module

    These 'desired methods' are specified by the q_names
    """

    all_q_method = {}
    for q_name in all_q_names:
        try:
            print("Loading method: {} from module {}".format(q_name, module.__name__))
            all_q_method[q_name] = getattr(module, q_name)
        except BaseException as error:
            method_name = gen_all_q_method.__name__
            print('An exception occurred in method {}:\n{}\n'.format(method_name, error))

    return all_q_method


def gen_all_q_colnam(all_q_names):
    """
    Generate a dict containing all the column names of the solution DataFrames.

    This is hardcoded for manifest uniformity, and assumes the standard setting
    of 10 queries.

    :param all_q_names:     List of query names
                                E.g. 'query_01'
    :return:
    """

    all_q_colnam = {}
    all_q_colnam[all_q_names[0]] = ['tname', 'year','HomeRun']
    all_q_colnam[all_q_names[1]] = ['nameFirst', 'nameLast', 'birthYear', 'birthMonth', 'birthDay']
    all_q_colnam[all_q_names[2]] = ['nameFirst', 'nameLast', 'tname']
    all_q_colnam[all_q_names[3]] = ['tname', 'rank', 'W', 'L', 'nameFirst', 'nameLast']
    all_q_colnam[all_q_names[4]] = ['tname']
    all_q_colnam[all_q_names[5]] = ['tname', 'yearID', 'rank', 'W', 'L']
    all_q_colnam[all_q_names[6]] = ['nameLast', 'nameFirst']
    all_q_colnam[all_q_names[7]] = ['birthState', 'avg_weight', 'avg_height', 'avg_HomeRun', 'avg_Saves']
    all_q_colnam[all_q_names[8]] = ['yearID', 'tname', 'HomeRun']
    all_q_colnam[all_q_names[9]] = ['yearID', 'tname', 'rank', 'Games']

    assert len(set(all_q_colnam)) == len(all_q_names)

    return all_q_colnam


def gen_all_q_params(all_q_names = None):

    if all_q_names is None:
        all_q_names = gen_all_q_names() # Assuming default situation

    all_q_params = {}

    # Query 1
    q_01_p_01 = {}

    all_q_params[all_q_names[0]] = [q_01_p_01]

    # Query 2
    q_02_p_01 = {'datum': '1980-01-16'}
    q_02_p_02 = {'datum': '1985-01-16'}

    all_q_params[all_q_names[1]] = [q_02_p_01, q_02_p_02]

    # Query 3
    q_03_p_01 = {}

    all_q_params[all_q_names[2]] = [q_03_p_01]

    """
    Nb.: Onderstaande parameterwaarden zijn niet de definitieve!
    """

    # Query 4
    q_04_p_01 = {'datum_x': '1980-01-01',
                 'datum_y': '1980-01-01'}

    all_q_params[all_q_names[3]] = [q_04_p_01]

    # Query 5
    q_05_p_01 = {}

    all_q_params[all_q_names[4]] = [q_05_p_01]

    # Query 6
    q_06_p_01 = {'salaris': 20000}

    all_q_params[all_q_names[5]] = [q_06_p_01]

    # Query 7
    q_07_p_01 = {}

    all_q_params[all_q_names[6]] = [q_07_p_01]

    # Query 8
    q_08_p_01 = {'jaar': 1990,
                 'lengte': 75}

    all_q_params[all_q_names[7]] = [q_08_p_01]

    # Query 9
    q_09_p_01 = {'jaar': 1990}

    all_q_params[all_q_names[8]] = [q_09_p_01]

    # Query 10
    q_10_p_01 = {'jaar': 1968}

    all_q_params[all_q_names[9]] = [q_10_p_01]

    assert len(set(all_q_params)) == len(all_q_names)

    return all_q_params