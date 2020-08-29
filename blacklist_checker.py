import re


class Blacklister:
    def __init__(self):
        self.blacklist_file = open('blacklist.txt', 'r')

    def is_blacklisted(self, url):
        domain = self.get_domain_from_url(url)
        print('Checking blacklist for domain:', domain)

        for line in self.blacklist_file:
            if line.rstrip() == domain:
                return True
        return False

    def get_domain_from_url(self, url):
        domain = ''
        if url.startswith('http'):
            match = re.search(r'(http[s]?:\/\/)([^\/\s]+)(\/.*)', url)
            domain = match.group(2)
        else:
            match = re.search(r'([^\/\s]+)(\/.*)', url)
            domain = match.group(1)
        print('Found domain:', domain)
        return domain
