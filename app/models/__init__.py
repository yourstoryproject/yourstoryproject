from app import db


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
