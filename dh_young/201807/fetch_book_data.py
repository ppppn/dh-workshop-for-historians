import json
import requests
from argparse import ArgumentParser
from multiprocessing import Pool
import logging
import re


# Check whether the program is running on Google Colaboratory or not.
try:
    import google.colab
    logging.warning('The program is running on Google Colaboratory.')
    run_on_colaboratory = True
except ImportError:
    run_on_colaboratory = False
    from joblib import Parallel, delayed


# Consts
# OUTPUT_FORMAT is used to output data lines for each books and HEADER too.
OUTPUT_FORMAT = '{authors}\t{title}\t{publisher}\t{publish_year}'

# When fetch a book JSON, we use Parallel to parallelize to reduce running time.
# DEFAULT_CONCURRENCY_LEVEL is specify how many threads to run simultaneously.
# If we pass n_job=-1 to Parallel, Parallel will choose optimized number.
# But the number based on CPU cores and threads.
# This program is NOT CPU-binded BUT HTTP requests-bind.
# So we should specify larger number than CPU cores and threads.
# However too large number also harms the perfomance, so around 100 is adequate.
DEFAULT_CONCURRENCY_LEVEL = 128

# During fetching a JSON, we rewrite the URLs from 'http://...' to 'https://...'
# See also: comments in fetch_and_convert_json_to_dict
COMPILED_HTTP = re.compile('^http://')

# How many results for books fetch from server in default.
DEFAULT_MAX_NUM = 1000

# Search url format
SEARCH_URL_FORMAT = 'https://ci.nii.ac.jp/books/opensearch/search?' \
                    'q={search_string}&' \
                    'publisher={publisher}&' \
                    'year_from={year_from}&' \
                    'year_to={year_to}&' \
                    'format=json&' \
                    'count={max_num}'


# argparse
argparser = ArgumentParser()
argparser.add_argument('--search-string', dest='search_string', nargs='?',
                       metavar='search_str', type=str, default='',
                       help='What string(s) to search for.')
argparser.add_argument('--publisher', dest='publisher', nargs='?',
                       metavar='publisher', type=str, default='',
                       help='What a publisher to search for.')
argparser.add_argument('--year-from', dest='year_from', nargs='?',
                       metavar='year_from', type=int, default=None,
                       help='From what year to search for.')
argparser.add_argument('--year-to', dest='year_to', nargs='?',
                       metavar='year_to', type=int, default=None,
                       help='To what year to search for.')
argparser.add_argument('--max-num', metavar='max_num', type=int,
                       nargs='?', default=DEFAULT_MAX_NUM,
                       help='How many results to fetch in maximum.')
argparser.add_argument('--concurrency-level', dest='n_jobs', metavar='N',
                       type=int, default=DEFAULT_CONCURRENCY_LEVEL,
                       help='How many JSON files to fetch simultaneously.')
argparser.add_argument('--show-progress', dest='show_progress',
                       action='store_true', default=False,
                       help='Show progress during fetching book JSON.')
argparser.add_argument('--debug', dest='log_level', action='store_const',
                       const=logging.DEBUG, default=logging.WARNING,
                       help='Debug mode.')


# Start parameters used when running on Colaboratory
colab_options = []
if run_on_colaboratory:
    # Use from function of Colaboratory
    colab_search_string = ''  # @param {type:"string"}
    colab_options.append(f'--search-string={colab_search_string}')

    colab_publisher = ''  # @param {type:"string"}
    colab_options.append(f'--publisher={colab_publisher}')

    colab_year_from = 0  # @param {type:"integer"}
    colab_options.append(f'--year-from={colab_year_from}')

    colab_year_to = 0  # @param {type:"integer"}
    colab_options.append(f'--year-to={colab_year_to}')

    colab_max_num = 1000  # @param {type:"integer"}
    colab_options.append(f'--max-num={colab_max_num}')

    colab_concurrency_level = 100 # @param {type:"integer"}
    colab_options.append(f'--concurrency-level={colab_concurrency_level}')
    colab_show_progress = False  # @param {type:"boolean"}
    if colab_show_progress:
        colab_options.append('--show-progress')
    colab_debug = False  # @param {type:"boolean"}
    if colab_debug:
        colab_options.append('--debug')
# End parameters


class Person():
    def __init__(self):
        self.name = ''
        self.name_kana = ''
        # self.first_name = ''
        # self.second_name = ''
        # self.first_name_kana = ''
        # self.second_name_kana = ''


class Book():
    def __init__(self):
        self.title = ''
        self.title_kana = ''
        self.authors = []
        self.publish_year = ''
        self.publisher = ''


