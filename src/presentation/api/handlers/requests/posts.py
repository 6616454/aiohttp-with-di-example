from marshmallow import Schema, fields


class OnePostRequestSchema(Schema):
    id = fields.Int(required=True)




