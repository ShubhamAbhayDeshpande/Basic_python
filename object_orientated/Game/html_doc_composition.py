"""
In this program we will create a html document in a pyhton script using composition.
"""

class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self):
        print(self)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' # DOCTYPE does not hava an end tag

class Head(Tag):
    def __init__(self):
        super().__init__('head', '')


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents): # this method will just accept the tag from and pass it on as an argument to the Tag class.
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self):
        for tag in self._body_contents:
            self.contents += str(tag)

            super().display()

class HtmlDoc(object):
    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents): # we could also rename this mehtod any other thing. But, just for the sake of name consistency, we are going to call it add_tag()
        self._body.add_tag(name, contents)

    def display(self):
        self._doc_type.display()
        print('<html>')
        self._body.display()
        print('</html>')

# The following code will create a new html object
if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This text will appear as a paragraph in the html document')
    my_page.display()

    


        



