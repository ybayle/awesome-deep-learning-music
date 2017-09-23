# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# Authors   Yann Bayle
# E-mails   bayle.yann@live.fr
# License   MIT
# Created   16/08/2017
# Updated   23/09/2017
# Version   1.0.0
#

"""
Description of dl4m.py
======================

Parse dl4m.csv to create a simple and readable ReadMe.md table.

"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt


def generate_summary_table(filen="dl4m.tsv"):
    """Description of generate_summary_table
    Parse dl4m.csv to create a simple and readable ReadMe.md table.
    """
    if not os.path.isfile(filen):
        print("Invalid input file name provided")
        sys.exit()
    articles = ""
    with open(filen, "r", encoding="utf-8") as filep:
        # Skip csv header
        next(filep)
        for line in filep:
            row = line.split("\t")
            articles += "| [" + row[0] + "](" + row[4] + ") | "
            if len(row[5]) > 1:
                if "No" in row[5]:
                    articles += "No "
                else:
                    if "github" in row[5]:
                        articles += "[GitHub"
                    else:
                        articles += "[Website"
                    articles += "](" + row[5] + ") "
            articles += "|\n"
    table_fn = "paste_in_ReadMe.md"
    with open(table_fn, "w", encoding="utf-8") as filep:
        filep.write(articles)
    print("Summary table saved in", table_fn)


def articles_per_year(filen="dl4m.tsv"):
    """Description of main
    Display the number of articles published per year
    input: file name storing articles details
    """
    years = []
    with open(filen, "r", encoding="utf-8") as filep:
        next(filep)
        for line in filep:
            years.append(int(line.split("\t")[2]))

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


def get_nb_articles(filen="dl4m.tsv"):
    """Description of get_nb_articles
    Count the number of articles in the database
    input: file name storing articles details
    """
    cpt = 0
    with open(filen, "r", encoding="utf-8") as filep:
        next(filep)
        for line in filep:
            cpt += 1
    print("There are", cpt, "articles.")
    return cpt


def main(filen="dl4m.tsv"):
    """Description of main
    Main entry point
    input: file name storing articles details
    """
    get_nb_articles(filen)
    generate_summary_table(filen)
    articles_per_year(filen)


if __name__ == "__main__":
    main()
