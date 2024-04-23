import sender_stand_request
import data


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body['firstName'] = first_name
    return current_body


def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body('Aa')
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()['authToken'] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

