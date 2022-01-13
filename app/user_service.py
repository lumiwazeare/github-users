class UserService:
    def __init__(self, userModel) -> None:
        self.user_model = userModel

    def get_all_users(self, page=1, limit=25):
        if page is None:
            page = 1

        if limit is None:
            limit = 25
        else:
            limit = int(limit)

        return self.user_model.query.paginate(page, limit, False)
