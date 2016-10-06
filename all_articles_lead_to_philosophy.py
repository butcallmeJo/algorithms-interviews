#!/usr/bin/env python

"""script to input a wikipedia article and iterate until Philosophy is reached
"""

"""TODO:
- Fabricate article link from normal words (guess article from words with space)
- article checking / formatting (better)
"""

import sys
import requests
import argparse
import re

def get_next_article(article_link):
    """function"""
    article_resp = requests.get(article_link)
    print article_resp.status_code
    print article_link
    content = article_resp.text
    get_p = content.split('<p>')
    print get_p
    new_path = re.search(
        '<a\s+(?:[^>]*?\s+)?href=\"(\/wiki\/[^\"]*)\"', get_p[1]
    ).group(1)
    new_link = new_path.split('/')[-1]
    print new_link
    if new_link == "/wiki/Philosophy":
        print "We have reach enlightenment! <3"
    elif '(' and ')' in new_link:
        print "Sorry, program not perfect yet"
    else:
        get_next_article(get_article_link(new_link))


def get_article_link(article):
    """function to get the actual url from user input
    article: string - user input
    """
    # last_part is the format of the wiki article for the URL
    last_part = '_'.join(article.split(' '))
    article_link = "https://en.wikipedia.org/wiki/" + last_part
    return article_link

def main(argv):
    parser = argparse.ArgumentParser(
        description="Script to iterate over Wikipedia articles until the \
        Philosophy article is reached"
    )
    parser.add_argument(
        '--article_path', '-a', type=str, required=True, metavar='"ARTICLE"',
        dest='article',
        help=("input the wikipedia article here")
    )
    args = parser.parse_args(argv[1:])

    article_link = get_article_link(args.article)
    get_next_article(article_link)


if __name__ == "__main__":
    main(sys.argv)