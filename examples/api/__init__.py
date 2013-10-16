# coding=utf-8

from location import Location
from album import Album
from blog import Blog
from evaluation import Evaluation
from share import Share
from ubb import Ubb
from feed import Feed
from place import Place
from status import Status
from like import Like
from photo import Photo
from checkin import Checkin
from user import User

class RenrenAPI(object):

    def __init__(self, client):
        self.client = client

    def __repr__(self):
        return '<RrenrenClient API>'

    @property
    def location(self):
        return Location(self.client)

    @property
    def album(self):
        return Album(self.client)

    @property
    def blog(self):
        return Blog(self.client)

    @property
    def evaluation(self):
        return Evaluation(self.client)

    @property
    def share(self):
        return Share(self.client)

    @property
    def ubb(self):
        return Ubb(self.client)
    
    @property
    def feed(self):
        return Feed(self.client)

    @property
    def place(self):
        return Place(self.client)

    @property
    def status(self):
        return Status(self.client)

    @property
    def like(self):
        return Like(self.client)

    @property
    def photo(self):
        return Photo(self.client)

    @property
    def checkin(self):
        return Checkin(self.client)

    @property
    def user(self):
        return User(self.client)

