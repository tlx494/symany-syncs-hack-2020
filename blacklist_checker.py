import re


def is_blacklisted(url):
    domain = get_domain_from_url(url)
    f = open('blacklist.txt', 'r')
    for line in f:
        if line.rstrip() == domain:
            return True
    return False


def get_domain_from_url(url):
    domain = ''
    if url.startswith('http'):
        match = re.search(r'(http[s]?:\/\/)([^\/\s]+)(\/.*)', url)
        domain = match.group(2)
    else:
        match = re.search(r'([^\/\s]+)(\/.*)', url)
        domain = match.group(1)
    print('Found domain:', domain)
    return domain
