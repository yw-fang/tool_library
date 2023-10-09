#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This script is used for generation of bibtex from the given DOI
# This script was originally from François-Xavier Coudert

import re
from urllib.parse import urlencode
from urllib.request import urlopen, Request


def main():
  import codecs
  import locale
  import sys

  # Set our output to the right encoding if none was chosen
  if sys.stdout.encoding is None:
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

  argv = sys.argv
  if '--doikey' in argv:
    argv.remove('--doikey')
    doiKey = True
  else:
    doiKey = False

  if len(argv) < 2:
    print("\nUsage: doi2bib DOI [...]\n")
    sys.exit(1)
  else:
    for doi in argv[1:]:
      try:
        ref = getCrossRef(doi, doiKey)
      except Exception as e:
        sys.stderr.write("Couldn't resolve DOI '" + doi + "' through CrossRef: " + str(e) + "\n")
        return

      print(bibtexEntry(ref))


################################################################
# LaTeX accents replacement
latexAccents = {
  "à": "\\`a" ,	# Grave accent
  "è": "\\`e" ,
  "ì": "\\`{\\i}" ,
  "ò": "\\`o" ,
  "ù": "\\`u" ,
  "ỳ": "\\`y" ,
  "À": "\\`A" ,
  "È": "\\`E" ,
  "Ì": "\\`{\\I}" ,
  "Ò": "\\`O" ,
  "Ù": "\\`U" ,
  "Ỳ": "\\`Y" ,
  "á": "\\'a" ,	# Acute accent
  "ć": "\\'c" ,
  "é": "\\'e" ,
  "í": "\\'{\\i}" ,
  "ó": "\\'o" ,
  "ú": "\\'u" ,
  "ý": "\\'y" ,
  "Á": "\\'A" ,
  "É": "\\'E" ,
  "Í": "\\'{\\I}" ,
  "Ó": "\\'O" ,
  "Ú": "\\'U" ,
  "Ý": "\\'Y" ,
  "â": "\\^a" ,	# Circumflex
  "ê": "\\^e" ,
  "î": "\\^{\\i}" ,
  "ô": "\\^o" ,
  "û": "\\^u" ,
  "ŷ": "\\^y" ,
  "Â": "\\^A" ,
  "Ê": "\\^E" ,
  "Î": "\\^{\\I}" ,
  "Ô": "\\^O" ,
  "Û": "\\^U" ,
  "Ŷ": "\\^Y" ,
  "ä": "\\\"a" ,	# Umlaut or dieresis
  "ë": "\\\"e" ,
  "ï": "\\\"{\\i}" ,
  "ö": "\\\"o" ,
  "ü": "\\\"u" ,
  "ÿ": "\\\"y" ,
  "Ä": "\\\"A" ,
  "Ë": "\\\"E" ,
  "Ï": "\\\"{\\I}" ,
  "Ö": "\\\"O" ,
  "Ü": "\\\"U" ,
  "Ÿ": "\\\"Y" ,
  "ã": "\\~{a}" ,	# Tilde
  "ñ": "\\~{n}" ,
  "ă": "\\u{a}" ,	# Breve
  "ĕ": "\\u{e}" ,
  "ŏ": "\\u{o}" ,
  "š": "\\v{s}" ,	# Caron
  "č": "\\v{c}" ,
  "ž": "\\v{z}" ,
  "ç": "\\c{c}" ,	# Cedilla
  "Ç": "\\c{C}" ,
  "œ": "{\\oe}" ,	# Ligatures
  "Œ": "{\\OE}" ,
  "æ": "{\\ae}" ,
  "Æ": "{\\AE}" ,
  "å": "{\\aa}" ,
  "Å": "{\\AA}" ,
  "–": "--" ,	# Dashes
  "—": "---" ,
  "−": "--" ,
  "ø": "{\\o}" ,	# Misc latin-1 letters
  "Ø": "{\\O}" ,
  "ß": "{\\ss}" ,
  "¡": "{!`}" ,
  "¿": "{?`}" ,
  "\\": "\\\\" ,	# Characters that should be quoted
  "~": "\\~" ,
  "&": "\\&" ,
  "$": "\\$" ,
  "{": "\\{" ,
  "}": "\\}" ,
  "%": "\\%" ,
  "#": "\\#" ,
  "_": "\\_" ,
  "≥": "$\\ge$" ,	# Math operators
  "≤": "$\\le$" ,
  "≠": "$\\neq$" ,
  "©": "\copyright" , # Misc
  "ı": "{\\i}" ,
  "α": "$\\alpha$" ,
  "β": "$\\beta$" ,
  "γ": "$\\gamma$" ,
  "δ": "$\\delta$" ,
  "ε": "$\\epsilon$" ,
  "η": "$\\eta$" ,
  "θ": "$\\theta$" ,
  "λ": "$\\lambda$" ,
  "µ": "$\\mu$" ,
  "ν": "$\\nu$" ,
  "π": "$\\pi$" ,
  "σ": "$\\sigma$" ,
  "τ": "$\\tau$" ,
  "φ": "$\\phi$" ,
  "χ": "$\\chi$" ,
  "ψ": "$\\psi$" ,
  "ω": "$\\omega$" ,
  "°": "$\\deg$" ,
  "‘": "`" ,	# Quotes
  "’": "'" ,
  "′": "$^\\prime$" ,
  "“": "``" ,
  "”": "''" ,
  "‚": "," ,
  "„": ",," ,
  "\xa0": " " ,     # Unprintable characters
}

def replaceLatexAccents(str):
  import unicodedata
  s = unicodedata.normalize('NFC', str)
  return "".join([ latexAccents[c] if c in latexAccents else c for c in s ])


