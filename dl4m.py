# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# Authors   Yann Bayle
# E-mails   bayle.yann@live.fr
# License   MIT
# Created   16/08/2017
# Updated   20/10/2017
# Version   1.0.0
#

"""
Description of dl4m.py
======================

Parse dl4m.bib to create a simple and readable ReadMe.md table.

..todo::
    sort bib
    add Fig for tasks, wordcloud, dataaugmentation
    bibtexparser accentuation handling in authors.md list
    error handling
    report on nb item per ENTRYTYPE
    generate .tsv from .bib
    wordcloud titles, abstract, articles
"""

import numpy as np
import matplotlib.pyplot as plt
import bibtexparser
from bibtexparser.bwriter import BibTexWriter


def write_bib(bib_database, filen="dl4m.bib"):
    """Description of write_bib
    Write the items stored in bib_database into filen
    """
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
    """Description of load_bib
    Load and return the items stored in filen
    """
    bib = read_bib(filen)
    write_bib(bib, filen)
    bib = read_bib(filen)
    return bib.entries


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
    plt.ylabel('Number of Deep Learning articles\n related to Music Information Retrieval')
    year_bins = np.arange(min(years), max(years) + 2.0, 1.0)
    plt.hist(years, bins=year_bins, color="#401153", align="left")
    axe = plt.gca()
    axe.spines['right'].set_color('none')
    axe.spines['top'].set_color('none')
    axe.xaxis.set_ticks_position('bottom')
    axe.yaxis.set_ticks_position('left')
    fig_fn = "fig/articles_per_year.png"
    plt.savefig(fig_fn, dpi=200)
    print("Fig. with number of articles per year saved in", fig_fn)


def get_reproducibility(bib):
    """Description of get_reproducibility
    Generate insights on reproducibility
    """
    cpt = 0
    for entry in bib:
        if "code" in entry:
            if entry["code"][:2] != "No":
                cpt += 1
    print(str(cpt) + " articles provide their source code.")

    return cpt


def get_nb_articles(bib):
    """Description of get_nb_articles
    Count the number of articles in the database
    """
    print("There are", len(bib), "articles referenced.")
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
    nb_authors = len(authors)
    print("There are", nb_authors, "researchers working on DL4M.")

    authors_fn = "authors.md"
    with open(authors_fn, "w", encoding="utf-8") as filep:
        filep.write("# List of authors\n\n")
        for author in authors:
            filep.write("- " + author + "\n")
    print("List of authors written in", authors_fn)

    return nb_authors