def fetch_and_convert_json_to_dict(url):
    """
    Fetch a json file via web and convert it to Python dictionary.
    :param str url: url to a JSON file
    :rtype: dict
    :return: dictionary parsed from JSON
    """

    # A URL to a book in JSON file starts with 'http://' But ci.nii.jp will
    # enforce HTTPS, and redirect it to one which starts with 'https://'
    # To reduce over-head per redirects, rewrite the URL.
    url = COMPILED_HTTP.sub('https://', url)
    response = requests.get(url)
    parsed_dict = json.loads(response.text)
    return parsed_dict


def get_book_url_list_from_parsed_dict(parsed_dict):
    """
    Get a list of URLs to JSON of books from dict parsed from JSON.
    :param dict parsed_dict: parsed dictionary from JSON
    :rtype: list[str]
    :return:  a list of books
    """

    books = parsed_dict["@graph"][0]["items"]
    book_urls = [book['rdfs:seeAlso']['@id'] for book in books]

    return book_urls


def parse_author_dicts_to_person(author_dicts):
    """
    Parse dict parsed from JSON to a list of Authors objects.
    :param author_dicts:
    :rtype: list[Person]
    :return: a list of authors
    """
    author_list = []
    for author_dict in author_dicts:
        author = Person()
        author.name = author_dict['foaf:name'][0]['@value']
        if len(author_dict['foaf:name']) > 1:
            author.name_kana = author_dict['foaf:name'][1]['@value']
        author_list.append(author)

    return author_list


def fetch_and_parse_book_json_to_book(book_url):
    """
    Parse dict parsed from JSON to a Book object.
    :param book_url: url to JSON of a book
    :rtype: Book
    :return: a Book object
    """
    parsed_book_dict = fetch_and_convert_json_to_dict(book_url)
    book_data_dict = parsed_book_dict['@graph'][0]
    book = Book()
    book.title = book_data_dict['dc:title'][0]['@value']
    if len(book_data_dict['dc:title']) > 1:
        book.title_kana = book_data_dict['dc:title'][1]['@value']
    if 'foaf:maker' in book_data_dict:
        authors = parse_author_dicts_to_person(book_data_dict['foaf:maker'])
        book.authors = authors
    if 'dc:date' in book_data_dict:
        book.publish_year = book_data_dict['dc:date']
    book.publisher = book_data_dict['dc:publisher'][0]
    return book


def fetch_and_parse_book_urls_to_list_of_book(book_urls,
                                              n_jobs, verbose_level):
    """
    Fetch JSON files of books and parse it to list of Book objects in parallel.
    :param book_urls: list of urls to JSON of book
    :param int n_jobs: number of total process to fetch and parse json
    :param verbose_level: verbose argument passed to Parallel
    :rtype: list[Book]
    :return: a sorted list of Book objects
    """
    if run_on_colaboratory:
        with Pool(processes=n_jobs) as pool:
            books = pool.map(fetch_and_parse_book_json_to_book, book_urls)
    else:
        books = Parallel(n_jobs=n_jobs, verbose=verbose_level)(
            [delayed(fetch_and_parse_book_json_to_book)(url) for url in book_urls]
        )
    return books


def main():
    if run_on_colaboratory:
        args = argparser.parse_args(colab_options)
        logging.warning(f'Args: search_string={args.search_string}, '
                        f'publisher={args.publisher}, '
                        f'year_from={args.year_from}, '
                        f'year_to={args.year_to}, '
                        f'max_num={args.max_num}, '
                        f'show_progress={args.show_progress}, '
                        f'concurrency_level={args.n_jobs}, '
                        f'log_level={args.log_level}')
    else:
        args = argparser.parse_args()
    if not(
        args.search_string or
        args.publisher or
        args.year_from or
        args.year_to
    ):
        print('Need more than one parameter. Abort.')
        return

    search_url = SEARCH_URL_FORMAT.format(
        search_string=args.search_string,
        publisher=args.publisher,
        year_from=args.year_from or '',
        year_to=args.year_to or '',
        max_num=args.max_num
    )
    logging.basicConfig(level=args.log_level)
    n_jobs = args.n_jobs
    if args.show_progress:
        if run_on_colaboratory:
            verbose_level = args.max_num
        else:
            verbose_level = 10
    else:
        verbose_level = 0
    books_dict = fetch_and_convert_json_to_dict(search_url)
    book_urls = get_book_url_list_from_parsed_dict(books_dict)
    books = fetch_and_parse_book_urls_to_list_of_book(
                book_urls,
                n_jobs=n_jobs,
                verbose_level=verbose_level
            )
    print(OUTPUT_FORMAT.format(
        authors='Authors',
        title='Title',
        publisher='Publisher',
        publish_year='Published Year'
    ))
    for book in books:
        authors_str = ', '.join([author.name for author in book.authors])
        print(OUTPUT_FORMAT.format(
            authors=authors_str,
            title=book.title,
            publisher=book.publisher,
            publish_year=book.publish_year
        ))


if __name__ == '__main__':
    main()