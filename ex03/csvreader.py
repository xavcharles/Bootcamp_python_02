class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    
    def __enter__(self):
        with open(self.filename, 'r') as file:
            content = file.readlines()
        n_seps = content[0].count(self.sep)
        for i in range(self.skip_top, len(content) - self.skip_bottom):
            if content[i].count(self.sep) != n_seps:
                return None
            lst = content[i].split(self.sep)
            for s in lst:
                if not s or s.isspace():
                    return None
        return self
    
    def __exit__(self):
        return False
    
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        with open(self.filename, 'r') as file:
            content = file.readlines()
        llst = [[content[i].split(self.sep)] for i in range(self.skip_top, len(content) - self.skip_bottom)]
        # for i in range(self.skip_top, len(content) - self.skip_bottom):
        #     lst = content[i].split(self.sep)
        #     for s in lst:
        #         if not s or s.isspace():
        #             return None
        return llst


    def getheader(self):
        """ Retrieves the header from the csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if not self.header:
            return None
        with open(self.filename, 'r') as file:
            content = file.readlines()
        return content[0]