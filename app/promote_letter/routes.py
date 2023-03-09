from app.promote_letter import bp

@bp.route('/ping')
def ping():
    return "ping!"