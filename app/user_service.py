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

    def get_all_users_api(
        self,
        page=1,
        limit=25,
        order_by=None,
        find_by_username=None,
        find_by_id=None,
    ):
        if page is None:
            page = 1

        if limit is None:
            limit = 25
        else:
            limit = int(limit)

        query = self.user_model.query

        if order_by == "id":
            query = query.order_by(self.user_model.id.asc())

        elif order_by == "type":
            query = query.order_by(self.user_model.type.asc())

        if find_by_username is not None:
            query = query.filter(
                self.user_model.username.contains(find_by_username)
            )

        if find_by_id is not None:
            query = query.filter(self.user_model.id == int(find_by_id))

        return query.paginate(page, limit, False)