def generate_list_articles(bib):
    """Description of generate_list_articles
    From the bib file generates a ReadMe-styled table like:
    | [Name of the article](Link to the .pdf) | Code's link if available |
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

    return articles


def generate_summary_table(bib):
    """Description of generate_summary_table
    Parse dl4m.bib to create a simple and readable ReadMe.md table.
    """
    nb_articles = get_nb_articles(bib)
    nb_repro = get_reproducibility(bib)
    percent_repro = str(int(nb_repro * 100. / nb_articles))
    nb_articles = str(nb_articles)
    nb_repro = str(nb_repro)
    nb_authors = str(get_authors(bib) - 1)
    nb_tasks = str(get_field(bib, "task"))
    nb_datasets = str(get_field(bib, "dataset"))
    nb_archi = str(get_field(bib, "architecture"))
    nb_framework = str(get_field(bib, "framework"))
    articles = generate_list_articles(bib)

    readme_fn = "README.md"
    readme = ""
    pasted_articles = False
    with open(readme_fn, "r", encoding="utf-8") as filep:
        for line in filep:
            if "| " in line[:2] and line[2] != " ":
                if not pasted_articles:
                    readme += articles
                    pasted_articles = True
            elif "papers referenced" in line:
                readme += "- " + nb_articles + " papers referenced. "
                readme += "See the details in [dl4m.bib](dl4m.bib).\n"
            elif "other researchers" in line:
                readme += "- If you are applying DL to music, there are ["
                readme += nb_authors + " other researchers](authors.md) "
                readme += "in your field.\n"
            elif "tasks investigated" in line:
                readme += "- " + nb_tasks + " tasks investigated. "
                readme += "See the list of [tasks](tasks.md).\n"
            elif "datasets used" in line:
                readme += "- " + nb_datasets + " datasets used. "
                readme += "See the list of [datasets](datasets.md).\n"
            elif "architectures used" in line:
                readme += "- " + nb_archi + " architectures used. "
                readme += "See the list of [architectures](architectures.md).\n"
            elif "frameworks used" in line:
                readme += "- " + nb_framework + " frameworks used. "
                readme += "See the list of [frameworks](frameworks.md).\n"
            elif "- Only" in line:
                readme += "- Only " + nb_repro + " articles (" + percent_repro
                readme += "%) provide their source code.\n"
            else:
                readme += line
    with open(readme_fn, "w", encoding="utf-8") as filep:
        filep.write(readme)
    print("New ReadMe generated")


def validate_field(field_name):
    """Description of validate_field
    Assert the validity of the field's name
    """
    fields = ["task", "dataset", "architecture", "author", "dataaugmentation",
              "link", "title", "year", "journal", "code", "ENTRYTYPE",
              "framework"]
    error_str = "Invalid field provided: " + field_name + ". "
    error_str += "Valid fields: " + '[%s]' % ', '.join(map(str, fields))
    assert field_name in fields, error_str

def make_autopct(values):
    """Wrapper for the custom values to display in the pie chart slices
    """
    def my_autopct(pct):
        """Define custom value to print in pie chart
        """
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.1f}%  ({v:d})'.format(p=pct, v=val)
    return my_autopct


def pie_chart(items, field_name, max_nb_slice=7):
    """Description of pie_chart
    Display a pie_chart from the items given in input
    """
    # plt.figure(figsize=(14, 10))
    sizes = []
    labels = sorted(set(items))
    for label in labels:
        sizes.append(items.count(label))

    labels = np.array(labels)
    sizes = np.array(sizes)
    if len(sizes) > max_nb_slice:
        new_labels = []
        new_sizes = []
        for _ in range(0, max_nb_slice):
            index = np.where(sizes == max(sizes))[0]
            if len(index) == len(labels):
                break
            new_labels.append(labels[index][0])
            new_sizes.append(sizes[index][0])
            labels = np.delete(labels, index)
            sizes = np.delete(sizes, index)
        new_labels.append(str(len(labels)) + " others")
        new_sizes.append(sum(sizes))
        labels = np.array(new_labels)
        sizes = np.array(new_sizes)

    colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue",
              "red", "green", "bisque", "lightgrey"]

    tmp_labels = []
    for label in labels:
        if "[" in label:
            label = label[1:].split("]")[0]
        tmp_labels.append(label)
    labels = np.array(tmp_labels)

    # h = plt.pie(sizes, labels=labels, colors=colors, shadow=False,
    plt.pie(sizes, labels=labels, colors=colors, shadow=False,
            startangle=90, autopct=make_autopct(sizes))

    # Display the legend
    # leg = plt.legend(h[0], labels, bbox_to_anchor=(0.08, 0.4))
    # leg.draw_frame(False)
    plt.axis('equal')
    fig_fn = "fig/pie_chart_" + field_name + ".png"
    plt.savefig(fig_fn, dpi=200)
    plt.close()
    print("Fig. with number of articles per year saved in", fig_fn)


def get_field(bib, field_name):
    """Description of get_field
    Generate insights on the field_name in the bib file
    """
    validate_field(field_name)
    nb_article_missing = 0
    fields = []
    for entry in bib:
        if field_name in entry:
            cur_fields = entry[field_name].split(" & ")
            for field in cur_fields:
                fields.append(field)
        else:
            nb_article_missing += 1
    print(str(nb_article_missing) + " entries are missing the " + field_name + " field.")
    nb_fields = len(set(fields))
    print(str(nb_fields) + " unique " + field_name + ".")

    field_fn = field_name + "s.md"
    with open(field_fn, "w", encoding="utf-8") as filep:
        filep.write("# List of " + field_name + "s\n\n")
        filep.write("Please refer to the list of useful acronyms used in deep ")
        filep.write("learning and music: [acronyms.md](acronyms.md).\n\n")
        for field in sorted(set(fields)):
            filep.write("- " + field + "\n")
    print("List of " + field_name + "s written in", field_fn)

    pie_chart(fields, field_name)

    return nb_fields


def create_table(bib, outfilen="dl4m.tsv"):
    """Description of create_table
    Generate human-readable table in .tsv form.
    """

    print("Generating the human-readable table as .tsv")
    # Gather all existing field in bib
    fields = []
    for entry in bib:
        for key in entry:
            fields.append(key)

    print("Available fields:")
    print(set(fields))
    fields = ["year", "ENTRYTYPE", "title", "author", "link", "code", "task",
              "reproducible", "dataset", "framework", "architecture", "dropout",
              "batch", "epochs", "dataaugmentation", "input", "dimension",
              "activation", "loss", "learningrate", "optimizer", "gpu"]
    print("Fields taken in order (in this order):")
    print(fields)

    separator = "\t"
    str2write = ""
    for field in fields:
        str2write += field.title() + separator
    str2write += "\n"
    for entry in bib:
        for field in fields:
            if field in entry:
                str2write += entry[field]
            str2write += separator
        str2write += "\n"
    with open(outfilen, "w", encoding="UTF-8") as filep:
        filep.write(str2write)


def where_published(bib):
    """Display insights on where the articles have been published
    """
    journals = []
    conf = []
    for entry in bib:
        if "article" in entry["ENTRYTYPE"]:
            journals.append(entry["journal"])
        elif "inproceedings" in entry["ENTRYTYPE"]:
            conf.append(entry["booktitle"])
    journals = sorted(set(journals))
    conf = sorted(set(conf))

    with open("publication_type.md", "w") as filep:
        filep.write("# List of publications type\n\n### Journals:\n\n- ")
        filep.write("\n- ".join(journals))
        filep.write("\n\n### Conferences:\n\n- ")
        filep.write("\n- ".join(conf))
        filep.write("\n")


def main(filen="dl4m.bib"):
    """Description of main
    Main entry point
    input: file name storing articles details
    """
    bib = load_bib(filen)
    generate_summary_table(bib)
    articles_per_year(bib)
    create_table(bib)
    where_published(bib)


if __name__ == "__main__":
    main("dl4m.bib")
