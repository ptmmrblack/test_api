from flask import Flask, jsonify, abort, request, make_response, url_for, Blueprint
from ..helpers.bphandler import BPHandler

QUESTION_BP = Blueprint('question', __name__)
BPHandler.add_blueprint(QUESTION_BP, url_prefix='/amttest/api')

@QUESTION_BP.route('/sections/<int:section_id>/question', methods=['POST'])
def create_question(section_id):
    """
    creates a new question under a section, question id's will probably all be
    unique but, it seems right to specify the section id every time. mongo
    can assign the question id

    {
        "question":"what is this api even doing?",
        "answers": {
                    "no one knows":False,
                    "testing amtgarders":False,
                    "having a laugh at alex's incompetence":True,
                    "confusing everyone reading it":False
                    },
    }

    """
    message = {}
    message['questoinid'] = 1234
    return make_response(jsonify(message), 201)


@QUESTION_BP.route('/question/<int:question_id>', methods = ['GET'])
def get_question(section_id, question_id):
    """
    may not be needed but returns a specfic question.
    return:
        {
        'question_id as int':
            {
            'question': 'what are we doing',
            'answers':
                [
                    {
                        'answer_id': 5,
                        'answer': 'no one knows',
                        'correct': False
                    },
                    {
                        'answer_id': 6,
                        'answer': 'having a laugh at alex\'s expense',
                        'correct': True
                    },
                ]
            }
        }
    """
    message ={
        'question_id as int':
            {
            'question': 'what are we doing',
            'answers':
                [
                    {
                        'answer_id': 5,
                        'answer': 'no one knows',
                        'correct': False
                    },
                    {
                        'answer_id': 6,
                        'answer': 'having a laugh at alex\'s expense',
                        'correct': True
                    },
                ]
            }
        }
    return make_response((jsonify(message)), 200)


@QUESTION_BP.route('/question/<int:question_id>', methods = ['PUT'])
def update_question(question_id):
    """
    updates a question, so it should probably send the entire question

    args:
    {
        "question":"some updated text?",
    }
    """
    message = {
        "question": "some updated text?",
    }
    return make_response((jsonify(message)), 201)


@QUESTION_BP.route('/question/<int:question_id>', methods = ['DELETE'])
def delete_question(section_id, question_id):
    """
    deletes question from a section
    archive
    """
    result = {}
    result['success'] = True
    result['message'] = 'question %s Deleted' % question_id
    return make_response(jsonify(result), 200)


# there is currently no way to update a questions answers
# gota figure out where to put that route