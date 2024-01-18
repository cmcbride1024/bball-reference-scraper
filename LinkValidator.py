class LinkValidator:
    def __init__(self, domain, forbidden_paths=None):
        if forbidden_paths is None:
            forbidden_paths = []
        self.domain = domain
        self.forbidden_paths = forbidden_paths

    def can_follow_link(self, url):
        return self.domain in url and True not in [self.domain + path in url for path in self.forbidden_paths]
