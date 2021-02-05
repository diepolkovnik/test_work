from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Notes_db(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	last_name = db.Column(db.String(100), nullable=False)
	number = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return f"Notes(name = {name}, last_name = {views}, number = {likes})"

notes_put_args = reqparse.RequestParser()
notes_put_args.add_argument("name", type=str, help="Name person", required=True)
notes_put_args.add_argument("last_name", type=str, help="last_name person", required=True)
notes_put_args.add_argument("number", type=str, help="number of person", required=True)

notes_update_args = reqparse.RequestParser()
notes_update_args.add_argument("name", type=str, help="name req person")
notes_update_args.add_argument("last_name", type=str, help="last_name of person")
notes_update_args.add_argument("number", type=str, help="number of person")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'last_name': fields.String,
	'number': fields.String
}

class Notes(Resource):
	@marshal_with(resource_fields)
	def get(self, note_id):
		result = Notes_db.query.filter_by(id=note_id).first()
		if not result:
			abort(404, message="notes is 404")
		return result

	@marshal_with(resource_fields)
	def put(self, note_id):
		args = notes_put_args.parse_args()
		result = Notes_db.query.filter_by(id=note_id).first()
		if result:
			abort(409, message="Notes id taken...")

		notes = Notes_db(id=video_id, name=args['name'], last_name=args['last_name'], number=args['number'])
		db.session.add(video)
		db.session.commit()
		return notes, 201

	@marshal_with(resource_fields)
	def patch(self, note_id):
		args = notes_update_args.parse_args()
		result = Notes_db.query.filter_by(id=note_id).first()
		if not result:
			abort(404, message="note_id doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result


	def delete(self, note_id):
		personisnotexist(note_id)
		del notes[note_id]
		return '', 204


api.add_resource(Notes, "/notes/<int:note_id>")

if __name__ == "__main__":
	app.run(debug=True)