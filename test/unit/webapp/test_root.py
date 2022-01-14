from webapp import client  # noqa: F401; pylint: disable=unused-variable


def test_landing(client):  # noqa: F811; pylint: disable=unused-variable
    landing = client.get("/")
    html = landing.data.decode()

    assert (
        """<div class="col card mb-3">
                <div class="card">
                    <a href="https://api.github.com/users/mojombo">
                        <div class="card-body">
                            <h5 class="card-title">mojombo</h5>
                        </div>
                        <img src="https://avatars.githubusercontent.com/u/1?v=4" class="card-img-bottom" alt="...">

                    </a>
                </div>
            </div>"""
        in html
    )

    assert landing.status_code == 200


def test_landing_with_page_number(client):  # noqa: F811;
    landing = client.get("/users/1")
    html = landing.data.decode()

    assert """1</a></li>""" in html
    assert """2</a></li>""" in html

    assert (
        """<div class="col card mb-3">
                <div class="card">
                    <a href="https://api.github.com/users/mojombo">
                        <div class="card-body">
                            <h5 class="card-title">mojombo</h5>
                        </div>
                        <img src="https://avatars.githubusercontent.com/u/1?v=4" class="card-img-bottom" alt="...">

                    </a>
                </div>
            </div>"""
        in html
    )

    assert landing.status_code == 200