################################################################
def validateDOI(doi):
  # We check that the DOI can be resolved by official means.  If so, we
  # return the resolved URL, otherwise, we return None (which means the
  # DOI is invalid).
  try:
    handle = urlopen("http://doi.org/" + doi)
  except:
    return None

  resolvedURL = handle.geturl()
  if resolvedURL[0:15] == "http://doi.org/":
    return None
  else:
    return resolvedURL


################################################################
# CrossRef queries
#
# CrossRef documentation comes from here:
# http://labs.crossref.org/site/quick_and_dirty_api_guide.html
#
# You need a CrossRef API key. 
#
crossRefKey = "fx.coudert@chimie-paristech.fr"
#
# Using Google allows one to find other API keys:
# zter:zter321
# ourl_rdmpage:peacrab
# egon@spenglr.com
# s_allannz@yahoo.com
# dollar10boy@hotmail.com


def getCrossRef(doi, doiKey):
  import xml.dom.minidom

  # Maybe we got a DOI URL instead of the DOI itself -- strip prefix
  if doi[0:8] == "https://": doi = doi[8:]
  if doi[0:7] == "http://": doi = doi[7:]
  if doi[0:3] == "dx.": doi = doi[3:]
  if doi[0:8] == "doi.org/": doi = doi[8:]

  # Get the XML from CrossRef
  params = urlencode({ "id" : "doi:" + doi, "noredirect" : "true",
                       "pid" : crossRefKey, "format" : "unixref" })
  url = Request("http://www.crossref.org/openurl/?" + params)
  doc = urlopen(url).read()

  # Parse it
  doc = xml.dom.minidom.parseString (doc)
  records = doc.getElementsByTagName("journal")

  # No results. Is it a valid DOI?
  if (len(records) == 0):
    res = validateDOI(doi)
    if res is None:
      raise Exception("Invalid DOI")
    else:
      raise Exception("Can't locate metadata")

  if (len(records) != 1):
    raise Exception("CrossRef returned more than one record")

  record = records[0]

  # Helper functions
  def findItemNamed(container, name):
    x = container.getElementsByTagName(name)
    if (len(x) == 0):
      return None
    else:
      return x[0]

  def data(node):
    if node is None:
      return None
    else:
      return "".join([x.toxml().strip() for x in node.childNodes])

  res = {}

  # Journal information
  journal = findItemNamed(record, "journal_metadata")
  if (journal):
    res["fullJournal"] = data(findItemNamed(journal, "full_title"))
    res["shortJournal"] = data(findItemNamed(journal, "abbrev_title"))

  # Volume information
  issue = findItemNamed(record, "journal_issue")
  res["issue"] = data(findItemNamed(issue, "issue"))
  res["volume"] = data(findItemNamed(issue, "volume"))
  res["year"] = data(findItemNamed(issue, "year"))
  res["month"] = data(findItemNamed(issue, "month"))

  # Other information
  other = findItemNamed(record, "journal_article")
  res["title"] = data(findItemNamed(other, "title"))
  res["firstPage"] = data(findItemNamed(other, "first_page"))
  res["lastPage"] = data(findItemNamed(other, "last_page"))
  res["doi"] = data(findItemNamed(other, "doi"))
  if res["year"] is None:
    res["year"] = data(findItemNamed(other, "year"))
  if res["month"] is None:
    res["month"] = data(findItemNamed(other, "month"))

  # Author list
  res["authors"] = []
  for node in other.getElementsByTagName("person_name"):
    surname = data(findItemNamed(node, "surname"))
    givenName = data(findItemNamed(node, "given_name"))

    if givenName is None:
      res["authors"].append(surname)
    elif surname is None:
      res["authors"].append(givenName)
    else:
      # res["authors"].append(surname + ", " + givenName)
      res["authors"].append(givenName + " " + surname)

  # Create a citation key
  if doiKey:
    key = doi
  else:
    r = re.compile("\W")
    if len(res["authors"]) > 0:
      key = r.sub('', res["authors"][0].split(",")[0])
    else:
      key = ""
    if res["year"] is not None:
      key = key + res["year"]
    if res["month"] is not None:
      key = key + res["month"]

  res["key"] = key

  return res


def bibtexEntry(ref):

  # Output all information in bibtex format
  latex = replaceLatexAccents
  s = "@article{" + ref["key"] + ",\n"

  if ref["title"] is not None:
    s = s + "\"" + latex(ref["title"]) + "\", "

  if len(ref["authors"]) > 0:
    s = s + "" + latex(" and ".join(ref["authors"])) + ", "

  if ref["shortJournal"] is not None:
    s = s + "" + latex(ref["shortJournal"]) + ", "
  if ref["volume"] is not None:
    s = s + "vol. " + latex(ref["volume"]) + ", "
  if ref["firstPage"] is not None:
    if ref["lastPage"] is not None:
      s = s + "pp. " + latex(ref["firstPage"]) + "-" + latex(ref["lastPage"]) + ", "
    else:
      s = s + "pp. " + latex(ref["firstPage"]) + ", "
  if ref["month"] is not None:
    s = s + "" + latex(ref["month"]) + " "
  if ref["year"] is not None:
    s = s + "" + latex(ref["year"]) + "\n"
#   if ref["issue"] is not None:
#     s = s + "  issue = { " + latex(ref["issue"]) + " },\n"
#  s += '  doi = {' + ref['doi'] + '},\n'
#  s += '  url = {http://doi.org/' + ref['doi'] + '},\n'

  s = s + "}"
  return s


if __name__ == '__main__':
    main()
