class Credentials:
    """
    Credentials class to create new credential instances
    """

    def __init__(self, site_name, user_name, password):
        """
        __init__ to define properties of new Credentials
        Args:
            site_name: Website in which the credentials belong to
            user_name: username for website's account
            password: password for said account
        """

        self.site_name = site_name
        self.user_name = user_name
        self.password = password
