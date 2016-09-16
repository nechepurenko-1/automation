from model.group import  Group

def test_modify_group_name(app):
    if_exist_group(app)
    app.group.modify_first_group(Group(name="New group"))



def test_modify_group_header(app):
    if_exist_group(app)
    app.group.modify_first_group(Group(header="New header"))


def if_exist_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))