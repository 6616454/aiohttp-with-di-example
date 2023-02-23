from marshmallow import Schema, fields


class OutputPost(Schema):
    title = fields.Str()
    body = fields.Str()
