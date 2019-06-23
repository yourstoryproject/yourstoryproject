from pyapp import db

tags = db.Table(
    'tags',
    db.Column(
        'tag_id',
        db.Integer,
        db.ForeignKey('tag.id'),
        primary_key=True),
    db.Column(
        'entry_id',
        db.Integer,
        db.ForeignKey('entry.id'),
        primary_key=True))

admins = db.Table(
    'admins',
    db.Column(
        'account_id',
        db.Integer,
        db.ForeignKey('account.id'),
        primary_key=True))

    # Added admin tble, added account id for admin. how do i check if it matches?
