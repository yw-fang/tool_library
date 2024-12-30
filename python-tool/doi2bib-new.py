#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This script is used for generation of bibtex from the given DOI
# This script was originally from François-Xavier Coudert

import re
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from scholarly import scholarly
import bibtexparser
from bibtexparser.bparser import BibTexParser

def main():
    import codecs
    import locale
    import sys

    if sys.stdout.encoding is None:
        sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

    argv = sys.argv
    if len(argv) < 2:
        print("\nUsage: doi2bib-new.py DOI [...]")
        sys.exit(1)

    for doi in argv[1:]:
        try:
            ref = getCrossRef(doi)
            citation_count = getCitationCount(ref['title'])
            formatted_entry = formatEntry(ref, citation_count)
            print(formatted_entry)
        except Exception as e:
            sys.stderr.write(f"Couldn't process DOI '{doi}': {e}\n")


def getCrossRef(doi):
    if doi.startswith("https://"):
        doi = doi[8:]
    if doi.startswith("doi.org/"):
        doi = doi[8:]

    try:
        params = urlencode({"id": f"doi:{doi}", "noredirect": "true", "format": "unixref"})
        url = Request(f"http://www.crossref.org/openurl/?{params}")
        doc = urlopen(url).read()

        # Try parsing as XML
        try:
            from xml.dom.minidom import parseString
            doc = parseString(doc)
            record = doc.getElementsByTagName("journal")[0]

            def getTagText(parent, tag):
                element = parent.getElementsByTagName(tag)
                return element[0].childNodes[0].data if element and element[0].childNodes else None

            res = {
                "authors": [],
                "title": getTagText(record, "title"),
                "journal": getTagText(record, "full_title"),
                "year": getTagText(record, "year"),
                "volume": getTagText(record, "volume"),
                "pages": getTagText(record, "pages"),
            }

            for author in record.getElementsByTagName("person_name"):
                first_name = getTagText(author, "given_name")
                last_name = getTagText(author, "surname")
                res["authors"].append(f"{first_name} {last_name}" if first_name and last_name else last_name)

            return res
        except Exception:
            # Fall back to parsing BibTeX if XML parsing fails
            bibtex_url = f"https://doi.org/{doi}"
            bibtex_request = Request(bibtex_url, headers={"Accept": "application/x-bibtex"})
            bibtex_response = urlopen(bibtex_request).read().decode("utf-8")

            return parseBibTeX(bibtex_response)

    except Exception as e:
        raise ValueError(f"Error while processing DOI '{doi}': {e}")


def parseBibTeX(bibtex_data):
    # Parse a BibTeX entry into the required dictionary format
    parser = BibTexParser(common_strings=True)
    bib_database = bibtexparser.loads(bibtex_data, parser=parser)
    entry = bib_database.entries[0]

    authors = entry.get("author", "").split(" and ")
    pages = entry.get("pages", "N/A")

    return {
        "authors": authors,
        "title": entry.get("title", "N/A").strip("{}"),
        "journal": entry.get("journal", "N/A"),
        "year": entry.get("year", "N/A"),
        "volume": entry.get("volume", "N/A"),
        "pages": pages,
    }


def getCitationCount(title):
    try:
        # Search for the publication by title
        search_query = scholarly.search_pubs(title)
        for pub in search_query:
            # Attempt to match the title exactly to avoid false positives
            if pub['bib']['title'].lower() == title.lower():
                return pub.get('num_citations', 0)
        return 0  # Return 0 if no exact match is found
    except Exception as e:
        print(f"Error retrieving citation count: {e}")
        return 0


def formatEntry(ref, citation_count):
    authors = ", ".join(ref["authors"])
    title = ref["title"]
    journal = ref["journal"]
    volume = ref.get("volume", "N/A")
    pages = ref.get("pages", "N/A")
    year = ref["year"]

    # Replace with actual impact factor if available
    impact_factor = "[IF Unknown]"

    return (
        f"{authors}: {title}. {journal}, {volume}: {pages}, {year}. "
        f"IF: {impact_factor}, TC: {citation_count}"
    )


if __name__ == '__main__':
    main()

