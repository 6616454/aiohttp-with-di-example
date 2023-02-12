from marshmallow import Schema, fields


class OutputPost(Schema):
    id = fields.Int()
    title = fields.Str()
    body = fields.Str()
