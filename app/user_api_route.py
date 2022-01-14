from flask import Blueprint, request, jsonify, url_for


def construct_user_api_blueprint(database, user_service):
    user_api = Blueprint("user_api", __name__)

    @user_api.route("/api/users/profiles")
    def home():
        return common_route()

    def common_route():
        page = request.args.get("page", 1)
        order_by = request.args.get("order_by", None)
        find_by_user = request.args.get("username", None)
        find_by_id = request.args.get("id", None)

        pagination = request.args.get("pagination", None)
        users = user_service.get_all_users_api(
            int(page),
            limit=pagination,
            order_by=order_by,
            find_by_username=find_by_user,
            find_by_id=find_by_id,
        )
        pagination_value = "?page="

        next_url = ""
        prev_url = ""

        if users.has_next:
            next_url = url_for("user_api.home") + "{}{}".format(
                pagination_value, users.next_num
            )

        if users.has_prev:
            prev_url = url_for("user_api.home") + "{}{}".format(
                pagination_value, users.prev_num
            )

        result = {
            "data": [
                {
                    "id": user.id,
                    "username": user.username,
                    "avatar_url": user.avatar_url,
                    "type": user.type,
                    "url": user.URL,
                }
                for user in users.items
            ],
            "main_page_number": users.page,
            "total_pages": users.pages,
            "prev_url": prev_url,
            "next_url": next_url,
        }

        return jsonify(result)

    return user_api
