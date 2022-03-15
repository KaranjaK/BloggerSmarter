import unittest
from app.main.views import subscribe
from app.models import User, Blog, Comment, Quote, Subscriber

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_safe is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_kelvin = User(username='kk', password='hihi', email='test@test.com')
        self.new_blog = Blog(id=1, title='Test', content='This is a test blog', user_id=self.user_charles.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.content, 'This is a test blog')
        self.assertEquals(self.new_blog.user_id, self.user_kelvin.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        get_blog = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        
        self.new_comment = Comment(id = 1, comment = 'Test comment', user = self.user_kk, blog_id = self.new_blog)
        
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_kk)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)

class QuoteModelTest(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quote(id = 1, quote = 'Test quote')

class SubscriberModelTest(unittest.TestCase):
    def setUp(self):
        self.new_subscriber= Subscriber(id=1, subscriber = 'Test Subscriber', user = self.user_kk)


if __name__ == '__main__':
    unittest.main()