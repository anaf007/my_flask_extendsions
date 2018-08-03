from my_flask_extendsions.user.models import User
from my_flask_extendsions.extensions import api_manager
from flask import current_app


api_manager.create_api(User,
    methods=['GET'],
    url_prefix='/api/v1/test',
    results_per_page=20,
    # code=0,
)

