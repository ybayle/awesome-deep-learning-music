import argparse
import os
import re
import multiprocessing as mp

from tqdm import tqdm

from client import Downloader
from dl4m import *


def main(args):
    bib = load_bib(args.filename)

    print('Generating files list ...')
    data = []
    for item in tqdm(bib):
        year = item['year']
        title = item['title'].replace(' ', '_')
        auth1 = re.split(' |,', item['author'])[0]
        item_str = '{:s}_{:s}_{:s}'.format(year, auth1, title)
        item_str = item_str[:40]

        if 'link' not in item:
            tqdm.write('Skip item ' + item_str + ': No link is provided')
            continue

        link = item['link']
        if not link.endswith('.pdf'):
            tqdm.write('Skip item ' + item_str + ': The link is not a pdf')
            continue

        filename = item_str + '.pdf'
        item_dict = dict(name=filename, link=link, year=year, title=title, auth1=auth1)
        data.append(item_dict)
    print('')
    print('File list is now generated')
    print('')

    # Create line format to print pretty
    max_len = 0
    for paper in data:
        max_len_new = len(paper['title'])
        if max_len < max_len_new:
            max_len = max_len_new
    line_format = \
            '{:4s}' + \
            '  ' + \
            '{:' + str(max_len) + 's}' + \
            '  ' + \
            '{:s}'

    # Print the results
    print(line_format.format('YEAR', 'TITLE', '1st AUTHOR'))
    for paper in data:
        print(line_format.format(paper['year'], paper['title'], paper['auth1']))

    # Search website for more information
    print('')
    print('Download papers from online ...')
    if not os.path.isdir(args.dirname):
        os.mkdir(args.dirname)
    downloader = Downloader(args.dirname)

    if args.use_single_thread:
        # Single-threaded downloader
        for paper in tqdm(data):
            downloader.client(paper)
    else:
        # Multi-threaded downloader
        pbar = tqdm(total=len(data))
        def update_pbar(*args):
            pbar.update()

        pool = mp.Pool(mp.cpu_count())
        for i in range(len(data)):
            pool.apply_async(downloader.client, args=(data[i],), callback=update_pbar)
        pool.close()
        pool.join()
    print('')
    print('Download is now complete')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Paper downloader')
    parser.add_argument('--filename', '-f', type=str, default='dl4m.bib',
            help='search database')
    parser.add_argument('--dirname', '-d', type=str, default='downloads',
            help='download directory')
    parser.add_argument('--use-single-thread', '-s', action='store_true',
            help='use single thread for downloading')
    args = parser.parse_args()

    main(args)
