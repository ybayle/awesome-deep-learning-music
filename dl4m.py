# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# Authors   Yann Bayle
# E-mails   bayle.yann@live.fr
# License   MIT
# Created   16/08/2017
# Updated   06/10/2017
# Version   1.0.0
#

"""
Description of dl4m.py
======================

Parse dl4m.bib to create a simple and readable ReadMe.md table.

..todo::
    sort bib
    add Fig for tasks, wordcloud, dataaugmentation
    bibtexparser accentuation handling
    error handling
    pylint

"""

import os
import sys
import bibtexparser
import numpy as np
import matplotlib.pyplot as plt
from bibtexparser.bwriter import BibTexWriter


def write_bib(bib_database, filen="dl4m.bib"):
    writer = BibTexWriter()
    writer.indent = '  '
    writer.order_entries_by = ('noneyear', "author")
    with open(filen, "w", encoding="utf-8") as bibfile:
        bibfile.write(writer.write(bib_database))


def read_bib(filen="dl4m.bib"):
    """Description of read_bib
    Parse a bib file and load it into memory in a python format
    """
    with open(filen, "r", encoding="utf-8") as bibtex_file:
        bibtex_str = bibtex_file.read()
    bib_database = bibtexparser.loads(bibtex_str)
    return bib_database


def load_bib(filen="dl4m.bib"):
    bib = read_bib(filen)
    write_bib(bib, filen)
    bib = read_bib(filen)
    return bib.entries


def generate_summary_table(bib):
    """Description of generate_summary_table
    Parse dl4m.bib to create a simple and readable ReadMe.md table.
    """
    articles = ""
    for entry in bib:
        if "title" in entry:
            if "link" in entry:
                articles += "| [" + entry["title"] + "](" + entry["link"] + ") | "
            else:
                articles += "| " + entry["title"] + " | "
            if "code" in entry:
                if "No" in entry["code"]:
                    articles += "No "
                else:
                    if "github" in entry["code"]:
                        articles += "[GitHub"
                    else:
                        articles += "[Website"
                    articles += "](" + entry["code"] + ") "
            else:
                articles += "No "
            articles += "|\n"
    table_fn = "paste_in_ReadMe.md"
    with open(table_fn, "w", encoding="utf-8") as filep:
        filep.write(articles)
    print("Summary table saved in", table_fn)


def articles_per_year(bib):
    """Description of main
    Display the number of articles published per year
    input: file name storing articles details
    """
    years = []
    for entry in bib:
        year = int(entry['year'])
        years.append(year)

    plt.xlabel('Years')
    plt.ylabel('Number of articles')
    year_bins = np.arange(min(years), max(years) + 2.0, 1.0)
    plt.hist(years, bins=year_bins, color="#401153", align="left")
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    fig_fn = "fig/articles_per_year.png"
    plt.savefig(fig_fn, dpi=200)
    print("Fig. with number of articles per year saved in", fig_fn)


def get_nb_articles(bib):
    """Description of get_nb_articles
    Count the number of articles in the database
    """
    print("There are", len(bib), "articles.")
    return len(bib)


def get_authors(bib):
    """Description of get_authors
    Print in authors.md the alphabetical list of authors
    """
    authors = []
    for entry in bib:
        for author in entry['author'].split(" and "):
            authors.append(author)
    authors = sorted(set(authors))
    print("There are", len(authors), "researchers working on DL4M.")

    authors_fn = "authors.md"
    with open(authors_fn, "w", encoding="utf-8") as filep:
        filep.write("# List of authors\n\n")
        for author in authors:
            filep.write("- " + author + "\n")
    print("List of authors written in", authors_fn)


def main(filen="dl4m.bib"):
    """Description of main
    Main entry point
    input: file name storing articles details
    """
    bib = load_bib(filen)
    get_nb_articles(bib)
    articles_per_year(bib)
    generate_summary_table(bib)
    get_authors(bib)


if __name__ == "__main__":
    main("dl4m.bib")
