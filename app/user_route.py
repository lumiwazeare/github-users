from flask import Blueprint, request, render_template, url_for


def construct_user_blueprint(database, user_service):
    user_app = Blueprint("user_app", __name__, template_folder="templates")

    @user_app.route("/")
    @user_app.route("/users")
    def home():
        return common_route()

    @user_app.route("/users/<int:page>")
    def home_by_page(page):
        return common_route(page)

    def common_route(page=1):
        pagination = request.args.get("pagination", None)
        users = user_service.get_all_users(int(page), limit=pagination)
        pagination_value = ""
        pages_sum = users.pages

        if pagination is not None:
            pagination_value = "?pagination=" + pagination

        next_url = "javascript:void(0)"
        prev_url = "javascript:void(0)"

        if users.has_next:
            next_url = (
                url_for("user_app.home_by_page", page=users.next_num)
                + pagination_value
            )

        if users.has_prev:
            prev_url = (
                url_for("user_app.home_by_page", page=users.prev_num)
                + pagination_value
            )

        if pages_sum > 6:
            pages_sum = 4

        return render_template(
            "index.html",
            users=users.items,
            pages=users.pages,
            pages_sum=pages_sum,
            limit=pagination_value,
            next_url=next_url,
            prev_url=prev_url,
        )

    return user_app
