class Portfolio:
    def __init__(self, session):
        """
        Initialize Accounts object with session and account information

        :param session: authenticated session
        """
        self.session = session
        self.account = {}
